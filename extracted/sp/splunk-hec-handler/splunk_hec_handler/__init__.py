import json
import logging
import requests
import ast
import socket


class SplunkHecHandler(logging.Handler):
    """
    This module returns a python logging handler capable of sending logs records to a Splunk HTTP Event Collector
    listener.  Log records can be simple string or dictionary.  In the latter case, if the sourcetype is configured
    to be _json (or variant), JSON format of the log message will be preserved.

    Example
    -------

    .. code-block:: text

        import logging
        from splunk_hec_handler import SplunkHecHandler
        logger = logging.getLogger('SplunkHecHandlerExample')
        logger.setLevel(logging.DEBUG)

        splunk_handler = SplunkHecHandler('splunkfw.domain.tld',
                            'EA33046C-6FEC-4DC0-AC66-4326E58B54C3',
                            port=8888, proto='https', ssl_verify=True,
                            source="HEC_example")
        logger.addHandler(splunk_handler)

        logger.info("Testing Splunk HEC Info message")

    Splunk Event Output
    -------------------
    Following should result in a Splunk entry with _time set to current timestamp :

    .. code-block:: text

        {
            log_level: INFO
            message: Testing Splunk HEC Info message
        }
    References
    ----------
    #. See http://dev.splunk.com/view/event-collector/SP-CAAAE6P for 'fields'
    #. Splunk remote logging configuration
        * http://docs.splunk.com/Documentation/SplunkCloud/latest/Data/UsetheHTTPEventCollector
        * http://docs.splunk.com/Documentation/Splunk/latest/Data/UsetheHTTPEventCollector
    #. To use fields, sourcetype must be specified and must allow for indexed field extractions

        .. code-block:: text

            dict_obj = {'time': 1533530023, 'fields': {'color': 'yellow', 'api_endpoint': '/results'},
                        'user': 'foobar', 'app': 'my demo', 'severity': 'low', 'error codes': [1, 23, 34, 456]}
            logger.error(dict_obj)
    """
    URL_PATTERN = "{0}://{1}:{2}/services/collector/{3}"
    TIMEOUT = 30

    def __init__(self, host, token, **kwargs):
        """
        Creates a python logging handler, capable of sending logs to Splunk server.

        :param host: Splunk server hostname or IP.
        :type host: ``str``
        :param token: Splunk HEC Token (see http://docs.splunk.com/Documentation/Splunk/latest/Data/UsetheHTTPEventCollector#About_Event_Collector_tokens)
        :type token: ``str``

        :kwargs Keyword Arguments :
            * *port* (``int``) -- 0-65535 port number of Splunk HEC listener
            * *proto* (``str``) -- [http | https]
            * *ssl_verify* (``bool|str```) -- [True|False|<Path to cert>].  True by default.
                see https://2.python-requests.org/en/master/user/advanced/#ssl-cert-verification
            * *source* (``str``) -- Override source value specified in Splunk HEC configuration.  None by default.
            * *sourcetype* (``str``) -- Override sourcetype value specified in Splunk HEC configuration.  None by default.
            * *hostname* (``str``) -- Specify custom host value.  Defaults to hostname returned by socket.gethostname()
            * *endpoint* (``str``) -- [raw|event].  Use 'raw' if field extractions should be skipped.
                see http://docs.splunk.com/Documentation/Splunk/latest/RESTREF/RESTinput#services.2Fcollector.2Fraw
            * *empty_body* (``bool``) -- [True|False] Initialize with an empty body. Eliminate *log_level* in log body.  *Default is False.*
        """
        self.host = host
        self.token = token
        if kwargs is not None:
            self.port = int(kwargs.get('port', 8080))
            self.proto = kwargs.get('proto', 'https')
            self.ssl_verify = False if (kwargs.get('ssl_verify') in ["0", 0, "false", "False", False]) \
                else kwargs.get('ssl_verify') or True
            self.source = kwargs.get('source')
            self.index = kwargs.get('index')
            self.sourcetype = kwargs.get('sourcetype')
            self.hostname = kwargs.get('hostname', socket.gethostname())
            self.endpoint = kwargs.get('endpoint', 'event')
            self.empty_body = kwargs.get('empty_body', False)

        try:
            # Testing connectivity
            s = socket.socket()
            s.settimeout(kwargs.get('timeout', self.TIMEOUT))
            s.connect((self.host, self.port))

            # Socket accessible.  Establish requests session
            self.r = requests.session()
            self.r.max_redirects = 1
            self.r.verify = self.ssl_verify
            self.r.headers['Authorization'] = "Splunk {}".format(self.token)
            logging.Handler.__init__(self)
        except Exception as err:
            logging.debug("Failed to connect to remote Splunk server (%s:%s). Exception: %s"
                          % (self.host, self.port, err))
            raise err
        else:
            self.url = self.URL_PATTERN.format(self.proto, self.host, self.port, self.endpoint)
            s.close()

    def emit(self, record):
        """
        Send log record to Splunk HEC listener
        :param record: string or dictionary. String record is logged as 'message' in Splunk.
        Dictionary is preserved as JSON object.  log_level is set to requested log level.
        :return: None
        """
        if self.empty_body:
            body = {}
        else:
            body = {'log_level': record.levelname}

        try:
            if record.msg.__class__ == dict:
                # If record.msg is dict, leverage it as is
                body.update(record.msg)
            else:
                # Check to see if msg can be converted to a python object
                body.update({'message': ast.literal_eval(str(record.msg))})
        except Exception as err:
            logging.debug("Log record emit exception raised. Exception: %s " % err)
            body.update({'message': record.msg})

        event = dict({'host': self.hostname, 'event': body, 'fields': {}})

        # Splunk 7.x does not like empty fields
        if self.source is not None:
            event['source'] = self.source

        if self.sourcetype is not None:
            event['sourcetype'] = self.sourcetype

        if self.index is not None:
            event['index'] = self.index

        # Use timestamp from event if available
        # Note, 'time' in 'fields' will override this
        if 'time' in body.keys():
            event['time'] = body['time']
        # Default to log record create time and preserve fractional seconds
        else:
            event['time'] = record.created

        # fields
        # This specifies explicit custom fields that are separate from the main "event" data.
        # This method is useful if you don't want to include the custom fields with the event data,
        # but you want to be able to annotate the data with some extra information, such as where it came from.
        # http://dev.splunk.com/view/event-collector/SP-CAAAFB6
        if ('fields' in body.keys() and hasattr(body['fields'], 'items')) or ('time' in body.keys()):
            try:
                for k, v in body['fields'].items():
                    if k in ['host', 'source', 'sourcetype', 'time', 'index']:
                        event[k] = v
                    else:
                        try:
                            if type(v) in [str, list]:
                                event['fields'][k] = v
                            else:
                                # Splunk fails to index event if fields contains values of type other than str or list
                                # i.e HTTP Status: 400, Reason: Bad Request,
                                # Content: {"text":" Error in handling indexed fields", "code":15}
                                event['fields'][k] = str(v)
                        except Exception:
                            pass
            except Exception:
                pass
            else:
                body.pop('fields')

        try:
            # 'skipkeys' - If skipkeys is true (default: False), then dict keys that are not of a basic type
            # (str, int, float, bool, None) will be skipped instead of raising a TypeError.
            # 'default' - If specified, default should be a function that gets called for objects that can’t otherwise
            # be serialized. It should return a JSON encode-able version of the object or raise a TypeError.
            data = json.dumps(event, sort_keys=True, skipkeys=True, default=self.serializer)
        except TypeError:
            raise

        try:
            req = self.r.post(self.url, data=data, timeout=self.TIMEOUT, headers={'Connection': 'close'})

            req.raise_for_status()
        except requests.exceptions.HTTPError as err:
            logging.debug("Failed to emit record to Splunk server (%s:%s).  Exception raised: %s"
                          % (self.host, self.port, err))
            raise err

    @staticmethod
    def serializer(obj):
        if type(obj) in [set, frozenset, range]:
            return list(obj)
        else:
            try:
                return str(obj)
            except Exception:
                raise
