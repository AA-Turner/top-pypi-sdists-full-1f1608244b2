import enum
import time
import heapq
import asyncio
import logging
import calendar
import datetime
import itertools
from datetime import timezone as tz
from collections.abc import Iterable, Mapping

import synapse.exc as s_exc
import synapse.common as s_common

import synapse.lib.base as s_base
import synapse.lib.coro as s_coro

# Agenda: manages running one-shot and periodic tasks in the future ("appointments")

logger = logging.getLogger(__name__)

def _dayofmonth(hardday, month, year):
    '''
    Returns a valid day of the month given the desired value.

    Negative values are interpreted as offset backwards from the last day of the month, with -1 representing the
    last day of the month.  Out-of-range values are clamped to the first or last day of the month.
    '''
    newday = hardday
    daysinmonth = calendar.monthrange(year, month)[1]
    if newday < 0:
        newday = daysinmonth + hardday + 1
    newday = max(1, min(newday, daysinmonth))
    return newday

class TimeUnit(enum.IntEnum):
    '''
    Unit of time that recurring and required parts of appointments are made of
    '''
    YEAR = enum.auto()
    MONTH = enum.auto()
    DAYOFMONTH = enum.auto()  # e.g. every 3rd of the month
    DAYOFWEEK = enum.auto()   # e.g. every Tuesday (Mon=0, Sun=6)
    DAY = enum.auto()         # every day
    HOUR = enum.auto()
    MINUTE = enum.auto()
    NOW = enum.auto()

    @classmethod
    def fromString(cls, s):
        return cls.__members__[s.upper()]

# Next largest unit for each unit
_NextUnitMap = {
    TimeUnit.YEAR: None,
    TimeUnit.MONTH: TimeUnit.YEAR,
    TimeUnit.HOUR: TimeUnit.DAY,
    TimeUnit.MINUTE: TimeUnit.HOUR,
    TimeUnit.DAYOFMONTH: TimeUnit.MONTH,
    TimeUnit.DAYOFWEEK: TimeUnit.DAYOFWEEK,
}

# Unit equivalence to datetime arguments
_TimeunitToDatetime = {
    TimeUnit.YEAR: 'year',
    TimeUnit.MONTH: 'month',
    TimeUnit.DAYOFMONTH: 'day',
    TimeUnit.DAYOFWEEK: 'day',
    TimeUnit.DAY: 'day',
    TimeUnit.HOUR: 'hour',
    TimeUnit.MINUTE: 'minute',
}

# The valid ranges for required and recurring
_UnitBounds = {
    TimeUnit.YEAR: ((2000, 2999), (1, 5)),
    TimeUnit.MONTH: ((1, 12), (1, 60)),
    TimeUnit.DAYOFMONTH: ((-31, 31), (-31, 31)),
    TimeUnit.DAYOFWEEK: ((0, 6), (0, 6)),
    TimeUnit.DAY: ((0, 0), (1, 365 * 5)),
    TimeUnit.HOUR: ((0, 23), (1, 1000)),
    TimeUnit.MINUTE: ((0, 59), (1, 60 * 60 * 24 * 30))
}

