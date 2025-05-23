#-*- coding: utf-8 -*-


# Python Imports
import calendar
import datetime
import decimal
import email.utils
import functools
import hashlib
import inspect
import ipaddress
import itertools
import json
import logging
import os
import pprint
import random
import re
import shlex
import signal
import socket
import string
import subprocess
import sys
import threading
import time
import urllib.parse
import xml

# Extern Imports
# This space intentionally left blank. Doing python3 -m build was hitting errors, since they aren't importable in the build scope.
# Currently they are imported into stdlib.py as-needed.

def absdir(path):
    return os.path.abspath(os.path.dirname(path))

def get_caller():
    f = inspect.currentframe()
    f = f.f_back
    f = f.f_back
    filename = f.f_code.co_filename
    module = filename.split('/')[-1].split('.')[0]
    #label = '%s.%s' % (module, f.f_code.co_name)
    #print(label)
    lineno = f.f_lineno
    return "%s:%s" % (module, lineno)

def logw(var, msg=''):
    caller = get_caller()
    logging.warning('%s %s %s %s', cstr(caller, 'yellow'), msg, type(var), pprint.pformat(var))

def loge(var, msg=''):
    caller = get_caller()
    logging.error('%s %s %s %s', cstr(caller, 'red'), msg, type(var), pprint.pformat(var))

def logline(*args):
    caller = get_caller()
    msg = '%s %s' % (cstr(caller, 'yellow'), args[0])
    logging.warning(msg, *args[1:])

def shell(cmd, cwd=None, env=None, decode_utf8=True, timeout=None):
    if type(cmd) not in (tuple, list):
        cmd = shlex.split(cmd)
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False, cwd=cwd, env=env)
    stdout, stderr = proc.communicate(timeout=timeout)
    if decode_utf8:
        stdout = stdout.decode('utf-8').strip()
        stderr = stderr.decode('utf-8').strip()
    return (stdout, stderr, proc.returncode)

def multi_shell(cmds, cwd=None, env=None):
    """ These processes should all be started and non-blocking. Then caller can use communicate(), wait(), call() as needed. """
    procs = []
    for cmd in cmds:
        procs.append(subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False, cwd=cwd, env=env))
    return procs

def force_int(string):
    if type(string) in (int, int): return int(string)
    int_re = re.compile(r'^.*?(\d+).*?$')
    match = int_re.match(string)
    if not match: return None
    return int(match.group(1))

def md5hex(val=None, encoding=None):
    if val:
        if encoding:
            val = val.encode(encoding)
        return hashlib.md5(val).hexdigest()
    else:
        return hashlib.md5().hexdigest()

def bcrypt_salt(log_rounds=14):
    import bcrypt
    return bcrypt.gensalt(rounds=log_rounds)

def bcrypt_hashpw(password, salt):
    import bcrypt
    result = bcrypt.hashpw(password, salt.encode('utf-8'))
    return result

def bcrypt_password(password, log_rounds=14):
    import bcrypt
    import tornado.util
    if type(password) is str:
        password = password.encode('utf-8')
    salt = tornado.util.unicode_type(bcrypt.gensalt(rounds=log_rounds), 'ascii').encode('utf-8')
    return bcrypt.hashpw(password, salt)

password_len = 24
password_chars = string.ascii_letters + string.digits
def pwgen(pw_len=password_len, pw_chars=password_chars):
    pw = functools.reduce(lambda x, y: x + random.choice(pw_chars), range(pw_len), '')
    max_pw = float(pow(len(pw_chars), pw_len))
    max_pw_int = int(max_pw)
    max_pw_str = f"{max_pw_int:100,}"
    return pw, max_pw, max_pw_str

def html_unescape(val):
    return xml.sax.saxutils.unescape(val, {'&quot;': '"'})

def split_name(name):
    if not name or type(name) is not str:
        return None
    names = name.split()
    if len(names) == 1:
        return {'first_name': name, 'last_name': ''}
    else:
        first = ' '.join(name.split()[:-1])
        last = name.split()[-1]
        return {'first_name': first, 'last_name': last}

def map_items(items, key):
    return dict([(item[key], item) for item in items])

# From Maxime Biais's comment on http://www.peterbe.com/plog/uniqifiers-benchmark
# Preserves order of the iterable in the return value
def unique_list(iterable):
    m = set()
    return list(filter(lambda x: not (m.__contains__(x) or m.add(x)), iterable))

# From the accepted answer on http://stackoverflow.com/questions/642763/python-intersection-of-two-lists
# Preserves order of the items in the second iterable
def stable_intersection(iter1, iter2):
    return list(filter(set(iter1).__contains__, iter2))

# Modified from above - remove items in 'iter_remove' from items in 'iter_keep'
def stable_difference(iter_remove, iter_keep):
    return list(itertools.filterfalse(set(iter_remove).__contains__, iter_keep))

def loopnext(iterable, itr):
    try:
        val = next(itr)
    except StopIteration:
        itr = iter(iterable)
        val = next(itr)
    return val, itr

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        elif isinstance(obj, datetime.date):
            return obj.isoformat()
        elif isinstance(obj, datetime.timedelta):
            return (datetime.datetime.min + obj).time().isoformat()
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
        else:
            return super(DateTimeEncoder, self).default(obj)


