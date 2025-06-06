use core::ffi::{c_int, c_void, CStr};
use core::ptr::null_mut as NULL;
use pyo3_ffi::*;

use crate::common::math::*;
use crate::common::*;
use crate::docstrings as doc;
use crate::{
    date::Date,
    date_delta::DateDelta,
    datetime_delta::set_units_from_kwargs,
    datetime_delta::DateTimeDelta,
    instant::Instant,
    offset_datetime::{
        self, instant, local, timestamp, timestamp_millis, timestamp_nanos, to_instant, to_plain,
        OffsetDateTime,
    },
    plain_datetime::{set_components_from_kwargs, DateTime},
    round,
    time::Time,
    time_delta::TimeDelta,
    zoned_datetime::ZonedDateTime,
    State,
};

pub(crate) const SINGLETONS: &[(&CStr, OffsetDateTime); 0] = &[];

impl OffsetDateTime {
    pub(crate) unsafe fn resolve_system_tz(
        py_api: &PyDateTime_CAPI,
        date: Date,
        time: Time,
        dis: Option<Disambiguate>,
        preferred_offset: Offset,
        exc_repeated: *mut PyObject,
        exc_skipped: *mut PyObject,
    ) -> PyResult<Self> {
        match dis {
            Some(dis) => Self::resolve_system_tz_using_disambiguate(
                py_api,
                date,
                time,
                dis,
                exc_repeated,
                exc_skipped,
            ),
            None => Self::resolve_system_tz_using_offset(py_api, date, time, preferred_offset),
        }
    }

    pub(crate) unsafe fn resolve_system_tz_using_disambiguate(
        py_api: &PyDateTime_CAPI,
        date: Date,
        time: Time,
        dis: Disambiguate,
        exc_repeated: *mut PyObject,
        exc_skipped: *mut PyObject,
    ) -> PyResult<Self> {
        use Ambiguity::*;
        Ok(match offset_for_system_tz(py_api, date, time)? {
            Unambiguous(offset) => OffsetDateTime::new_unchecked(date, time, offset),
            Fold(offset0, offset1) => {
                let offset = match dis {
                    Disambiguate::Compatible | Disambiguate::Earlier => offset0,
                    Disambiguate::Later => offset1,
                    Disambiguate::Raise => raise(
                        exc_repeated,
                        format!("{} {} is repeated in the system timezone", date, time),
                    )?,
                };
                OffsetDateTime::new_unchecked(date, time, offset)
            }
            Gap(offset0, offset1) => {
                let (offset, shift) = match dis {
                    Disambiguate::Compatible | Disambiguate::Later => {
                        (offset1, offset1.sub(offset0))
                    }
                    Disambiguate::Earlier => (offset0, offset0.sub(offset1)),
                    Disambiguate::Raise => raise(
                        exc_skipped,
                        format!("{} {} is skipped in the system timezone", date, time),
                    )?,
                };
                DateTime { date, time }
                    .change_offset(shift)
                    .ok_or_value_err("Resulting date is out of range")?
                    .with_offset_unchecked(offset)
            }
        })
    }

    unsafe fn resolve_system_tz_using_offset(
        py_api: &PyDateTime_CAPI,
        date: Date,
        time: Time,
        target: Offset,
    ) -> PyResult<Self> {
        use Ambiguity::*;
        match offset_for_system_tz(py_api, date, time)? {
            Unambiguous(offset) => OffsetDateTime::new(date, time, offset),
            Fold(offset0, offset1) => OffsetDateTime::new(
                date,
                time,
                if target == offset1 { offset1 } else { offset0 },
            ),
            Gap(offset0, offset1) => {
                let (offset, shift) = if target == offset0 {
                    (offset0, offset0.sub(offset1))
                } else {
                    (offset1, offset1.sub(offset0))
                };
                DateTime { date, time }
                    .change_offset(shift)
                    .ok_or_value_err("Resulting date is out of range")?
                    .with_offset(offset)
            }
        }
        .ok_or_value_err("Resulting datetime is out of range")
    }

    pub(crate) unsafe fn to_system_tz(self, py_api: &PyDateTime_CAPI) -> PyResult<Self> {
        let dt_original = self.to_py(py_api)?;
        defer_decref!(dt_original);
        // FUTURE: define `astimezone` string once, then reuse it?
        let dt_new = methcall0(dt_original, "astimezone")?;
        defer_decref!(dt_new);
        Ok(OffsetDateTime::new_unchecked(
            Date::from_py_unchecked(dt_new),
            Time {
                hour: PyDateTime_DATE_GET_HOUR(dt_new) as u8,
                minute: PyDateTime_DATE_GET_MINUTE(dt_new) as u8,
                second: PyDateTime_DATE_GET_SECOND(dt_new) as u8,
                subsec: self.time.subsec,
            },
            offset_from_py_dt(dt_new)?,
        ))
    }

    #[allow(clippy::too_many_arguments)]
    unsafe fn shift_in_system_tz(
        self,
        py_api: &PyDateTime_CAPI,
        months: DeltaMonths,
        days: DeltaDays,
        delta: TimeDelta,
        dis: Option<Disambiguate>,
        exc_repeated: *mut PyObject,
        exc_skipped: *mut PyObject,
    ) -> PyResult<Self> {
        let slf = if !months.is_zero() || !days.is_zero() {
            Self::resolve_system_tz(
                py_api,
                self.date
                    .shift(months, days)
                    .ok_or_value_err("Resulting date is out of range")?,
                self.time,
                dis,
                self.offset,
                exc_repeated,
                exc_skipped,
            )?
        } else {
            self
        };
        slf.instant()
            .shift(delta)
            .ok_or_value_err("Result is out of range")?
            .to_system_tz(py_api)
    }
}