class ApptRec:
    '''
    Represents a single element of a single combination of an appointment
    '''
    def __init__(self, reqdict, incunit=None, incval=1):
        if incunit is not None:
            incunit = TimeUnit(incunit)
        self.incunit = incunit
        self.incval = incval if incunit is not None else None

        if not reqdict and incunit is None:
            raise s_exc.BadTime(mesg='reqdict must be nonempty or incunit must be non-None')

        if TimeUnit.DAY in reqdict:
            raise s_exc.BadTime(mesg='Must not specify day as requirement')

        if TimeUnit.DAYOFMONTH in reqdict and TimeUnit.DAYOFWEEK in reqdict:
            raise s_exc.BadTime(mesg='Both day of month and day of week must not both be requirements')

        if TimeUnit.DAYOFWEEK in reqdict and incunit is not None:
            raise s_exc.BadTime(mesg='Day of week requirement not supported with a recurrence')

        if incunit == TimeUnit.DAYOFMONTH:
            raise s_exc.BadTime(mesg='Day of month not a valid incunit')

        if incunit is not None:
            boundmin, boundmax = _UnitBounds[incunit][1]
            if not boundmin <= incval <= boundmax:
                raise s_exc.BadTime(mesg='Out of bounds incval')

        reqdict = {TimeUnit(k): v for k, v in reqdict.items()}
        self.reqdict = reqdict

        for reqkey, reqval in reqdict.items():
            boundmin, boundmax = _UnitBounds[reqkey][0]
            if not boundmin <= reqval <= boundmax:
                raise s_exc.BadTime(mesg='Out of bounds reqdict value')

            if incunit is not None and reqkey <= incunit:
                # We could, actually support this, but most of these combinations are nonsensical (e.g. run every 5
                # minutes in 2018 only?)
                raise s_exc.BadTime(mesg='Must not have fixed unit equal to or greater than recurrence unit')

        self.reqdict = {}
        # Put keys in size order, with dayof... added last, as nexttime processes in that order
        for key in _NextUnitMap:
            if key in reqdict:
                self.reqdict[key] = reqdict[key]

    def __repr__(self):
        return repr(self.pack())

    def pack(self):
        '''
        Make ApptRec json/msgpack-friendly
        '''
        reqdictf = {k.name.lower(): v for (k, v) in self.reqdict.items()}
        incunitf = None if self.incunit is None else self.incunit.name.lower()
        return (reqdictf, incunitf, self.incval)

    @classmethod
    def unpack(cls, val):
        '''
        Convert from json/msgpack-friendly
        '''
        reqdictf, incunitf, incval = val
        reqdict = {TimeUnit[k.upper()]: v for (k, v) in reqdictf.items()}
        incunit = None if incunitf is None else TimeUnit[incunitf.upper()]
        return cls(reqdict, incunit, incval)

    def nexttime(self, lastts):
        '''
        Returns next timestamp that meets requirements, incrementing by (self.incunit * incval) if not increasing, or
        0.0 if there are no future matches
        '''
        lastdt = datetime.datetime.fromtimestamp(lastts, tz.utc)
        newvals = {}  # all the new fields that will be changed in datetime of lastts

        # Truncate the seconds part
        newdt = lastdt.replace(second=0)

        # Note: self.reqdict is sorted from largest unit to smallest
        for unit, newval in self.reqdict.items():
            dtkey = _TimeunitToDatetime[unit]

            if unit is TimeUnit.DAYOFWEEK:
                newdt = newdt.replace(**newvals)
                newvals = {}
                newval = newdt.day + (6 + newval - newdt.weekday()) % 7 + 1
                if newval > calendar.monthrange(newdt.year, newdt.month)[1]:
                    newval -= 7

            elif unit is TimeUnit.YEAR:
                # As we change the year, clamp the day of the month to a valid value (only matters on leap day)
                dayval = _dayofmonth(newdt.day, newdt.month, newval)
                newvals['day'] = dayval

            elif unit is TimeUnit.MONTH:
                # As we change the month, clamp the day of the month to a valid value
                newdt = newdt.replace(**newvals)
                newvals = {}
                dayval = _dayofmonth(newdt.day, newval, newdt.year)
                newvals['day'] = dayval

            elif unit is TimeUnit.DAYOFMONTH:
                newdt = newdt.replace(**newvals)
                newvals = {}
                newval = _dayofmonth(newval, newdt.month, newdt.year)

            newvals[dtkey] = newval

        newdt = newdt.replace(**newvals)

        # Then move forward if we have to
        if newdt <= lastdt or \
                self.incunit == TimeUnit.DAYOFWEEK and newdt.weekday() != self.incval:
            if self.incunit is None:
                largest_req = min(self.reqdict.keys())
                tmpunit = _NextUnitMap[largest_req]
                if tmpunit is None:  # required a year and we're already there
                    return 0.0
                # Unless we're going to the next day of week, increment by 1 unit of the next larger unit
                tmpincval = self.reqdict.get(TimeUnit.DAYOFWEEK, 1)
            else:
                tmpunit = self.incunit
                tmpincval = self.incval
            newdt = self._inc(tmpunit, tmpincval, self.reqdict, lastdt, newdt)
            assert newdt > lastdt
        return newdt.timestamp()

    def _inc(self, incunit, incval, reqdict, origdt, dt):
        '''
        Return a datetime incremented by incunit * incval
        '''
        if incunit == TimeUnit.YEAR:
            return dt.replace(year=dt.year + incval)
        if incunit == TimeUnit.MONTH:
            newyear = dt.year
            absmonth = dt.month + incval - 1
            newmonth = absmonth % 12 + 1
            newyear += absmonth // 12
            daysinmonth = calendar.monthrange(newyear, newmonth)[1]
            dayofmonthreq = reqdict.get(TimeUnit.DAYOFMONTH)
            if dayofmonthreq is not None:
                newday = _dayofmonth(dayofmonthreq, newmonth, newyear)
            else:
                newday = min(daysinmonth, dt.day)
            return dt.replace(day=newday, month=newmonth, year=newyear)
        if incunit == TimeUnit.DAY:
            return dt + datetime.timedelta(days=incval)
        if incunit == TimeUnit.DAYOFWEEK:
            # incval in this case means next day of week whose weekday matches incval (0-6)
            days = (6 + incval - dt.weekday()) % 7 + 1
            newdt = dt + datetime.timedelta(days=days)
            assert newdt.weekday() == incval
            return newdt
        if incunit == TimeUnit.HOUR:
            return dt + datetime.timedelta(hours=incval)
        if incunit == TimeUnit.MINUTE:
            return dt + datetime.timedelta(minutes=incval)
        else:
            assert 0, 'Invalid incunit'  # pragma: no cover