# Tools for converting 'snake_case' to 'lowerCamelCase' 'UpperCamelCase' and 'Space Camel Case'. Adapted from: https://stackoverflow.com/a/19053800
def snake_to_camel(snake_str, upper=False, space=False):
    components = snake_str.split('_')
    if upper:
        join_char = ''
        if space:
            join_char = ' '
        # Capitalize the first letter of each component, using title(), then join them together.
        return join_char.join(x.title() for x in components)
    else:
        # Capitalize the first letter of each component except the first one, using title(), then join them together.
        return components[0] + ''.join(x.title() for x in components[1:])

def camel_to_snake(camelStr):
      mid_str = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', camelStr)
      return re.sub('([a-z0-9])([A-Z])', r'\1_\2', mid_str).lower()

# This rewrites the key in-place. Make a copy.deepcopy() before calling this!
def json_snake_to_camel(json_obj, upper=False, space=False, debug=False):
    mro = inspect.getmro(json_obj.__class__)
    if dict in mro:
        # Since the json_obj is changing in place, grab the keys to iterate up front so the iterator doesn't change during the loop
        for snake_key in list(json_obj.keys()):
            value = json_obj.get(snake_key)
            if debug:
                logw(snake_key, "SNAKE KEY")
                logw(value, "VALUE")
            camel_key = snake_to_camel(snake_key, upper=upper, space=space)
            if debug:
                logw(camel_key, "CAMEL KEY")
            value_mro = inspect.getmro(value.__class__)
            if dict in value_mro or list in value_mro:
                if debug:
                    logw(value, "DICT VALUE BEFORE")
                json_snake_to_camel(value, upper=upper, space=space, debug=debug)
                if debug:
                    logw(value, "DICT VALUE AFTER")
            json_obj[camel_key] = value
            if camel_key != snake_key:
                del json_obj[snake_key]
    elif list in mro:
        for item in json_obj:
            if debug:
                logw(item, "LIST ITEM BEFORE")
            json_snake_to_camel(item, upper=upper, space=space, debug=debug)
            if debug:
                logw(item, "LIST ITEM AFTER")


def ts_to_dt(timestamp):
    if timestamp is None: return None
    return datetime.datetime.utcfromtimestamp(timestamp)

def dt_to_ts(dttm, keep_milliseconds=False):
    """ calendar.timegm() doesn't maintain the microseconds awareness of datetime (!?!)
        maintain the milliseconds as an integer to fit into 8 bytes: 1516687988867
        could also for example be sent as decimal representation with microseconds: 1516687988.867397
    """
    if dttm is None: return None
    if keep_milliseconds:
        return int(str(calendar.timegm(dttm.utctimetuple())) + str(dttm.microsecond)[:3])
    else:
        return calendar.timegm(dttm.utctimetuple())


# Make it easier to use ansi escape sequences for terminal colors
colors = {'black' : 30, 'red' : 31, 'green' : 32, 'yellow' : 33, 'blue' : 34,
          'magenta' : 35, 'cyan' : 36, 'white' : 37, 'reset': 39, }
attrs = {'reset':'0', 'bold':'1', 'faint':'2', 'regular':'2',
         'underscore':'4', 'blink':'5', 'reverse':'7'}

def ansi_esc(colorName, **kwargs):
    out = '\x1B['
    if 'attr' in kwargs and kwargs['attr'] in attrs:
        out += attrs[kwargs['attr']] + ';'
    if 'bgcolor' in kwargs and kwargs['bgcolor'] in colors:
        bgcolor = colors[kwargs['bgcolor']] + 10
        out += str(bgcolor) + ';'
    out += str(colors[colorName]) + 'm'
    return out

def cline(line, mode):
    pick_ansi = {'-': 'red', '+': 'green', '*': 'green', '@': 'cyan'}
    color = pick_ansi.get(line[0], '')
    if color != '':
        line = ansi_esc(color) + line + ansi_esc('reset')
    if mode == 'print': print(line)
    if mode == 'return': return line

def cdiff(line):
    pick_ansi = {'-': 'red', '+': 'green', '*': 'green'}
    color = pick_ansi.get(line[0], '')
    if color != '':
        return ansi_esc(color) + line + ansi_esc('reset')
    else:
        return line

def cstr(data, color):
    return ansi_esc(color) + data + ansi_esc('reset')

def nl2br(value):
    return value.replace('\n', '<br />')

def format_integer(number):
    return "{:,}".format(number)

def format_money(amount, rjust=None):
    amt = "%.2f" % amount
    profile = re.compile(r"(\d)(\d\d\d[.,])")
    while 1:
        amt, count = re.subn(profile, r"\1,\2", amt)
        if not count:
            break
    if rjust:
        return amt.rjust(rjust)
    return amt


# Token format that is unique and hard to guess. Enforce at least one letter so it can't accidentally be cast to an int.
# Combine with a second factor like a row_id to eliminate unbelievably lucky brute force possibilities.
#>>> chars=8; "%4.2f Trillion Should Be Enough For Just %s Chars" % (float(26*pow(36, chars-1)) / float(pow(1024, 4)), chars)
#'1.85 Trillion Should Be Enough For Just 8 Chars'
#>>> chars=10; "If not, %4.2f Trillion in %s Chars Should Definitely Be Enough" % (float(26*pow(36, chars-1)) / float(pow(1024, 4)), chars)
#'If not, 2401.57 Trillion in 10 Chars Should Definitely Be Enough'
#>>> chars=12; "Ludicrous Odds: %s Chars Makes For %4.2f Trillion Possibilities (3 Quintillion)" % (chars, float(26*pow(36, chars-1)) / float(pow(1024, 4)))
#'Ludicrous Odds: 12 Chars Makes For 3112440.30 Trillion Possibilities (3 Quintillion)'
token_length = 10
token_chars = string.ascii_letters + string.digits
def magic_token(length=token_length):
    return random.choice(string.ascii_lowercase) + functools.reduce(lambda x, y: x + random.choice(token_chars), range(length-1), '').lower()