unsafe fn offset_for_system_tz(
    py_api: &PyDateTime_CAPI,
    date: Date,
    time: Time,
) -> PyResult<Ambiguity> {
    let (offset0, shifted) = system_offset(date, time, 0, py_api)?;
    let (offset1, _) = system_offset(date, time, 1, py_api)?;

    Ok(if offset0 == offset1 {
        Ambiguity::Unambiguous(offset0)
    } else if shifted {
        // Before Python 3.12, the fold of system times was erroneously reversed
        // in case of gaps. See cpython/issues/83861
        #[cfg(Py_3_12)]
        {
            Ambiguity::Gap(offset1, offset0)
        }
        #[cfg(not(Py_3_12))]
        {
            Ambiguity::Gap(offset0, offset1)
        }
    } else {
        Ambiguity::Fold(offset0, offset1)
    })
}

unsafe fn system_offset(
    date: Date,
    time: Time,
    fold: i32,
    &PyDateTime_CAPI {
        DateTime_FromDateAndTimeAndFold,
        DateTime_FromDateAndTime,
        DateTimeType,
        ..
    }: &PyDateTime_CAPI,
) -> PyResult<(Offset, bool)> {
    // OPTIMIZE: re-use Python string objects
    let naive = DateTime_FromDateAndTimeAndFold(
        date.year.get().into(),
        date.month.get().into(),
        date.day.into(),
        time.hour.into(),
        time.minute.into(),
        time.second.into(),
        0, // assume no sub-second system offsets
        Py_None(),
        fold,
        DateTimeType,
    )
    .as_result()?;
    defer_decref!(naive);
    let aware = methcall0(naive, "astimezone")?;
    defer_decref!(aware);
    let shifted_naive = DateTime_FromDateAndTime(
        PyDateTime_GET_YEAR(aware),
        PyDateTime_GET_MONTH(aware),
        PyDateTime_GET_DAY(aware),
        PyDateTime_DATE_GET_HOUR(aware),
        PyDateTime_DATE_GET_MINUTE(aware),
        PyDateTime_DATE_GET_SECOND(aware),
        0,
        Py_None(),
        DateTimeType,
    );
    defer_decref!(shifted_naive);
    let shifted = match PyObject_RichCompareBool(naive, shifted_naive, Py_EQ) {
        1 => false,
        0 => true,
        _ => Err(PyErrOccurred())?,
    };
    Ok((offset_from_py_dt(aware)?, shifted))
}

impl Instant {
    #[inline]
    pub(crate) unsafe fn to_system_tz(self, py_api: &PyDateTime_CAPI) -> PyResult<OffsetDateTime> {
        let dt_utc = self.to_py(py_api)?;
        defer_decref!(dt_utc);
        let dt_new = methcall0(dt_utc, "astimezone")?;
        defer_decref!(dt_new);
        Ok(OffsetDateTime::new_unchecked(
            Date::from_py_unchecked(dt_new),
            Time {
                hour: PyDateTime_DATE_GET_HOUR(dt_new) as u8,
                minute: PyDateTime_DATE_GET_MINUTE(dt_new) as u8,
                second: PyDateTime_DATE_GET_SECOND(dt_new) as u8,
                subsec: self.subsec,
            },
            offset_from_py_dt(dt_new)?,
        ))
    }
}

unsafe fn __new__(cls: *mut PyTypeObject, args: *mut PyObject, kwargs: *mut PyObject) -> PyReturn {
    let &State {
        py_api,
        exc_repeated,
        exc_skipped,
        str_compatible,
        str_raise,
        str_earlier,
        str_later,
        ..
    } = State::for_type(cls);
    let mut year = 0;
    let mut month = 0;
    let mut day = 0;
    let mut hour = 0;
    let mut minute = 0;
    let mut second = 0;
    let mut nanosecond = 0;
    let mut disambiguate: *mut PyObject = str_compatible;

    parse_args_kwargs!(
        args,
        kwargs,
        c"lll|lll$lU:SystemDateTime",
        year,
        month,
        day,
        hour,
        minute,
        second,
        nanosecond,
        disambiguate
    );

    let date = Date::from_longs(year, month, day).ok_or_value_err("Invalid date")?;
    let time =
        Time::from_longs(hour, minute, second, nanosecond).ok_or_value_err("Invalid time")?;
    let dis = Disambiguate::from_py(
        disambiguate,
        str_compatible,
        str_raise,
        str_earlier,
        str_later,
    )?;
    OffsetDateTime::resolve_system_tz_using_disambiguate(
        py_api,
        date,
        time,
        dis,
        exc_repeated,
        exc_skipped,
    )?
    .to_obj(cls)
}

unsafe fn __repr__(slf: *mut PyObject) -> PyReturn {
    let OffsetDateTime { date, time, offset } = OffsetDateTime::extract(slf);
    format!("SystemDateTime({} {}{})", date, time, offset).to_py()
}

unsafe fn __str__(slf: *mut PyObject) -> PyReturn {
    format!("{}", OffsetDateTime::extract(slf)).to_py()
}

