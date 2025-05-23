from __future__ import absolute_import
import json
import copy
import threading
from datetime import datetime, timedelta
from mixpanel import BufferedConsumer as SynchronousBufferedConsumer
from mixpanel import MixpanelException

class FlushThread(threading.Thread):
    '''
    FlushThread is used to asynchronously flush the events stored in
    the AsyncBufferedConsumer buffers.
    '''

    def __init__(self, consumer, endpoint=None):
        '''
        Create a new instance of a FlushThread class.

        :param consumer (AsyncBufferedConsumer): Specifies the consumer where
        the flush should be called on in the thread

        :param endpoint (string): Specifies whether flush should be called on
        one specific endpoint buffer or for all endpoint buffers. An endpoint
        is one of 'people' or 'events' and represents the Mixpanel endpoint
        for sending the data.
        '''
        threading.Thread.__init__(self)
        self.consumer = consumer
        self.endpoint = endpoint

    def run(self):
        # if we create the flushing thread with an endpoint value,
        # it only flushes the given endpoint
        if self.endpoint:
            self.consumer._sync_flush(endpoint=self.endpoint)
        else:
            self.consumer._sync_flush()


class AsyncBufferedConsumer(SynchronousBufferedConsumer):
    '''
    AsyncBufferedConsumer works just like the BufferedConsumer, but
    flushes events in a asynchronous thread after a given number of
    messages or a given time period.

    Because AsyncBufferedConsumer holds events until the `flush_after` timeout
    or an endpoint queue hits the size of _max_queue_size, you should call
    flush(async_=False) before you terminate any process where you have been
    using the AsyncBufferedConsumer.
    '''

    # constants used in the _should_flush method
    ALL = "ALL"
    ENDPOINT = "ENDPOINT"

    def __init__(
        self,
        flush_after=timedelta(0, 10),
        flush_first=True,
        max_size=20,
        events_url=None,
        people_url=None,
        import_url=None,
        request_timeout=None,
        groups_url=None,
        api_host="api.mixpanel.com",
        retry_limit=4,
        retry_backoff_factor=0.25,
        verify_cert=True,
    ):
        '''
        Create a new instance of a AsyncBufferedConsumer class.

        :param flush_after (datetime.timedelta): the time period after which
        the AsyncBufferedConsumer will flush the events upon receiving a
        new event (no matter what the event queue size is).
        :param flush_first (bool): if True, always flush the first event that
        the consumer receives
        :param max_size (int): the number of events in queue that will trigger
        the queue to be flushed asynchronously
        :param events_url: Mixpanel API URL that track events will be sent to
        :param people_url: Mixpanel API URL that people events will be sent to
        :param import_url: Mixpanel API URL that import events will be sent to
        :param request_timeout: Connection timeout in seconds
        :param groups_url: Mixpanel API URL that groups events will be sent to
        :param api_host: Mixpanel API domain for all requests unless overriden by above URLs
        :param retry_limit: Number of times to retry each request in case of an error, 0
        to fail after first attempt.
        :param retry_backoff_factor: Factor which controls sleep duration between retries:
        sleep_seconds = backoff_factor * (2 ^ (retry_count - 1))
        :param verify_cert: Whether to verify the server certificate. "True" is
        recommended.
        '''
        super(AsyncBufferedConsumer, self).__init__(
            max_size=max_size,
            events_url=events_url,
            people_url=people_url,
            import_url=import_url,
            request_timeout=request_timeout,
            groups_url=groups_url,
            api_host=api_host,
            retry_limit=retry_limit,
            retry_backoff_factor=retry_backoff_factor,
            verify_cert=verify_cert,
        )

        # remove the minimum max size that the SynchronousBufferedConsumer
        # class sets
        self._max_size = max_size
        self.flush_after = flush_after
        self.flush_first = flush_first

        self._async_buffers = copy.deepcopy(self._buffers)

        if not self.flush_first:
            self.last_flushed = datetime.now()
        else:
            self.last_flushed = None

        self.flush_lock = threading.Lock()
        self.flushing_thread = None


    def _flush_thread_is_free(self):
        '''
        Check whether a thread is currently being used to flush events. This
        guarantees that only one thread is ever used at a time to flush.
        '''
        return self.flushing_thread is None \
            or not self.flushing_thread.is_alive()


    def _should_flush(self, endpoint=None):
        '''
        Checks whether the events in the AsyncBufferedConsumer should be flushed.

        :param endpoint string: the endpoint that is being checked for need
        to flush.
        '''
        full = False

        if endpoint:
            full = len(self._async_buffers[endpoint]) >= self._max_size

        # always flush the first event
        stale = self.last_flushed is None

        if not stale and self.flush_after:
            # if a flush_after value is set, then we check whether the last
            # flush was more than flush_after seconds (or other timedelta) ago
            stale = datetime.now() - self.last_flushed > self.flush_after

        if stale:
            # if the consumer has passed the timeout for sending events,
            # we return that it should flush all events
            return self.ALL

        if full:
            # if the endpoint queue where the event was added to is full,
            # we return that it should flush all events in that endpoint queue
            return self.ENDPOINT

        return False


    def send(self, endpoint, json_message, api_key=None):
        '''
        Record an event or a profile update. Calls to send() will store
        the given message in memory, and (when enough messages have been stored)
        trigger an async request to Mixpanel's servers.

        Calls to send() may throw an exception, but the exception may be
        associated with the message given in an earlier call. If this is the case,
        the resulting MixpanelException e will have members e.message and e.endpoint

        :param endpoint: One of 'events' or 'people', the Mixpanel endpoint for sending the data
        :type endpoint: str (one of 'events' or 'people')
        :param json_message: A json message formatted for the endpoint.
        :type json_message: str
        :param api_key: Your Mixpanel project's API key
        :type api_key: str
        :raises: MixpanelException
        '''
        if endpoint not in self._async_buffers:
            raise MixpanelException('No such endpoint "{0}". Valid endpoints are one of {1}'.format(endpoint, self._async_buffers.keys()))

        buf = self._async_buffers[endpoint]
        buf.append(json_message)

        if api_key is not None:
            self._api_key = api_key

        should_flush = self._should_flush(endpoint)

        if should_flush == self.ALL:
            self.flush()
        elif should_flush == self.ENDPOINT:
            self._flush_endpoint(endpoint)


    def flush(self, endpoint=None, async_=True):
        '''
        Send all remaining messages to Mixpanel. AsyncBufferedConsumers will
        flush automatically when you call send(), but you will need to call
        flush() when you are completely done using the consumer (for example,
        when your application exits) to ensure there are no messages remaining
        in memory.

        Calls to flush() may raise a MixpanelException if there is a problem
        communicating with the Mixpanel servers. In this case, the exception
        thrown will have a message property, containing the text of the message,
        and an endpoint property containing the endpoint that failed.


        :param endpoint (str): One of 'events' or 'people, the Mixpanel endpoint
        for sending the data
        :param async (bool): Whether to flush the data in a seperate thread or not
        '''

        flushing = False

        if async_:
            # this flush lock is used to guarantee that only one flushing_thread
            # is ever alive.
            with self.flush_lock:
                if self._flush_thread_is_free():

                    self.transfer_buffers(endpoint=endpoint)

                    self.flushing_thread = FlushThread(self, endpoint=endpoint)
                    self.flushing_thread.start()

                    flushing = True
                else:
                    # this is the case where another FlushingThread has been
                    # activated and is still alive. In this situation, no new
                    # flush is run and we do not mark last_flushed. This results
                    # in two outcomes:
                    #
                    #   (1) the queue that is triggering this second flush is
                    #   cleared by the first flush, meaning the second flush
                    #   was unnecessary.
                    #
                    #   (2) last_flushed will still be stale so the next time an
                    #   event is added this second flush will be retriggered and
                    #   will complete.
                    flushing = False

        else:
            self.transfer_buffers(endpoint=endpoint)
            self._sync_flush(endpoint=endpoint)
            flushing = True

        if flushing:
            self.last_flushed = datetime.now()

        return flushing


    def transfer_buffers(self, endpoint=None):
        """
        Transfer events from the `_async_buffers` where they are stored to the
        `_buffers` where they will be flushed from by the flushing thread.

        :param endpoint (str): One of 'events' or 'people, the Mixpanel endpoint
        that is about to be flushed
        """
        if endpoint:
            keys = [endpoint]
        else:
            keys = self._async_buffers.keys()

        for key in keys:
            buf = self._async_buffers[key]
            while buf:
                self._buffers[key].append(buf.pop(0))


    def _flush_endpoint(self, endpoint, async_=True):
        # we override flush with endpoint so as to keep all the
        # threading logic in one place, while still allowing individual
        # endpoints to be flushed
        self.flush(endpoint=endpoint, async_=async_)


    def _sync_flush(self, endpoint=None):
        if endpoint:
            super(AsyncBufferedConsumer, self)._flush_endpoint(endpoint)
        else:
            for endpoint in self._buffers.keys():
                super(AsyncBufferedConsumer, self)._flush_endpoint(endpoint)