def validate_token(row_id, token):
    return validate_int(row_id) and token and len([ch for ch in token if ch in token_chars]) == token_length

def validate_int(value):
    # int() can't take a None so we have to check that first
    if value is None:
        return None
    # As long as it's a string we can remove commas, since those don't validate
    if type(value) is str:
        value = value.replace(',', '')
    try:
        return int(value)
    except (ValueError, TypeError):
        return None

def validate_date(value):
    if not value:
        return None
    if type(value) is datetime.datetime:
        return value
    try:
        import dateutil.parser
        return dateutil.parser.parse(value)
    except (ValueError, TypeError):
        return None

def validate_bool(value):
    if value is None:
        return None
    if type(value) is bool:
        return value
    return bool(value)

def validate_decimal(value):
    if value is None:
        return None
    if type(value) in (float, int):
        return decimal.Decimal(value)
    try:
        value = decimal.Decimal(re.sub(r'[^\d.-]', '', value.strip()))
    except decimal.InvalidOperation:
        return None
    return value

def validate_ip_address(value):
    try:
        ip = ipaddress.ip_address(value)
        return ip
    except:
        return None

def validate_json(value):
    if type(value) is dict:
        return value
    try:
        return json.loads(value)
    except ValueError:
        return None

def validate_url(url):
    try:
        result = urllib.parse.urlparse(url)
        if not result.path:
            result = result._replace(path='/')
        if all([result.scheme, result.netloc, result.path]):
            return result
    except Exception as ex:
        logging.exception(ex)
        return False


email_validator = None
def validate_email(value):
    global email_validator
    if not email_validator:
        email_validator = EmailValidator()
    if value is None:
        return None
    if type(value) is not str:
        return None
    try:
        email_validator.validate(value)
        return value.lower()
    except ValueError:
        logging.warning("Invalid email: %s", value)
        return None

### Adapted from Django: https://github.com/django/django/blob/11b8c30b9e02ef6ecb996ad3280979dfeab700fa/django/core/validators.py
class EmailValidator:
    user_regex = re.compile(
        r"(^[-!#$%&'*+/=?^_`{}|~0-9A-Z]+(\.[-!#$%&'*+/=?^_`{}|~0-9A-Z]+)*\Z"  # dot-atom
        r'|^"([\001-\010\013\014\016-\037!#-\[\]-\177]|\\[\001-\011\013\014\016-\177])*"\Z)',  # quoted-string
        re.IGNORECASE)
    domain_regex = re.compile(
        # max length for domain name labels is 63 characters per RFC 1034
        r'((?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+)(?:[A-Z0-9-]{2,63}(?<!-))\Z',
        re.IGNORECASE)
    literal_regex = re.compile(
        # literal form, ipv4 or ipv6 address (SMTP 4.1.3)
        r'\[([A-f0-9:\.]+)\]\Z',
        re.IGNORECASE)
    domain_whitelist = ['localhost']

    def __init__(self, whitelist=None):
        if whitelist is not None:
            self.domain_whitelist = whitelist

    def validate(self, value):
        if not value or '@' not in value:
            raise ValueError("Email must have @ sign")
        user_part, domain_part = value.rsplit('@', 1)
        if not self.user_regex.match(user_part):
            raise ValueError("Invalid user part")
        if (domain_part not in self.domain_whitelist and not self.validate_domain_part(domain_part)):
            # Try for possible IDN domain-part
            try:
                domain_part = domain_part.encode('idna').decode('ascii')
            except UnicodeError:
                pass
            else:
                if self.validate_domain_part(domain_part):
                    return True
            raise ValueError("Invalid domain part")
        return True

    def validate_domain_part(self, domain_part):
        if self.domain_regex.match(domain_part):
            return True
        literal_match = self.literal_regex.match(domain_part)
        if literal_match:
            ip_address = literal_match.group(1)
            return validate_ip_address(ip_address)
        return False