unsafe fn __richcmp__(a_obj: *mut PyObject, b_obj: *mut PyObject, op: c_int) -> PyReturn {
    let type_a = Py_TYPE(a_obj);
    let type_b = Py_TYPE(b_obj);
    let inst_a = OffsetDateTime::extract(a_obj).instant();
    let inst_b = if type_b == type_a {
        OffsetDateTime::extract(b_obj).instant()
    } else if type_b == State::for_type(type_a).instant_type {
        Instant::extract(b_obj)
    } else if type_b == State::for_type(type_a).zoned_datetime_type {
        ZonedDateTime::extract(b_obj).instant()
    } else if type_b == State::for_type(type_a).offset_datetime_type {
        OffsetDateTime::extract(b_obj).instant()
    } else {
        return Ok(newref(Py_NotImplemented()));
    };
    match op {
        pyo3_ffi::Py_EQ => inst_a == inst_b,
        pyo3_ffi::Py_NE => inst_a != inst_b,
        pyo3_ffi::Py_LT => inst_a < inst_b,
        pyo3_ffi::Py_LE => inst_a <= inst_b,
        pyo3_ffi::Py_GT => inst_a > inst_b,
        pyo3_ffi::Py_GE => inst_a >= inst_b,
        _ => unreachable!(),
    }
    .to_py()
}

#[inline]
unsafe fn _shift_operator(obj_a: *mut PyObject, obj_b: *mut PyObject, negate: bool) -> PyReturn {
    debug_assert_eq!(
        PyType_GetModule(Py_TYPE(obj_a)),
        PyType_GetModule(Py_TYPE(obj_b))
    );
    let type_a = Py_TYPE(obj_a);
    let type_b = Py_TYPE(obj_b);
    let &State {
        time_delta_type,
        date_delta_type,
        datetime_delta_type,
        py_api,
        exc_repeated,
        exc_skipped,
        ..
    } = State::for_type(type_a);

    let odt = OffsetDateTime::extract(obj_a);
    let mut months = DeltaMonths::ZERO;
    let mut days = DeltaDays::ZERO;
    let mut tdelta = TimeDelta::ZERO;

    if type_b == time_delta_type {
        tdelta = TimeDelta::extract(obj_b);
    } else if type_b == date_delta_type {
        let dd = DateDelta::extract(obj_b);
        months = dd.months;
        days = dd.days;
    } else if type_b == datetime_delta_type {
        let dtd = DateTimeDelta::extract(obj_b);
        months = dtd.ddelta.months;
        days = dtd.ddelta.days;
        tdelta = dtd.tdelta;
    } else {
        return Ok(newref(Py_NotImplemented()));
    };
    if negate {
        months = -months;
        days = -days;
        tdelta = -tdelta;
    };

    odt.shift_in_system_tz(
        py_api,
        months,
        days,
        tdelta,
        None,
        exc_repeated,
        exc_skipped,
    )?
    .to_obj(type_a)
}

unsafe fn __add__(obj_a: *mut PyObject, obj_b: *mut PyObject) -> PyReturn {
    if PyType_GetModule(Py_TYPE(obj_a)) == PyType_GetModule(Py_TYPE(obj_b)) {
        _shift_operator(obj_a, obj_b, false)
    } else {
        Ok(newref(Py_NotImplemented()))
    }
}

unsafe fn __sub__(obj_a: *mut PyObject, obj_b: *mut PyObject) -> PyReturn {
    let type_a = Py_TYPE(obj_a);
    let type_b = Py_TYPE(obj_b);

    // Easy case: systemDT - systemDT
    let (inst_a, inst_b) = if type_a == type_b {
        (
            OffsetDateTime::extract(obj_a).instant(),
            OffsetDateTime::extract(obj_b).instant(),
        )
    // Other cases are more difficult, as they can be triggered
    // by reflexive operations with arbitrary types.
    // We need to eliminate them carefully.
    } else {
        let mod_a = PyType_GetModule(type_a);
        let mod_b = PyType_GetModule(type_b);
        if mod_a == mod_b {
            let inst_b = if type_b == State::for_mod(mod_a).instant_type {
                Instant::extract(obj_b)
            } else if type_b == State::for_mod(mod_a).zoned_datetime_type {
                ZonedDateTime::extract(obj_b).instant()
            } else if type_b == State::for_mod(mod_a).offset_datetime_type {
                OffsetDateTime::extract(obj_b).instant()
            } else {
                return _shift_operator(obj_a, obj_b, true);
            };
            debug_assert_eq!(type_a, State::for_type(type_a).system_datetime_type);
            (OffsetDateTime::extract(obj_a).instant(), inst_b)
        } else {
            return Ok(newref(Py_NotImplemented()));
        }
    };
    inst_a
        .diff(inst_b)
        .to_obj(State::for_type(type_a).time_delta_type)
}