class _Appt:
    '''
    A single entry in the Agenda:  a storm query to run in the future, potentially more than once

    Each such entry has a list of ApptRecs.  Each time the appointment is scheduled, the nexttime of the appointment is
    the lowest nexttime of all its ApptRecs.
    '''

    _synced_attrs = {
        'doc',
        'name',
        'pool',
        'created',
        'enabled',
        'errcount',
        'loglevel',
        'nexttime',
        'lasterrs',
        'isrunning',
        'lastresult',
        'startcount',
        'laststarttime',
        'lastfinishtime',
    }

    def __init__(self, stor, iden, recur, indx, query, creator, recs, nexttime=None, view=None, created=None, pool=False, loglevel=None):
        self.doc = ''
        self.name = ''
        self.task = None
        self.stor = stor
        self.pool = pool
        self.iden = iden
        self.recur = recur  # does this appointment repeat
        self.indx = indx  # incremented for each appt added ever.  Used for nexttime tiebreaking for stable ordering
        self.query = query  # query to run
        self.creator = creator  # user iden to run query as
        self.recs = recs  # List[ApptRec]  list of the individual entries to calculate next time from
        self._recidxnexttime = None  # index of rec who is up next
        self.view = view
        self.created = created
        self.loglevel = loglevel

        if self.recur and not self.recs:
            raise s_exc.BadTime(mesg='A recurrent appointment with no records')

        if nexttime is None and self.recs:
            self.nexttime = self.stor._getNowTick()
            self.updateNexttime(self.nexttime)
            if self.nexttime is None:
                raise s_exc.BadTime(mesg='Appointment is in the past')
        else:
            self.nexttime = nexttime
        self.isrunning = False  # whether it is currently running
        self.startcount = 0  # how many times query has started
        self.errcount = 0  # how many times this appt failed
        self.lasterrs = []
        self.laststarttime = None
        self.lastfinishtime = None
        self.lastresult = None
        self.enabled = True

    def getStorNode(self, form):
        ndef = (form.name, form.type.norm(self.iden)[0])
        buid = s_common.buid(ndef)

        props = {
            'doc': self.doc,
            'name': self.name,
            'storm': self.query,
            '.created': self.created,
        }

        pnorms = {}
        for prop, valu in props.items():
            formprop = form.props.get(prop)
            if formprop is not None and valu is not None:
                pnorms[prop] = formprop.type.norm(valu)[0]

        return (buid, {
            'ndef': ndef,
            'props': pnorms
        })

    def __eq__(self, other):
        ''' For heap logic to sort upcoming events lower '''
        return (self.nexttime, self.indx) == (other.nexttime, other.indx)

    def __lt__(self, other):
        ''' For heap logic '''
        return (self.nexttime, self.indx) < (other.nexttime, other.indx)

    def pack(self):
        return {
            'ver': 1,
            'doc': self.doc,
            'name': self.name,
            'pool': self.pool,
            'enabled': self.enabled,
            'recur': self.recur,
            'iden': self.iden,
            'view': self.view,
            'indx': self.indx,
            'query': self.query,
            'creator': self.creator,
            'created': self.created,
            'recs': [d.pack() for d in self.recs],
            'nexttime': self.nexttime,
            'startcount': self.startcount,
            'errcount': self.errcount,
            'isrunning': self.isrunning,
            'laststarttime': self.laststarttime,
            'lastfinishtime': self.lastfinishtime,
            'lastresult': self.lastresult,
            'lasterrs': list(self.lasterrs[:5])
        }

    @classmethod
    def unpack(cls, stor, val):
        if val['ver'] != 1:
            raise s_exc.BadStorageVersion(mesg=f"Found version {val['ver']}")  # pragma: no cover
        recs = [ApptRec.unpack(tupl) for tupl in val['recs']]
        # TODO: MOAR INSANITY
        loglevel = val.get('loglevel', 'WARNING')
        appt = cls(stor, val['iden'], val['recur'], val['indx'], val['query'], val['creator'], recs,
                   nexttime=val['nexttime'], view=val.get('view'), loglevel=loglevel)
        appt.doc = val.get('doc', '')
        appt.name = val.get('name', '')
        appt.pool = val.get('pool', False)
        appt.created = val.get('created', None)
        appt.laststarttime = val['laststarttime']
        appt.lastfinishtime = val['lastfinishtime']
        appt.lastresult = val['lastresult']
        appt.enabled = val['enabled']
        appt.lasterrs = list(val.get('lasterrs', []))

        return appt

    def updateNexttime(self, now):
        '''
        Find the next time this appointment should be scheduled.

        Delete any nonrecurring record that just happened.
        '''
        if self._recidxnexttime is not None and not self.recur:
            del self.recs[self._recidxnexttime]

        while self.recs and self.nexttime <= now:

            lowtime = 999999999999.9

            # Find the lowest next time of all of our recs (backwards, so we can delete)
            for i in range(len(self.recs) - 1, -1, -1):
                rec = self.recs[i]
                nexttime = rec.nexttime(self.nexttime)
                if nexttime == 0.0:
                    # We blew by and missed a fixed-year appointment, either due to clock shenanigans, this query going
                    # really long, or the initial requirement being in the past
                    logger.warning(f'Missed an appointment: {rec}')
                    del self.recs[i]
                    continue
                if nexttime < lowtime:
                    lowtime = nexttime
                    lowidx = i

            if not self.recs:
                break

            self._recidxnexttime = lowidx
            self.nexttime = lowtime

        if not self.recs:
            self._recidxnexttime = None
            self.nexttime = None

        return self.nexttime

    async def edits(self, edits):
        for name, valu in edits.items():
            if name not in self.__class__._synced_attrs:
                extra = await self.stor.core.getLogExtra(name=name, valu=valu)
                logger.warning('_Appt.edits() Invalid attribute received: %s = %r', name, valu, extra=extra)
                continue

            if name == 'lasterrs' and not isinstance(valu, list):
                valu = list(valu)

            setattr(self, name, valu)

        await self.save()

    async def save(self):
        stordict = self.pack()
        self.stor.apptdefs.set(self.iden, stordict)