### Known Robots Handling, used along with user_agents module is_bot()
class RobotValidator:
    robot_patterns = [
        '360Spider',
        '80legs.com/webcrawler',
        'ADmantX',
        '^123peoplebot',
        '^.{1,4}$',
        '^A1 Website Download',
        '^A12$',
        '^A6-Indexer',
        '^abc',
        '^Aboundex',
        '^About.me',
        '^AdnormCrawler',
        '^AdsBot-Google',
        '^Aghaven',
        '^Anemone',
        '^Apache-HttpClient/',
        '^AppEngine-Google;',
        '^Apple-PubSub',
        '^ArcheType',
        '^AsyncHttpClient',
        '^Atomic_Email_Hunter',
        '^Attribot',
        '^BacklinkCrawler',
        '^Baiduspider',
        '^BDFetch',
        '^BigBozz Bot',
        'BingPreview/',
        '^binlar_',
        '^bitlybot',
        '^Browserlet',
        '^BublupBot',
        '^Bufferbot',
        '^CatchBot',
        '^CCBot',
        'CensysInspect',
        '^check_http',
        '^checks.panopta.com',
        '^CJNetworkQuality',
        '^CloudACL',
        '^coccoc',
        '^COMODO',
        '^Comodo-Certificates-Spider',
        '^Content Crawler',
        '^ContextAd Bot',
        '^crawl',
        '^Crowsnest',
        '^curl/',
        'Daum/',
        '^Docunator',
        '^DomainCrawler',
        '^Domnutch-Bot',
        '^elefent/Elefent',
        '^EventGuruBot',
        '^EventMachine',
        '^Evolution Crawler',
        '^ExactSeek Crawler',
        '^ExB Language Crawler',
        '^facebookexternalhit',
        '^facebookplatform',
        '^Feedfetcher-Google',
        '^feedfinder',
        '^fetch libfetch',
        '^findlinks',
        '^Firefox 5.0.2$',
        '^Firefox$',
        '^FisigBot',
        '^FlightDeckReportsBot',
        '^GarlikCrawler',
        '^geotest',
        '^Gigabot',
        '^gimme60',
        '^Goldfire Server',
        '^Google-Site-Verification',
        '^Google-Test',
        '^Google_Analytics_Content_Experiments',
        '^Google_Analytics_Snippet_Validator',
        'Google-InspectionTool',
        '^Googlebot-Image',
        'Google Favicon',
        'Google-Read-Aloud',
        '^gsa-crawler',
        '^Hatena::Bookmark',
        '^HuaweiSymantecSpider',
        '^ia_archiver',
        '^ichiro',
        '^InAGist',
        '^InboundScore',
        '^Influencebot',
        '^ip-web-crawler.com',
        '^it2media-domain-crawler',
        '^IXEbot',
        '^Jakarta',
        '^Java',
        '^KD Bot',
        '^Kimengi/nineconnections.com',
        '^larbin',
        '^libwww-perl',
        '^Linguee Bot',
        '^LinkedInBot',
        '^LongURL API',
        '^LSSRocketCrawler',
        '^Luminator',
        '^Maggie',
        '^magpie-crawler',
        '^Mail.RU',
        '^mantam',
        '^Mediapartners-Google',
        '^MetaURI',
        '^Microsoft Windows Network Diagnostics',
        '^MLBot',
        '^montastic-monitor',
        r'^Mozilla/.*\(compatible$',
        '^Mozilla/.*Abonti',
        '^Mozilla/.*AcoonBot',
        '^Mozilla/.*AhrefsBot',
        '^Mozilla/.*aiHitBot',
        '^Mozilla/.*AppEngine-Google',
        '^Mozilla/.*archive.org',
        '^Mozilla/.*baidu.com',
        '^Mozilla/.*Baiduspider',
        '^Mozilla/.*BigBozzBot',
        '^Mozilla/.*bingbot',
        '^Mozilla/.*Blekkobot',
        '^Mozilla/.*Butterfly',
        '^Mozilla/.*CareerBot',
        '^Mozilla/.*Cliqusbot',
        '^Mozilla/.*coccoc/',
        '^Mozilla/.*CompSpyBot',
        '^Mozilla/.*Dataprovider Site Explorer',
        '^Mozilla/.*DCPbot',
        '^Mozilla/.*Diffbot',
        '^Mozilla/.*discobot',
        '^Mozilla/.*discoverybot',
        '^Mozilla/.*EasouSpider',
        '^Mozilla/.*Embedly',
        '^Mozilla/.*evc',
        '^Mozilla/.*EventGuruBot',
        '^Mozilla/.*Exositesbot',
        '^Mozilla/.*Ezooms',
        '^Mozilla/.*FacebookStatistics',
        '^Mozilla/.*FlipboardProxy',
        '^Mozilla/.*FriendFeedBot',
        '^Mozilla/.*Genieo',
        '^Mozilla/.*GrapeshotCrawler',
        '^Mozilla/.*Gravitybot',
        '^Mozilla/.*heritrix',
        '^Mozilla/.*HTTrack',
        r'^Mozilla/.*ICS\)$'
        '^Mozilla/.*IntelCSbot',
        '^Mozilla/.*ips-agent',
        '^Mozilla/.*JikeSpider',
        '^Mozilla/.*KomodiaBot',
        '^Mozilla/.*lemurwebcrawler',
        '^Mozilla/.*ltbot',
        '^Mozilla/.*LucidWorks',
        '^Mozilla/.*Mail.RU',
        '^Mozilla/.*Memorybot',
        '^Mozilla/.*MJ12bot',
        '^Mozilla/.*MojeekBot',
        '^Mozilla/.*monitis - premium monitoring service',
        '^Mozilla/.*MSIE or Firefox mutant; not on Windows server;',
        '^Mozilla/.*NaverJapan',
        '^Mozilla/.*NerdByNature.Bot',
        '^Mozilla/.*news bot',
        '^Mozilla/.*Nigma.ru',
        '^Mozilla/.*Nmap Scripting Engine',
        '^Mozilla/.*oBot',
        '^Mozilla/.*OpenindexSpider',
        '^Mozilla/.*PaperLiBot',
        '^Mozilla/.*Plukkie',
        '^Mozilla/.*ProCogBot',
        '^Mozilla/.*proximic',
        '^Mozilla/.*redditbot',
        '^Mozilla/.*ReverseGet',
        '^Mozilla/.*Robo',
        '^Mozilla/.*ScoutJet',
        '^Mozilla/.*ScribdReader',
        '^Mozilla/.*search.thunderstone.com',
        '^Mozilla/.*Search17Bot',
        '^Mozilla/.*SearchmetricsBot',
        '^Mozilla/.*SemrushBot',
        '^Mozilla/.*SISTRIX Crawler',
        '^Mozilla/.*SiteBot',
        '^Mozilla/.*SiteExplorer',
        '^Mozilla/.*Sosospider',
        '^Mozilla/.*spbot',
        '^Mozilla/.*special_archiver',
        '^Mozilla/.*Statsbot',
        '^Mozilla/.*Steeler',
        '^Mozilla/.*suggybot',
        '^Mozilla/.*SurveyBot',
        '^Mozilla/.*Swarm',
        '^Mozilla/.*SWEBot',
        '^Mozilla/.*TourlentaScanner',
        '^Mozilla/.*TweetedTimes',
        '^Mozilla/.*TweetmemeBot',
        '^Mozilla/.*Undrip Bot',
        '^Mozilla/.*UnisterBot',
        '^Mozilla/.*WASALive-Bot',
        '^Mozilla/.*Wazzup',
        '^Mozilla/.*WBSearchBot',
        '^Mozilla/.*WebmasterCoffee',
        '^Mozilla/.*woriobot',
        '^Mozilla/.*Yahoo',
        '^Mozilla/.*YandexImages',
        '^Mozilla/.*YioopBot',
        '^Mozilla/.*yolinkBot',
        '^Mozilla/.*YoudaoBot',
        '^Mozilla/.*ZEERCHBOT',
        '^msnbot',
        '^mysmutsearch',
        '^news.me',
        '^newsme',
        '^NextGenSearchBot',
        '^NING',
        'NULL USER AGENT',
        '^Nuzzel',
        '^OpenWebIndex',
        'OutclicksBot',
        '^PagesInventory'
        '^panscient.com',
        '^peerindex',
        '^percbotspider',
        '^PercolateCrawler',
        '^perlclient',
        'PetalBot',
        '^Pingdom',
        '^Pinterest',
        '^PostRank',
        '^psbot',
        '^Python-httplib2',
        '^python-requests',
        '^Python-urllib',
        'Qwantify/'
        '^rbot',
        '^Readability',
        '^Rielee',
        '^RockmeltEmbed',
        '^Ronzoobot',
        '^Ruby',
        '^SaladSpoon',
        '^SAS Web Crawler',
        '^Scope PreviewBot',
        '^Screaming Frog SEO Spider',
        '^Search-Dev',
        '^SemrushBot',
        'Scrapy',
        '^ShortLinkTranslate',
        '^ShowyouBot',
        '^SiteSucker',
        '^SkimBot',
        '^Slurp',
        'SMTBot',
        '^Sogou',
        '^SolomonoBot',
        '^Sosospider',
        '^spider',
        '^spotinfluence',
        '^sqlmap',
        '^squirrobot/',
        '^ssearch_bot',
        '^StatusNet/',
        '^Summify',
        '^Swiftbot',
        '^test',
        '^thumbshots',
        '^TinEye',
        '^TosCrawler',
        '^trovator',
        '^ts_spider',
        '^TurnitinBot',
        '^Twisted',
        '^Twitterbot',
        '^Tweetbot',
        '^UCI IR crawler',
        '^UnwindFetchor',
        '^Updownerbot',
        '^Voyager',
        '^W3C-checklink',
        '^W3C_Validator',
        '^Wada.vn',
        '^Web front page analyser',
        '^Wget',
        '^WinHTTP',
        '^WocBot',
        '^worder',
        '^Wotbox',
        '^wsAnalyzer',
        '^www.integromedb.org',
        '^Xenu Link Sleuth',
        '^Y!J-BRJ/YATS crawler',
        '^yacybot',
        '^Yahoo Pipes',
        '^Yahoo! Slurp China',
        '^Yahoo:LinkExpander',
        '^Yepi/',
        '^Yeti',
        '^yolinkBot',
        'bixo',
        'crawler',
        'ELB-HealthChecker',
        'Exabot',
        'Google Web Preview',
        'Googlebot',
        'Googlebot-Mobile',
        'ichiro/mobile goo;',
        'InsieveBot',
        'larbin',
        'LinkChecker',
        'MS Search',
        'MSIECrawler',
        'naver.com',
        'NewRelicPinger',
        'Nutch',
        'openwebspider.org',
        'org_bot',
        'PycURL',
        'Python',
        'ReverseGet',
        'Robot',
        'search.goo.ne.jp',
        'SeekportBot',
        'SeznamBot',
        'SISTRIX crawler',
        'SiteIntel.net Bot',
        'Slackbot-LinkExpanding',
        'Speedy Spider',
        'Spider',
        'StumbleUpon;',
        'TLSProber',
        'trendictionbot',
        'TwilioProxy',
        'urllib',
        'verticalpigeon.com',
        'VoilaBot',
        'VoilaBotCollector',
        'YamanaLab-Robot',
        'YandexBot',
        'Yeti-Mobile',
        'YodaoBot',
        'Zend_Http_Client',
    ]
    robot_str = "(?i)(?P<robot>" + "|".join(robot_patterns) + ")"
    robot_re = None