#[allow(static_mut_refs)]
static mut SLOTS: &[PyType_Slot] = &[
    slotmethod!(Py_tp_new, __new__),
    slotmethod!(Py_tp_str, __str__, 1),
    slotmethod!(Py_tp_repr, __repr__, 1),
    slotmethod!(Py_tp_richcompare, __richcmp__),
    slotmethod!(Py_nb_add, __add__, 2),
    slotmethod!(Py_nb_subtract, __sub__, 2),
    PyType_Slot {
        slot: Py_tp_doc,
        pfunc: doc::SYSTEMDATETIME.as_ptr() as *mut c_void,
    },
    PyType_Slot {
        slot: Py_tp_hash,
        pfunc: offset_datetime::__hash__ as *mut c_void,
    },
    PyType_Slot {
        slot: Py_tp_methods,
        pfunc: unsafe { METHODS.as_ptr() as *mut c_void },
    },
    PyType_Slot {
        slot: Py_tp_getset,
        pfunc: unsafe { GETSETTERS.as_ptr() as *mut c_void },
    },
    PyType_Slot {
        slot: Py_tp_dealloc,
        pfunc: generic_dealloc as *mut c_void,
    },
    PyType_Slot {
        slot: 0,
        pfunc: NULL(),
    },
];

unsafe fn exact_eq(obj_a: *mut PyObject, obj_b: *mut PyObject) -> PyReturn {
    if Py_TYPE(obj_a) == Py_TYPE(obj_b) {
        Ok(newref(
            (OffsetDateTime::extract(obj_a) == OffsetDateTime::extract(obj_b)).to_py()?,
        ))
    } else {
        raise_type_err(format!("Argument must be same type, got {}", obj_b.repr()))
    }
}

pub(crate) unsafe fn unpickle(module: *mut PyObject, arg: *mut PyObject) -> PyReturn {
    let mut packed = arg.to_bytes()?.ok_or_type_err("Invalid pickle data")?;
    if packed.len() != 15 {
        raise_value_err("Invalid pickle data")?
    }
    OffsetDateTime::new_unchecked(
        Date {
            year: Year::new_unchecked(unpack_one!(packed, u16)),
            month: Month::new_unchecked(unpack_one!(packed, u8)),
            day: unpack_one!(packed, u8),
        },
        Time {
            hour: unpack_one!(packed, u8),
            minute: unpack_one!(packed, u8),
            second: unpack_one!(packed, u8),
            subsec: SubSecNanos::new_unchecked(unpack_one!(packed, i32)),
        },
        Offset::new_unchecked(unpack_one!(packed, i32)),
    )
    .to_obj(State::for_mod(module).system_datetime_type)
}

unsafe fn py_datetime(slf: *mut PyObject, _: *mut PyObject) -> PyReturn {
    OffsetDateTime::extract(slf).to_py(State::for_obj(slf).py_api)
}

unsafe fn date(slf: *mut PyObject, _: *mut PyObject) -> PyReturn {
    OffsetDateTime::extract(slf)
        .date
        .to_obj(State::for_obj(slf).date_type)
}

unsafe fn time(slf: *mut PyObject, _: *mut PyObject) -> PyReturn {
    OffsetDateTime::extract(slf)
        .time
        .to_obj(State::for_obj(slf).time_type)
}

unsafe fn replace_date(
    slf: *mut PyObject,
    cls: *mut PyTypeObject,
    args: &[*mut PyObject],
    kwargs: &mut KwargIter,
) -> PyReturn {
    let &State {
        date_type,
        py_api,
        str_disambiguate,
        exc_skipped,
        exc_repeated,
        str_compatible,
        str_raise,
        str_earlier,
        str_later,
        ..
    } = State::for_obj(slf);

    let &[arg] = args else {
        raise_type_err(format!(
            "replace_date() takes 1 positional argument but {} were given",
            args.len()
        ))?
    };

    if Py_TYPE(arg) == date_type {
        let OffsetDateTime { time, offset, .. } = OffsetDateTime::extract(slf);
        OffsetDateTime::resolve_system_tz(
            py_api,
            Date::extract(arg),
            time,
            Disambiguate::from_only_kwarg(
                kwargs,
                str_disambiguate,
                "replace_date",
                str_compatible,
                str_raise,
                str_earlier,
                str_later,
            )?,
            offset,
            exc_repeated,
            exc_skipped,
        )?
        .to_obj(cls)
    } else {
        raise_type_err("date must be a Date instance")
    }
}

unsafe fn replace_time(
    slf: *mut PyObject,
    cls: *mut PyTypeObject,
    args: &[*mut PyObject],
    kwargs: &mut KwargIter,
) -> PyReturn {
    let &State {
        time_type,
        py_api,
        str_disambiguate,
        exc_skipped,
        exc_repeated,
        str_compatible,
        str_raise,
        str_earlier,
        str_later,
        ..
    } = State::for_obj(slf);

    let &[arg] = args else {
        raise_type_err(format!(
            "replace_time() takes 1 positional argument but {} were given",
            args.len()
        ))?
    };

    if Py_TYPE(arg) == time_type {
        let OffsetDateTime { date, offset, .. } = OffsetDateTime::extract(slf);
        OffsetDateTime::resolve_system_tz(
            py_api,
            date,
            Time::extract(arg),
            Disambiguate::from_only_kwarg(
                kwargs,
                str_disambiguate,
                "replace_time",
                str_compatible,
                str_raise,
                str_earlier,
                str_later,
            )?,
            offset,
            exc_repeated,
            exc_skipped,
        )?
        .to_obj(cls)
    } else {
        raise_type_err("time must be a Time instance")
    }
}

unsafe fn format_common_iso(slf: *mut PyObject, _: *mut PyObject) -> PyReturn {
    __str__(slf)
}