class Agenda(s_base.Base):
    '''
    Organize and execute all the scheduled storm queries in a cortex.
    '''

    async def __anit__(self, core):

        await s_base.Base.__anit__(self)

        self.core = core
        self.apptheap = []  # Stores the appointments in a heap such that the first element is the next appt to run
        self.appts = {}  # Dict[bytes: Appt]
        self._next_indx = 0  # index a new appt gets assigned
        self.tickoff = 0  # Used for test overrides

        self._wake_event = s_coro.Event()  # Causes the scheduler loop to wake up
        self.onfini(self._wake_event.set)

        self.apptdefs = self.core.cortexdata.getSubKeyVal('agenda:appt:')

        await self._load_all()

    async def _load_all(self):
        '''
        Load all the appointments from persistent storage
        '''
        # Clear existing appointments before loading
        self.apptheap = []
        self.appts = {}

        to_delete = []
        for iden, info in self.apptdefs.items():
            try:
                appt = _Appt.unpack(self, info)
                if appt.iden != iden:
                    raise s_exc.InconsistentStorage(mesg='iden inconsistency')
                self._addappt(iden, appt)
                self._next_indx = max(self._next_indx, appt.indx + 1)
            except (s_exc.InconsistentStorage, s_exc.BadStorageVersion, s_exc.BadTime, TypeError, KeyError,
                    UnicodeDecodeError) as e:
                logger.warning('Invalid appointment %r found in storage: %r.  Removing.', iden, e)
                to_delete.append(iden)
                continue

        for iden in to_delete:
            self.apptdefs.pop(iden)

        # Make sure we don't assign the same index to 2 appointments
        if self.appts:
            maxindx = max(appt.indx for appt in self.appts.values())
            self._next_indx = maxindx + 1

    def _addappt(self, iden, appt):
        '''
        Updates the data structures to add an appointment
        '''
        if appt.nexttime:
            heapq.heappush(self.apptheap, appt)
        self.appts[iden] = appt
        if self.apptheap and self.apptheap[0] is appt:
            self._wake_event.set()

    @staticmethod
    def _dictproduct(rdict):
        '''
        Yields a series of dicts that cover the combination of all multiple-value (e.g. lists or tuples) values, with
        non-multiple-value values remaining the same.
        '''
        multkeys = [k for k, v in rdict.items() if isinstance(v, Iterable)]
        if not multkeys:
            yield rdict
            return

        multvals = [rdict[k] for k in multkeys]

        for combo in itertools.product(*multvals):
            newdict = rdict.copy()
            for i, k in enumerate(multkeys):
                newdict[k] = combo[i]
            yield newdict

    def list(self):
        return list(self.appts.items())

    async def add(self, cdef):
        '''
        Persistently adds an appointment

        Args:
            cdef (dict):  Dictionary containing the Cron definition.

        Notes:
            The cron definition may contain the following keys:

                creator (str)
                    Iden of the creating user.

                iden (str)
                    Iden of the appointment.

                storm (str)
                    The Storm query to run.

                reqs (Union[None, Dict[TimeUnit, Union[int, Tuple[int]], List[...])
                    One or more dicts of the fixed aspects of the appointment.  dict value may be a single or multiple.
                    May be an empty dict or None.

                incunit (Union[None, TimeUnit])
                    The unit that changes for recurring, or None for non-recurring.  It is an error for this value to
                    match a key in reqdict.

                incvals (Union[None, int, Iterable[int])
                    Count of units of incunit or explicit day of week or day of month.
                    Not allowed for incunit == None, required for others (1 would be a typical value)

            If the values for req and incvals are both lists, all combinations of all values (the product) are used.

        Returns:
            Packed appointment definition
        '''
        iden = cdef['iden']
        incunit = cdef.get('incunit')
        incvals = cdef.get('incvals')
        reqs = cdef.get('reqs', {})
        query = cdef.get('storm')
        creator = cdef.get('creator')
        view = cdef.get('view')
        created = cdef.get('created')
        loglevel = cdef.get('loglevel', 'WARNING')

        pool = cdef.get('pool', False)

        recur = incunit is not None
        indx = self._next_indx
        self._next_indx += 1

        if iden in self.appts:
            mesg = f'Cron job already exists with iden: {iden}'
            raise s_exc.DupIden(iden=iden, mesg=mesg)

        if not query:
            raise ValueError('"query" key of cdef parameter is not present or empty')

        await self.core.getStormQuery(query)

        if not creator:
            raise ValueError('"creator" key is cdef parameter is not present or empty')

        if not reqs and incunit is None:
            raise ValueError('at least one of reqs and incunit must be non-empty')

        if incunit is not None and incvals is None:
            raise ValueError('incvals must be non-None if incunit is non-None')

        if isinstance(reqs, Mapping):
            reqs = [reqs]

        # Find all combinations of values in reqdict values and incvals values
        nexttime = None
        recs = []  # type: ignore
        for req in reqs:
            if TimeUnit.NOW in req:
                if incunit is not None:
                    mesg = "Recurring jobs may not be scheduled to run 'now'"
                    raise ValueError(mesg)
                nexttime = self._getNowTick()
                continue

            reqdicts = self._dictproduct(req)
            if not isinstance(incvals, Iterable):
                incvals = (incvals, )
            recs.extend(ApptRec(rd, incunit, v) for (rd, v) in itertools.product(reqdicts, incvals))

        # TODO: this is insane. Make _Appt take the cdef directly...
        appt = _Appt(self, iden, recur, indx, query, creator, recs, nexttime=nexttime, view=view,
                           created=created, pool=pool, loglevel=loglevel)
        self._addappt(iden, appt)

        appt.doc = cdef.get('doc', '')

        await appt.save()

        return appt.pack()

    async def get(self, iden):

        appt = self.appts.get(iden)
        if appt is not None:
            return appt

        mesg = f'No cron job with iden {iden}'
        raise s_exc.NoSuchIden(iden=iden, mesg=mesg)

    async def enable(self, iden):
        appt = self.appts.get(iden)
        if appt is None:
            mesg = f'No cron job with iden: {iden}'
            raise s_exc.NoSuchIden(iden=iden, mesg=mesg)

        await self.mod(iden, appt.query)

    async def disable(self, iden):
        appt = self.appts.get(iden)
        if appt is None:
            mesg = f'No cron job with iden: {iden}'
            raise s_exc.NoSuchIden(iden=iden, mesg=mesg)

        appt.enabled = False
        await appt.save()

    async def mod(self, iden, query):
        '''
        Change the query of an appointment
        '''
        appt = self.appts.get(iden)
        if appt is None:
            mesg = f'No cron job with iden: {iden}'
            raise s_exc.NoSuchIden(iden=iden, mesg=mesg)

        if not query:
            raise ValueError('empty query')

        await self.core.getStormQuery(query)

        appt.query = query
        appt.enabled = True  # in case it was disabled for a bad query

        await appt.save()

    async def move(self, croniden, viewiden):
        '''
        Move a cronjob from one view to another
        '''
        appt = self.appts.get(croniden)
        if appt is None:
            mesg = f'No cron job with iden: {croniden}'
            raise s_exc.NoSuchIden(iden=croniden, mesg=mesg)

        appt.view = viewiden

        await appt.save()

    async def delete(self, iden):
        '''
        Delete an appointment
        '''
        appt = self.appts.get(iden)
        if appt is None:
            mesg = f'No cron job with iden: {iden}'
            raise s_exc.NoSuchIden(iden=iden, mesg=mesg)

        self._delete_appt_from_heap(appt)
        del self.appts[iden]
        self.apptdefs.delete(iden)

    def _delete_appt_from_heap(self, appt):
        try:
            heappos = self.apptheap.index(appt)
        except ValueError:
            pass  # this is OK, just a non-recurring appt that has no more records
        else:
            # If we're already the last item, just delete it
            if heappos == len(self.apptheap) - 1:
                del self.apptheap[heappos]
            else:
                # put the last item at the current position and reheap
                self.apptheap[heappos] = self.apptheap.pop()
                heapq.heapify(self.apptheap)

    def _getNowTick(self):
        return time.time() + self.tickoff

    def _addTickOff(self, offs):
        self.tickoff += offs
        self._wake_event.set()

    async def clearRunningStatus(self):
        '''Used for clearing the running state at startup or change of leadership.'''
        for appt in list(self.appts.values()):
            if appt.isrunning:
                logger.debug(f'Clearing the isrunning flag for {appt.iden}')

                edits = {
                    'isrunning': False,
                    'lastfinishtime': self._getNowTick(),
                    'lasterrs': ['aborted'] + appt.lasterrs[-4:]
                }
                await self.core.addCronEdits(appt.iden, edits)
                await self.core.feedBeholder('cron:stop', {'iden': appt.iden})

                if appt.nexttime is None:
                    self._delete_appt_from_heap(appt)

    async def runloop(self):
        '''
        Task loop to issue query tasks at the right times.
        '''
        await self.clearRunningStatus()
        while not self.isfini:

            timeout = None
            if self.apptheap:
                timeout = self.apptheap[0].nexttime - self._getNowTick()

            if timeout is None or timeout > 0:
                self._wake_event.clear()
                await self._wake_event.timewait(timeout=timeout)

            if self.isfini:
                return

            now = self._getNowTick()
            while self.apptheap and self.apptheap[0].nexttime <= now:

                appt = heapq.heappop(self.apptheap)
                nexttime = appt.updateNexttime(now)
                edits = {
                    'nexttime': nexttime,
                }
                await self.core.addCronEdits(appt.iden, edits)

                if appt.nexttime:
                    heapq.heappush(self.apptheap, appt)

                if not appt.enabled:
                    continue

                if appt.isrunning:  # pragma: no cover
                    mesg = f'Appointment {appt.iden} {appt.name} is still running from previous time when scheduled' \
                           f' to run. Skipping.'
                    logger.warning(mesg,
                                   extra={'synapse': {'iden': appt.iden, 'name': appt.name}})
                else:
                    try:
                        await self._execute(appt)
                    except Exception as e:
                        extra = {'iden': appt.iden, 'name': appt.name, 'user': appt.creator, 'view': appt.view}
                        user = self.core.auth.user(appt.creator)
                        if user is not None:
                            extra['username'] = user.name
                        if isinstance(e, s_exc.SynErr):
                            mesg = e.get('mesg', str(e))
                        else:  # pragma: no cover
                            mesg = str(e)
                        logger.exception(f'Agenda error running appointment {appt.iden} {appt.name}: {mesg}',
                                         extra={'synapse': extra})
                        await self._markfailed(appt, f'error: {e}')

    async def _execute(self, appt):
        '''
        Fire off the task to make the storm query
        '''
        user = self.core.auth.user(appt.creator)
        if user is None:
            logger.warning(f'Unknown user {appt.creator} in stored appointment {appt.iden} {appt.name}',
                           extra={'synapse': {'iden': appt.iden, 'name': appt.name, 'user': appt.creator}})
            await self._markfailed(appt, 'unknown user')
            return

        locked = user.info.get('locked')
        if locked:
            logger.warning(f'Cron {appt.iden} {appt.name} failed because creator {user.name} is locked',
                           extra={'synapse': {'iden': appt.iden, 'name': appt.name, 'user': appt.creator,
                                              'username': user.name}})
            await self._markfailed(appt, 'locked user')
            return

        view = self.core.getView(iden=appt.view, user=user)
        if view is None:
            logger.warning(f'Unknown view {appt.view} in stored appointment {appt.iden} {appt.name}',
                           extra={'synapse': {'iden': appt.iden, 'name': appt.name, 'user': appt.creator,
                                              'username': user.name, 'view': appt.view}})
            await self._markfailed(appt, 'unknown view')
            return

        info = {'iden': appt.iden, 'query': appt.query, 'view': view.iden}

        coro = self._runJob(user, appt)
        task = self.core.runActiveTask(coro)

        appt.task = await self.core.boss.promotetask(task, f'Cron {appt.iden}', user, info=info)
        async def fini():
            appt.task = None

        appt.task.onfini(fini)

    async def _markfailed(self, appt, reason):
        now = self._getNowTick()
        edits = {
            'laststarttime': now,
            'lastfinishtime': now,
            'startcount': appt.startcount + 1,
            'isrunning': False,
            'lastresult': f'Failed due to {reason}',
        }
        await self.core.addCronEdits(appt.iden, edits)

    async def _runJob(self, user, appt):
        '''
        Actually run the storm query, updating the appropriate statistics and results
        '''
        count = 0
        edits = {
            'isrunning': True,
            'laststarttime': self._getNowTick(),
            'startcount': appt.startcount + 1,
        }
        await self.core.addCronEdits(appt.iden, edits)

        logger.info(f'Agenda executing for iden={appt.iden}, name={appt.name} user={user.name}, view={appt.view}, query={appt.query}',
                    extra={'synapse': {'iden': appt.iden, 'name': appt.name, 'user': user.iden, 'text': appt.query,
                                       'username': user.name, 'view': appt.view}})
        starttime = self._getNowTick()

        success = False
        loglevel = s_common.normLogLevel(appt.loglevel)

        try:
            opts = {
                'user': user.iden,
                'view': appt.view,
                'mirror': appt.pool,
                'vars': {'auto': {'iden': appt.iden, 'type': 'cron'}},
                '_loginfo': {
                    'cron': appt.iden
                }
            }
            opts = self.core._initStormOpts(opts)

            await self.core.feedBeholder('cron:start', {'iden': appt.iden})

            async for mesg in self.core.storm(appt.query, opts=opts):

                if mesg[0] == 'node':
                    count += 1

                elif mesg[0] == 'warn' and loglevel <= logging.WARNING:
                    text = mesg[1].get('mesg', '<missing message>')
                    extra = await self.core.getLogExtra(cron=appt.iden, **mesg[1])
                    logger.warning(f'Cron job {appt.iden} issued warning: {text}', extra=extra)

                elif mesg[0] == 'err':
                    excname, errinfo = mesg[1]
                    errinfo.pop('eline', None)
                    errinfo.pop('efile', None)
                    excctor = getattr(s_exc, excname, s_exc.SynErr)
                    raise excctor(**errinfo)

        except asyncio.CancelledError:
            result = 'cancelled'
            raise

        except Exception as e:
            result = f'raised exception {e}'
            logger.exception(f'Agenda job {appt.iden} {appt.name} raised exception',
                             extra={'synapse': {'iden': appt.iden, 'name': appt.name}}
                             )
        else:
            success = True
            result = f'finished successfully with {count} nodes'

        finally:
            finishtime = self._getNowTick()
            if not success:
                appt.lasterrs.append(result)
                edits = {
                    'errcount': appt.errcount + 1,
                    # we only care about the last five errors
                    'lasterrs': list(appt.lasterrs[-5:]),
                }

                if self.core.isactive:
                    await self.core.addCronEdits(appt.iden, edits)

            took = finishtime - starttime
            mesg = f'Agenda completed query for iden={appt.iden} name={appt.name} with result "{result}" ' \
                   f'took {took:.3f}s'
            if not self.core.isactive:
                mesg = mesg + ' Agenda status will not be saved since the Cortex is no longer the leader.'
            logger.info(mesg, extra={'synapse': {'iden': appt.iden, 'name': appt.name, 'user': user.iden,
                                                 'result': result, 'username': user.name, 'took': took}})
            edits = {
                'lastfinishtime': finishtime,
                'isrunning': False,
                'lastresult': result,
            }
            if self.core.isactive:
                await self.core.addCronEdits(appt.iden, edits)

            if not self.isfini:
                # fire beholder event before invoking nexus change (in case readonly)
                await self.core.feedBeholder('cron:stop', {'iden': appt.iden})