# Test Robot with curl -X GET -kH 'User-Agent: Googlebot' https://<hostname>
def is_robot(user_agent):
    if not user_agent:
        return True
    if not RobotValidator.robot_re:
        RobotValidator.robot_re = re.compile(RobotValidator.robot_str)
    return bool(RobotValidator.robot_re.search(user_agent) is not None)


def rate_limit(limit_obj, key, hostname, delta_sec):
    """ Return True if should be rate-limited. Keep attribute on object passed in. """
    attr_name = '%s-%s' % (key, hostname)
    if hasattr(limit_obj, attr_name):
        attr = getattr(limit_obj, attr_name)
        if attr + datetime.timedelta(seconds=delta_sec) > datetime.datetime.now():
            return True
    setattr(limit_obj, attr_name, datetime.datetime.now())
    return False


# Simple memory cache with expiry mechanism. Stores objects in process so no serialization required, but is not distributed over network.
# The application must call purge_cache() as needed by the application to expire keys that haven't been accessed.
class Memcache(dict):
    def set_cache(self, key, value, expiry_sec):
        seconds_old = expiry_sec + random.randint(0, expiry_sec)
        expiry = datetime.datetime.utcnow() + datetime.timedelta(seconds=seconds_old)
        self[key] = (value, expiry)

    def get_cache(self, key):
        cache_obj = self.get(key)
        if cache_obj:
            value, expiry = cache_obj
            if expiry > datetime.datetime.utcnow():
                return value

    def purge_cache(self):
        utcnow = datetime.datetime.utcnow()
        delete_keys = []
        for key, cache_obj in self.items():
            value, expiry = cache_obj
            if expiry <= utcnow:
                delete_keys.append(key)
        for delete_key in delete_keys:
            del self[delete_key]