unsafe fn replace(
    slf: *mut PyObject,
    cls: *mut PyTypeObject,
    args: &[*mut PyObject],
    kwargs: &mut KwargIter,
) -> PyReturn {
    if !args.is_empty() {
        raise_type_err("replace() takes no positional arguments")?
    }
    let &State {
        str_disambiguate,
        exc_repeated,
        exc_skipped,
        str_year,
        str_month,
        str_day,
        str_hour,
        str_minute,
        str_second,
        str_nanosecond,
        str_compatible,
        str_raise,
        str_earlier,
        str_later,
        py_api,
        ..
    } = State::for_type(cls);
    let OffsetDateTime { date, time, offset } = OffsetDateTime::extract(slf);
    let mut year = date.year.get().into();
    let mut month = date.month.get().into();
    let mut day = date.day.into();
    let mut hour = time.hour.into();
    let mut minute = time.minute.into();
    let mut second = time.second.into();
    let mut nanos = time.subsec.get() as _;
    let mut dis = None;

    handle_kwargs("replace", kwargs, |key, value, eq| {
        if eq(key, str_disambiguate) {
            dis = Some(Disambiguate::from_py(
                value,
                str_compatible,
                str_raise,
                str_earlier,
                str_later,
            )?);
            Ok(true)
        } else {
            set_components_from_kwargs(
                key,
                value,
                &mut year,
                &mut month,
                &mut day,
                &mut hour,
                &mut minute,
                &mut second,
                &mut nanos,
                str_year,
                str_month,
                str_day,
                str_hour,
                str_minute,
                str_second,
                str_nanosecond,
                eq,
            )
        }
    })?;

    let date = Date::from_longs(year, month, day).ok_or_value_err("Invalid date")?;
    let time = Time::from_longs(hour, minute, second, nanos).ok_or_value_err("Invalid time")?;
    OffsetDateTime::resolve_system_tz(py_api, date, time, dis, offset, exc_repeated, exc_skipped)?
        .to_obj(cls)
}

unsafe fn now(cls: *mut PyObject, _: *mut PyObject) -> PyReturn {
    let state = State::for_type(cls.cast());
    let instant = state.time_ns()?;
    let utc_dt = instant.to_py(state.py_api)?;
    defer_decref!(utc_dt);
    let dt = methcall0(utc_dt, "astimezone")?;
    defer_decref!(dt);
    OffsetDateTime::from_py_and_nanos_unchecked(dt, instant.subsec)?.to_obj(cls.cast())
}

unsafe fn from_py_datetime(cls: *mut PyObject, dt: *mut PyObject) -> PyReturn {
    if PyDateTime_Check(dt) == 0 {
        raise_type_err("Argument must be a datetime.datetime instance")?
    }
    OffsetDateTime::from_py(dt, State::for_type(cls.cast()))?
        .ok_or_else_value_err(|| {
            format!(
                "Argument must have a `datetime.timezone` tzinfo and be within range, got {}",
                dt.repr()
            )
        })?
        .to_obj(cls.cast())
}

unsafe fn __reduce__(slf: *mut PyObject, _: *mut PyObject) -> PyReturn {
    let OffsetDateTime {
        date: Date { year, month, day },
        time:
            Time {
                hour,
                minute,
                second,
                subsec,
                ..
            },
        offset,
    } = OffsetDateTime::extract(slf);
    let data = pack![
        year.get(),
        month.get(),
        day,
        hour,
        minute,
        second,
        subsec.get(),
        offset.get()
    ];
    (
        State::for_obj(slf).unpickle_system_datetime,
        steal!((steal!(data.to_py()?),).to_py()?),
    )
        .to_py()
}

unsafe fn from_timestamp(cls: *mut PyObject, arg: *mut PyObject) -> PyReturn {
    match arg.to_i64()? {
        Some(ts) => Instant::from_timestamp(ts),
        None => Instant::from_timestamp_f64(
            arg.to_f64()?
                .ok_or_type_err("Timestamp must be an integer or float")?,
        ),
    }
    .ok_or_value_err("timestamp is out of range")
    .and_then(|inst| inst.to_system_tz(State::for_type(cls.cast()).py_api))?
    .to_obj(cls.cast())
}

unsafe fn from_timestamp_millis(cls: *mut PyObject, arg: *mut PyObject) -> PyReturn {
    Instant::from_timestamp_millis(
        arg.to_i64()?
            .ok_or_type_err("timestamp must be an integer")?,
    )
    .ok_or_value_err("timestamp is out of range")
    .and_then(|inst| inst.to_system_tz(State::for_type(cls.cast()).py_api))?
    .to_obj(cls.cast())
}

unsafe fn from_timestamp_nanos(cls: *mut PyObject, arg: *mut PyObject) -> PyReturn {
    Instant::from_timestamp_nanos(
        arg.to_i128()?
            .ok_or_type_err("timestamp must be an integer")?,
    )
    .ok_or_value_err("timestamp is out of range")
    .and_then(|inst| inst.to_system_tz(State::for_type(cls.cast()).py_api))?
    .to_obj(cls.cast())
}

unsafe fn parse_common_iso(cls: *mut PyObject, s_obj: *mut PyObject) -> PyReturn {
    OffsetDateTime::parse(
        s_obj
            .to_utf8()?
            .ok_or_type_err("argument must be a string")?,
    )
    .ok_or_else_value_err(|| format!("Invalid format: {}", s_obj.repr()))?
    .to_obj(cls.cast())
}

unsafe fn to_fixed_offset(slf_obj: *mut PyObject, args: &[*mut PyObject]) -> PyReturn {
    let slf = OffsetDateTime::extract(slf_obj);
    match *args {
        [] => {
            let &State {
                offset_datetime_type,
                ..
            } = State::for_obj(slf_obj);
            slf.to_obj(offset_datetime_type)
        }
        [arg] => {
            let &State {
                offset_datetime_type,
                time_delta_type,
                ..
            } = State::for_obj(slf_obj);
            let offset = offset_datetime::extract_offset(arg, time_delta_type)?;
            slf.instant()
                .to_offset(offset)
                .ok_or_value_err("Resulting local date out of range")?
                .to_obj(offset_datetime_type)
        }
        _ => raise_type_err("to_fixed_offset() takes at most 1 argument"),
    }
}

unsafe fn to_tz(slf: *mut PyObject, tz_obj: *mut PyObject) -> PyReturn {
    let &mut State {
        zoned_datetime_type,
        exc_tz_notfound,
        ref mut tz_cache,
        ..
    } = State::for_obj_mut(slf);
    let tz = tz_cache.obj_get(tz_obj, exc_tz_notfound)?;
    OffsetDateTime::extract(slf)
        .instant()
        .to_tz(tz)
        .ok_or_value_err("Resulting datetime is out of range")?
        .to_obj(zoned_datetime_type)
}

unsafe fn to_system_tz(slf: *mut PyObject, _: *mut PyObject) -> PyReturn {
    let cls = Py_TYPE(slf);
    OffsetDateTime::extract(slf)
        .to_system_tz(State::for_type(cls).py_api)?
        .to_obj(cls)
}

unsafe fn add(
    slf: *mut PyObject,
    cls: *mut PyTypeObject,
    args: &[*mut PyObject],
    kwargs: &mut KwargIter,
) -> PyReturn {
    _shift_method(slf, cls, args, kwargs, false)
}

unsafe fn subtract(
    slf: *mut PyObject,
    cls: *mut PyTypeObject,
    args: &[*mut PyObject],
    kwargs: &mut KwargIter,
) -> PyReturn {
    _shift_method(slf, cls, args, kwargs, true)
}

#[inline]
unsafe fn _shift_method(
    slf: *mut PyObject,
    cls: *mut PyTypeObject,
    args: &[*mut PyObject],
    kwargs: &mut KwargIter,
    negate: bool,
) -> PyReturn {
    let fname = if negate { "subtract" } else { "add" };
    let state = State::for_type(cls);
    let &State {
        str_disambiguate,
        time_delta_type,
        date_delta_type,
        datetime_delta_type,
        str_compatible,
        str_raise,
        str_earlier,
        str_later,
        ..
    } = state;
    let mut dis = None;
    let mut months = DeltaMonths::ZERO;
    let mut days = DeltaDays::ZERO;
    let mut tdelta = TimeDelta::ZERO;

    match *args {
        [arg] => {
            match kwargs.next() {
                Some((key, value)) if kwargs.len() == 1 && key.py_eq(state.str_disambiguate)? => {
                    dis = Some(Disambiguate::from_py(
                        value,
                        str_compatible,
                        str_raise,
                        str_earlier,
                        str_later,
                    )?)
                }
                Some(_) => raise_type_err(format!(
                    "{}() can't mix positional and keyword arguments",
                    fname
                ))?,
                None => {}
            };
            if Py_TYPE(arg) == time_delta_type {
                tdelta = TimeDelta::extract(arg);
            } else if Py_TYPE(arg) == date_delta_type {
                let dd = DateDelta::extract(arg);
                months = dd.months;
                days = dd.days;
            } else if Py_TYPE(arg) == datetime_delta_type {
                let dt = DateTimeDelta::extract(arg);
                months = dt.ddelta.months;
                days = dt.ddelta.days;
                tdelta = dt.tdelta;
            } else {
                raise_type_err(format!("{}() argument must be a delta", fname))?
            }
        }
        [] => {
            let mut nanos = 0;
            let mut raw_months = 0;
            let mut raw_days = 0;
            handle_kwargs(fname, kwargs, |key, value, eq| {
                if eq(key, str_disambiguate) {
                    dis = Some(Disambiguate::from_py(
                        value,
                        str_compatible,
                        str_raise,
                        str_earlier,
                        str_later,
                    )?);
                    Ok(true)
                } else {
                    set_units_from_kwargs(
                        key,
                        value,
                        &mut raw_months,
                        &mut raw_days,
                        &mut nanos,
                        state,
                        eq,
                    )
                }
            })?;
            tdelta = TimeDelta::from_nanos(nanos).ok_or_value_err("Total duration out of range")?;
            // FUTURE: these range checks are double
            months = DeltaMonths::new(raw_months).ok_or_value_err("Months out of range")?;
            days = DeltaDays::new(raw_days).ok_or_value_err("Days out of range")?;
        }
        _ => raise_type_err(format!(
            "{}() takes at most 1 positional argument, got {}",
            fname,
            args.len()
        ))?,
    }
    if negate {
        months = -months;
        days = -days;
        tdelta = -tdelta;
    }
    OffsetDateTime::extract(slf)
        .shift_in_system_tz(
            state.py_api,
            months,
            days,
            tdelta,
            dis,
            state.exc_repeated,
            state.exc_skipped,
        )?
        .to_obj(cls)
}