class TimerObj(object):
    pass

def get_timer(obj=None, debug=False):
    # Optional object that sets the timer on the object given so it doesn't have to crawl the stack each call
    if obj and hasattr(obj, '_timer_obj'):
        return obj._timer_obj
    frame = inspect.currentframe()
    timer_obj = frame.f_locals.get('timer_obj')
    if timer_obj:
        return timer_obj
    f_self = frame.f_locals.get('self')
    while not f_self or not hasattr(f_self, 'timer_obj'):
        frame = frame.f_back
        #if debug:
        #    logw(frame, "FRAME")
        if not frame:
            if debug:
                logging.warning('no frame')
            return None
        if frame.f_locals.get('timer_obj'):
            return frame.f_locals['timer_obj']
        f_self = frame.f_locals.get('self')
        if hasattr(f_self, 'timer_obj'):
            if obj:
                obj._timer_obj = f_self.timer_obj
            return f_self.timer_obj

# Timer System for by-hand tracking _timings on any object
def timer_start(obj, timer_name):
    if not obj:
        return {}
    # Initialize _timers on obj
    if not hasattr(obj, '_timers'):
        setattr(obj, '_timers', {})
    # Don't overwrite if it's already been set
    start_name = '_%s_start_ts' % timer_name
    if not obj._timers.get(start_name):
        obj._timers[start_name] =  time.time()

def timer_stop(obj, timer_name):
    if not obj:
        return {}
    start_name = '_%s_start_ts' % timer_name
    stop_name = '_%s_stop_ts' % timer_name
    exec_name = '_%s_exec_s' % timer_name
    # Don't overwrite if it's already been set, and compute execution time
    if not obj._timers.get(stop_name):
        obj._timers[stop_name] = time.time()
        obj._timers[exec_name] = obj._timers[stop_name] - obj._timers[start_name]

def timer_log(obj, timer_name, do_log=True):
    if not obj:
        return {}
    exec_name = '_%s_exec_s' % timer_name
    exec_t = 1000 * obj._timers[exec_name]
    if do_log:
        logging.debug("%s  %.3f ms" % (timer_name, exec_t))
    return exec_t

def timer_reset(obj, timer_name):
    if not obj:
        return {}
    start_name = '_%s_start_ts' % timer_name
    stop_name = '_%s_stop_ts' % timer_name
    exec_name = '_%s_exec_s' % timer_name
    del obj._timers[start_name]
    del obj._timers[stop_name]
    del obj._timers[exec_name]

def incr_start(obj, timer_name):
    if not obj:
        return {}
    # Initialize _timers on obj
    if not hasattr(obj, '_timers'):
        setattr(obj, '_timers', {})
    # Do overwrite the previous so we can add up the times
    start_name = '_%s_start_ts' % timer_name
    obj._timers[start_name] = time.time()

def incr_stop(obj, timer_name):
    if not obj:
        return {}
    start_name = '_%s_start_ts' % timer_name
    stop_name = '_%s_stop_ts' % timer_name
    exec_name = '_%s_exec_s' % timer_name
    cnt_name = '_%s_cnt' % timer_name
    # Do overwrite the previous so we can add up the times.
    obj._timers[stop_name] = time.time()
    obj._timers.setdefault(exec_name, 0.0)
    obj._timers.setdefault(cnt_name, 0)
    obj._timers[exec_name] += obj._timers[stop_name] - obj._timers[start_name]
    obj._timers[cnt_name] += 1
    return obj._timers[stop_name] - obj._timers[start_name]



# Support for MaxMind's free GeoLite2 database, sign up at https://www.maxmind.com/en/geolite2/signup
# Add geoip2 to setup.py and pip requirements.txt, and set geolite_db_path to the filesystem location of the downloaded db in application config.py
class GeoLite(object):
    geolite_db = None
    geolite_path = None

    def __init__(self, geolite_path):
        if not GeoLite.geolite_path:
            GeoLite.geolite_path = geolite_path

    @classmethod
    def get_ip(cls, ip_addr):
        if not ip_addr:
            return {}
        # Only open the database once, and only as-needed
        if not os.path.exists(cls.geolite_path):
            logging.error("GeoLite db not found: %s" % cls.geolite_path)
            return {}
        # Only import these if not already imported
        import geoip2.database
        import maxminddb
        if not cls.geolite_db:
            cls.geolite_db = geoip2.database.Reader(cls.geolite_path)
        try:
            record = cls.geolite_db.city(ip_addr)
        except geoip2.errors.AddressNotFoundError as ex:
            logging.exception(ex)
            return {}
        except maxminddb.errors.InvalidDatabaseError as ex:
            logging.exception(ex)
            return {}
        geoip = {'continent': record.continent.name, 'country_iso_code': record.country.iso_code, 'country': record.country.name, 'time_zone': record.location.time_zone,
                 'city': record.city.name, 'ip_addr': ip_addr}
        if len(record.subdivisions):
            geoip['region_iso_code'] = record.subdivisions[0].iso_code
            geoip['region'] = record.subdivisions[0].name
        return geoip