unsafe fn difference(obj_a: *mut PyObject, obj_b: *mut PyObject) -> PyReturn {
    let type_b = Py_TYPE(obj_b);
    let type_a = Py_TYPE(obj_a);
    let state = State::for_type(type_a);
    let inst_a = OffsetDateTime::extract(obj_a).instant();
    let inst_b = if type_b == Py_TYPE(obj_a) {
        OffsetDateTime::extract(obj_b).instant()
    } else if type_b == state.instant_type {
        Instant::extract(obj_b)
    } else if type_b == state.zoned_datetime_type {
        ZonedDateTime::extract(obj_b).instant()
    } else if type_b == state.offset_datetime_type {
        OffsetDateTime::extract(obj_b).instant()
    } else {
        raise_type_err(
            "difference() argument must be an OffsetDateTime,
             Instant, ZonedDateTime, or SystemDateTime",
        )?
    };
    inst_a.diff(inst_b).to_obj(state.time_delta_type)
}

unsafe fn is_ambiguous(slf: *mut PyObject, _: *mut PyObject) -> PyReturn {
    let OffsetDateTime { date, time, .. } = OffsetDateTime::extract(slf);
    matches!(
        offset_for_system_tz(State::for_obj(slf).py_api, date, time)?,
        Ambiguity::Fold(_, _)
    )
    .to_py()
}

unsafe fn start_of_day(slf: *mut PyObject, _: *mut PyObject) -> PyReturn {
    let OffsetDateTime { date, .. } = OffsetDateTime::extract(slf);
    let &State {
        py_api,
        exc_repeated,
        exc_skipped,
        ..
    } = State::for_obj(slf);
    OffsetDateTime::resolve_system_tz_using_disambiguate(
        py_api,
        date,
        Time::MIDNIGHT,
        Disambiguate::Compatible,
        exc_repeated,
        exc_skipped,
    )?
    .to_obj(Py_TYPE(slf))
}

unsafe fn day_length(slf: *mut PyObject, _: *mut PyObject) -> PyReturn {
    let OffsetDateTime { date, .. } = OffsetDateTime::extract(slf);
    let &State {
        py_api,
        exc_repeated,
        exc_skipped,
        time_delta_type,
        ..
    } = State::for_obj(slf);
    let start_of_day = OffsetDateTime::resolve_system_tz_using_disambiguate(
        py_api,
        date,
        Time::MIDNIGHT,
        Disambiguate::Compatible,
        exc_repeated,
        exc_skipped,
    )?
    .instant();
    let start_of_next_day = OffsetDateTime::resolve_system_tz_using_disambiguate(
        py_api,
        date.tomorrow().ok_or_value_err("Date is out of range")?,
        Time::MIDNIGHT,
        Disambiguate::Compatible,
        exc_repeated,
        exc_skipped,
    )?
    .instant();
    start_of_next_day.diff(start_of_day).to_obj(time_delta_type)
}

unsafe fn round(
    slf: *mut PyObject,
    cls: *mut PyTypeObject,
    args: &[*mut PyObject],
    kwargs: &mut KwargIter,
) -> PyReturn {
    let state = State::for_type(cls);
    let (unit, increment, mode) = round::parse_args(state, args, kwargs, false, false)?;

    match unit {
        round::Unit::Day => _round_day(slf, state, mode),
        _ => {
            let OffsetDateTime {
                mut date,
                time,
                offset,
            } = OffsetDateTime::extract(slf);
            let (time_rounded, next_day) = time.round(increment as u64, mode);
            if next_day == 1 {
                date = date
                    .tomorrow()
                    .ok_or_value_err("Resulting date out of range")?;
            };
            OffsetDateTime::resolve_system_tz_using_offset(state.py_api, date, time_rounded, offset)
        }
    }?
    .to_obj(cls)
}

unsafe fn _round_day(
    slf: *mut PyObject,
    state: &State,
    mode: round::Mode,
) -> PyResult<OffsetDateTime> {
    let OffsetDateTime { date, time, .. } = OffsetDateTime::extract(slf);
    let &State {
        py_api,
        exc_repeated,
        exc_skipped,
        ..
    } = state;
    let get_floor = || {
        OffsetDateTime::resolve_system_tz_using_disambiguate(
            py_api,
            date,
            Time::MIDNIGHT,
            Disambiguate::Compatible,
            exc_repeated,
            exc_skipped,
        )
    };
    let get_ceil = || {
        OffsetDateTime::resolve_system_tz_using_disambiguate(
            py_api,
            date.tomorrow().ok_or_value_err("Date out of range")?,
            Time::MIDNIGHT,
            Disambiguate::Compatible,
            exc_repeated,
            exc_skipped,
        )
    };
    match mode {
        round::Mode::Ceil => get_ceil(),
        round::Mode::Floor => get_floor(),
        _ => {
            let time_ns = time.total_nanos();
            let floor = get_floor()?;
            let ceil = get_ceil()?;
            let day_ns = ceil.instant().diff(floor.instant()).total_nanos() as u64;
            debug_assert!(day_ns > 1);
            let threshold = match mode {
                round::Mode::HalfEven => day_ns / 2 + (time_ns % 2 == 0) as u64,
                round::Mode::HalfFloor => day_ns / 2 + 1,
                round::Mode::HalfCeil => day_ns / 2,
                _ => unreachable!(),
            };
            if time_ns >= threshold {
                Ok(ceil)
            } else {
                Ok(floor)
            }
        }
    }
}

static mut METHODS: &[PyMethodDef] = &[
    method!(identity2 named "__copy__", c""),
    method!(identity2 named "__deepcopy__", c"", METH_O),
    method!(__reduce__, c""),
    method!(to_tz, doc::EXACTTIME_TO_TZ, METH_O),
    method!(to_system_tz, doc::EXACTTIME_TO_SYSTEM_TZ),
    method_vararg!(to_fixed_offset, doc::EXACTTIME_TO_FIXED_OFFSET),
    method!(exact_eq, doc::EXACTTIME_EXACT_EQ, METH_O),
    method!(py_datetime, doc::BASICCONVERSIONS_PY_DATETIME),
    method!(to_instant, doc::EXACTANDLOCALTIME_TO_INSTANT),
    method!(instant, c""), // deprecated alias
    method!(to_plain, doc::EXACTANDLOCALTIME_TO_PLAIN),
    method!(local, c""), // deprecated alias
    method!(date, doc::LOCALTIME_DATE),
    method!(time, doc::LOCALTIME_TIME),
    method!(format_common_iso, doc::OFFSETDATETIME_FORMAT_COMMON_ISO),
    method!(
        parse_common_iso,
        doc::SYSTEMDATETIME_PARSE_COMMON_ISO,
        METH_O | METH_CLASS
    ),
    method!(now, doc::SYSTEMDATETIME_NOW, METH_CLASS | METH_NOARGS),
    method!(
        from_py_datetime,
        doc::SYSTEMDATETIME_FROM_PY_DATETIME,
        METH_O | METH_CLASS
    ),
    method!(timestamp, doc::EXACTTIME_TIMESTAMP),
    method!(timestamp_millis, doc::EXACTTIME_TIMESTAMP_MILLIS),
    method!(timestamp_nanos, doc::EXACTTIME_TIMESTAMP_NANOS),
    method!(
        from_timestamp,
        doc::SYSTEMDATETIME_FROM_TIMESTAMP,
        METH_O | METH_CLASS
    ),
    method!(
        from_timestamp_millis,
        doc::SYSTEMDATETIME_FROM_TIMESTAMP_MILLIS,
        METH_O | METH_CLASS
    ),
    method!(
        from_timestamp_nanos,
        doc::SYSTEMDATETIME_FROM_TIMESTAMP_NANOS,
        METH_O | METH_CLASS
    ),
    method_kwargs!(replace, doc::SYSTEMDATETIME_REPLACE),
    method_kwargs!(replace_date, doc::SYSTEMDATETIME_REPLACE_DATE),
    method_kwargs!(replace_time, doc::SYSTEMDATETIME_REPLACE_TIME),
    method_kwargs!(add, doc::SYSTEMDATETIME_ADD),
    method_kwargs!(subtract, doc::SYSTEMDATETIME_SUBTRACT),
    method!(difference, doc::EXACTTIME_DIFFERENCE, METH_O),
    method!(is_ambiguous, doc::SYSTEMDATETIME_IS_AMBIGUOUS),
    method!(start_of_day, doc::SYSTEMDATETIME_START_OF_DAY),
    method!(day_length, doc::SYSTEMDATETIME_DAY_LENGTH),
    method_kwargs!(round, doc::SYSTEMDATETIME_ROUND),
    PyMethodDef::zeroed(),
];

unsafe fn get_year(slf: *mut PyObject) -> PyReturn {
    OffsetDateTime::extract(slf).date.year.get().to_py()
}

unsafe fn get_month(slf: *mut PyObject) -> PyReturn {
    OffsetDateTime::extract(slf).date.month.get().to_py()
}

unsafe fn get_day(slf: *mut PyObject) -> PyReturn {
    OffsetDateTime::extract(slf).date.day.to_py()
}

unsafe fn get_hour(slf: *mut PyObject) -> PyReturn {
    OffsetDateTime::extract(slf).time.hour.to_py()
}

unsafe fn get_minute(slf: *mut PyObject) -> PyReturn {
    OffsetDateTime::extract(slf).time.minute.to_py()
}

unsafe fn get_second(slf: *mut PyObject) -> PyReturn {
    OffsetDateTime::extract(slf).time.second.to_py()
}

unsafe fn get_nanos(slf: *mut PyObject) -> PyReturn {
    OffsetDateTime::extract(slf).time.subsec.get().to_py()
}

unsafe fn get_offset(slf: *mut PyObject) -> PyReturn {
    TimeDelta::from_offset(OffsetDateTime::extract(slf).offset)
        .to_obj(State::for_obj(slf).time_delta_type)
}

static mut GETSETTERS: &[PyGetSetDef] = &[
    getter!(get_year named "year", "The year component"),
    getter!(get_month named "month", "The month component"),
    getter!(get_day named "day", "The day component"),
    getter!(get_hour named "hour", "The hour component"),
    getter!(get_minute named "minute", "The minute component"),
    getter!(get_second named "second", "The second component"),
    getter!(get_nanos named "nanosecond", "The nanosecond component"),
    getter!(get_offset named "offset", "The offset from UTC"),
    PyGetSetDef {
        name: NULL(),
        get: None,
        set: None,
        doc: NULL(),
        closure: NULL(),
    },
];

pub(crate) static mut SPEC: PyType_Spec =
    type_spec::<OffsetDateTime>(c"whenever.SystemDateTime", unsafe { SLOTS });