def monitor_shell(cmd, timeout=8):
    # Run the monitoring command with 8 second timeout. Monitoring should fail fast.
    try:
        stdout, stderr, exit_status = shell(cmd, timeout=timeout)
    except subprocess.TimeoutExpired as ex:
        logging.exception(ex)
        stdout = ""
        stderr = str(ex)
        exit_status = 1
    # Write it to the db
    import aegis.model
    monitor = {'monitor_host': socket.gethostname(), 'monitor_cmd': cmd, 'monitor_stdout': stdout, 'monitor_stderr': stderr, 'monitor_status': exit_status}
    monitor_id = aegis.model.Monitor.insert_columns(**monitor)
    return exit_status == 0


def submit_mailer(email_type_id, from_addr, to_addr, email_data, dbconn=None):
    from_addr = email.utils.parseaddr(from_addr)
    email_data['from_name'] = from_addr[0]
    from_email = validate_email(from_addr[1])
    to_addr = email.utils.parseaddr(to_addr)
    email_data['to_name'] = to_addr[0]
    to_email = validate_email(to_addr[1])
    # Write it to the db
    import aegis.model
    from_email = aegis.model.Email.set_email(from_email, dbconn=dbconn)
    to_email = aegis.model.Email.set_email(to_email, dbconn=dbconn)
    email_data = json.dumps(email_data, cls=aegis.stdlib.DateTimeEncoder)
    return aegis.model.EmailTracking.insert(email_type_id, from_email['email_id'], to_email['email_id'], email_data, dbconn=dbconn)


version_str = None
def read_version():
    # Set in memory once at startup time
    global version_str
    if version_str:
        return version_str
    try:
        aegis_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
        version_file = os.path.join(aegis_dir, 'version')
        if os.path.exists(version_file):
            fp = open(version_file)
            version_str = fp.read()
        else:
            version_str = '0.0'
        return version_str
    except Exception as ex:
        logging.exception(ex)
        return '0.0'

# Increment minor (z) number up to z_ct (use only 99 or 9) and the major numbers x and y to 10
def incr_version(x, y, z, z_ct=99):
    if z < z_ct:
        return x, y, z+1
    z = 0
    if y < 9:
        return x, y+1, z
    y = 0
    return x+1, y, z

def write_version(version_str):
    # write config files into the build directory and not version control
    aegis_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
    # Write plaintext version file
    version_file = os.path.join(aegis_dir, 'version')
    version = open(version_file, 'w')
    version.write("%s" % version_str)
    version.close()
    # Also write a version.json for external sources to use
    version_file = os.path.join(aegis_dir, 'version.json')
    version_json = open(version_file, 'w')
    version_json.write('{"version": "%s"}\n' % version_str)
    version_json.close()


class DaemonThread(threading.Thread):
    # quitting uses threading.Event() at the class level to synchronize flags between threads
    quitting = threading.Event()
    filename = __file__

    def __init__(self, *args, **kwargs):
        threading.Thread.__init__(self, *args, **kwargs)
        self.start_t = time.time()
        self.record_cnt = 0
        self.last_id = 0

    # Alert and debug hooks likely need to be defined in applications
    def exception_alert(self, ex):
        logw(ex, "EXCEPTION ALERT - OVERRIDE ME IN CHILD CLASS")
        # XXX TODO It could default to channels

    def run(self):
        try:
            self.process()
        except Exception as ex:
            logging.exception(ex)
            self.exception_alert(ex)

    def finish(self):
        end_t = time.time()
        exec_t = end_t - self.start_t
        recs_s = max(float(self.record_cnt), 1.0) / exec_t
        recs_h = max(float(self.record_cnt), 1.0) / exec_t * 3600
        logging.info("%s ending.  Records: %d   Seconds: %4.3f   Records/sec: %4.3f   Records/hr: %4.3f   Last Id: %s", self.name, self.record_cnt, exec_t, recs_s, recs_h, self.last_id)

    def main_thread(self, sleep_sec=3, debug=False):
        # Handling signals only works in the main thread
        signal.signal(signal.SIGINT, self.signal_stop)
        signal.signal(signal.SIGTERM, self.signal_stop)
        signal.signal(signal.SIGHUP, self.signal_stop)
        signal.signal(signal.SIGUSR1, self.signal_debug)
        # Main thread is used only as a control thread... monitors quitting variable, and sleep gets interrupted by signal. And that's it!
        threads, active_threads, daemon_threads = self.get_threads()
        while len(active_threads) > 1:
            if DaemonThread.quitting.is_set():
                logging.warning("DaemonThread waiting %ss for active threads to finish... %s active" % (sleep_sec, len(active_threads)))
                # Callback hook to call the subclass method in the loop, to clean up
                if hasattr(self, 'shutdown'):
                    self.shutdown()
                threads, active_threads, daemon_threads = self.get_threads()
                if debug:
                    logw(len(active_threads), "ACTIVE THREADS")
                    logw(len(daemon_threads), "DAEMON THREADS")
                    for thr in threads:
                        logging.warning("Thread name: %s   is_alive: %s   daemon: %s  [%s]", thr.name, thr.is_alive(), thr.daemon, thr.ident)
                # Join the non-daemon threads, which should be controlled by DaemonThread and subclass.
                if len(active_threads) > 1:
                    for thread in active_threads:
                        if thread.name == 'MainThread' or thread == threading.current_thread():
                            continue
                        logging.warning("Join Thread: %s", thread.name)
                        thread.join(1.0)
            else:
                time.sleep(sleep_sec)

    def get_threads(self):
        threads = threading.enumerate()
        active_threads = [thr for thr in threads if not thr.daemon]
        daemon_threads = [thr for thr in threads if thr.daemon]
        return threads, active_threads, daemon_threads

    @staticmethod
    def signal_stop(signal, frm):
        logging.warning('SIGINT or SIGTERM received (%s). Quitting now...', signal)
        DaemonThread.quitting.set()

    # Debug dump in response to kill -SIGUSR1
    @staticmethod
    def signal_debug(sig, frame):
        """Interrupt running process, and provide a stack trace for each thread. Trigger using kill -SIGUSR1 <pid>"""
        # Show memory usage
        import pympler
        all_objects = pympler.muppy.get_objects()
        summary1 = pympler.summary.summarize(all_objects)
        formatted = pympler.summary.format_(summary1)
        logging.warning("Received SIGUSR1 - Dumping Debug Output" + "\n".join(formatted) + "\n")
        # Dump a stack trace on each thread
        id2name = dict([(th.ident, th.name) for th in threading.enumerate()])
        code = []
        for threadId, stack in sys._current_frames().items():
            code.append("\n# Thread: %s(%d)" % (id2name.get(threadId,""), threadId))
            for filename, lineno, name, line in traceback.extract_stack(stack):
                code.append('File: "%s", line %d, in %s' % (filename, lineno, name))
                if line:
                    code.append("  %s" % (line.strip()))
        logging.warning("\n".join(code))


# In-memory accumulator for usage data, to consolidate data down to the db every few seconds
class Accumulator(dict):
    usage_set = set()

    def incr(self, usage_name, usage_ms):
        # It is possible for two threads to be racing around the accumulator global instantiate of this.
        # So the setdefault checks are more explicit and also the critical section narrowed (but not closed entirely)
        self.setdefault(usage_name, {})
        usage = self[usage_name]
        usage_ms = decimal.Decimal(usage_ms)
        if 'usage_cnt' not in self[usage_name]:
            usage.setdefault('usage_cnt', 0)
        usage['usage_cnt'] += 1
        if 'usage_ms' not in self[usage_name]:
            usage.setdefault('usage_ms', decimal.Decimal('0'))
        usage['usage_ms'] += usage_ms
        if 'usage_ms_min' not in self[usage_name]:
            usage.setdefault('usage_ms_min', decimal.Decimal('0'))
        if not usage['usage_ms_min'] or usage_ms < usage['usage_ms_min']:
            usage['usage_ms_min'] = usage_ms
        if 'usage_ms_max' not in self[usage_name]:
            usage.setdefault('usage_ms_max', decimal.Decimal('0'))
        if usage_ms > usage['usage_ms_max']:
            usage['usage_ms_max'] = usage_ms

# Decorator to put on any function. Records to usage table in the db if configured. Example usage:
#   @aegis.stdlib.usage()
#   def do_something()
use_usage = None
accumulator = Accumulator()
accum_sync = Accumulator()
def usage():
    def wrapper(fn):
        Accumulator.usage_set.add(fn.__qualname__)
        def aegis_stdlib_usage(*args, **kwargs):
            #caller = get_caller()   # XXX experimental
            usage_name = fn.__qualname__
            timer_obj = TimerObj()
            timer_start(timer_obj, usage_name)
            result = fn(*args, **kwargs)
            timer_stop(timer_obj, usage_name)
            usage_ms = timer_log(timer_obj, usage_name, do_log=False)
            timer_reset(timer_obj, usage_name)
            # Trying to connect to the database to record usage. Only works if a database has been configured.
            global use_usage
            global accumulator
            global accum_sync
            import aegis.database
            import aegis.model
            if use_usage is None:
                if aegis.database.pgsql_available:
                    results = aegis.database.db().get("SELECT EXISTS (SELECT 1 FROM pg_tables WHERE schemaname = 'public' AND tablename = 'usage')")
                elif aegis.database.mysql_available:
                    results = aegis.database.db().get("SELECT * FROM information_schema.tables WHERE TABLE_SCHEMA=%s AND TABLE_NAME='usage'", options.mysql_database)
                    results = {'exists': bool(results)}
                use_usage = results['exists']
            # If we're tracking usage, do so in the Accumulator, then sync to db periodically. After sync create a new accumulator.
            if use_usage:
                accumulator.incr(usage_name, usage_ms)
                if not rate_limit(accum_sync, 'sync_to_db', '', delta_sec=5):
                    logging.warning("Syncing Usage to DB")
                    accum = accumulator
                    accumulator = Accumulator()
                    for usage_name, usage in accum.items():
                        aegis.model.Usage.incr_name(usage_name, usage['usage_cnt'], usage['usage_ms'], usage['usage_ms_min'], usage['usage_ms_max'])
            # Return the result of the wrapped function call
            return result
        return aegis_stdlib_usage
    return wrapper
