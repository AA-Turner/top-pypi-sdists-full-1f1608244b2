import base64
import datetime as dt

from slixmpp.util import bytes
from slixmpp.xmlstream import ElementBase, ET, register_stanza_plugin, JID
from slixmpp.plugins import xep_0082


class VCardTemp(ElementBase):
    name = 'vCard'
    namespace = 'vcard-temp'
    plugin_attrib = 'vcard_temp'
    interfaces = {'FN', 'VERSION'}
    sub_interfaces = {'FN', 'VERSION'}


class Name(ElementBase):
    name = 'N'
    namespace = 'vcard-temp'
    plugin_attrib = name
    interfaces = {'FAMILY', 'GIVEN', 'MIDDLE', 'PREFIX', 'SUFFIX'}
    sub_interfaces = interfaces

    def _set_component(self, name, value):
        if isinstance(value, list):
            value = ','.join(value)
        if value is not None:
            self._set_sub_text(name, value, keep=True)
        else:
            self._del_sub(name)

    def _get_component(self, name):
        value = self._get_sub_text(name, '')
        if ',' in value:
            value = [v.strip() for v in value.split(',')]
        return value

    def set_family(self, value):
        self._set_component('FAMILY', value)

    def get_family(self):
        return self._get_component('FAMILY')

    def set_given(self, value):
        self._set_component('GIVEN', value)

    def get_given(self):
        return self._get_component('GIVEN')

    def set_middle(self, value):
        print(value)
        self._set_component('MIDDLE', value)

    def get_middle(self):
        return self._get_component('MIDDLE')

    def set_prefix(self, value):
        self._set_component('PREFIX', value)

    def get_prefix(self):
        return self._get_component('PREFIX')

    def set_suffix(self, value):
        self._set_component('SUFFIX', value)

    def get_suffix(self):
        return self._get_component('SUFFIX')


class Nickname(ElementBase):
    name = 'NICKNAME'
    namespace = 'vcard-temp'
    plugin_attrib = name
    plugin_multi_attrib = 'nicknames'
    interfaces = {name}
    is_extension = True

    def set_nickname(self, value):
        if not value:
            self.xml.text = ''
            return

        if not isinstance(value, list):
            value = [value]

        self.xml.text = ','.join(value)

    def get_nickname(self):
        if self.xml.text:
            return self.xml.text.split(',')


class Email(ElementBase):
    name = 'EMAIL'
    namespace = 'vcard-temp'
    plugin_attrib = name
    plugin_multi_attrib = 'emails'
    interfaces = {'HOME', 'WORK', 'INTERNET', 'PREF', 'X400', 'USERID'}
    sub_interfaces = {'USERID'}
    bool_interfaces = {'HOME', 'WORK', 'INTERNET', 'PREF', 'X400'}


class Address(ElementBase):
    name = 'ADR'
    namespace = 'vcard-temp'
    plugin_attrib = name
    plugin_multi_attrib = 'addresses'
    interfaces = {'HOME', 'WORK', 'POSTAL', 'PARCEL', 'DOM', 'INTL',
                  'PREF', 'POBOX', 'EXTADD', 'STREET', 'LOCALITY',
                  'REGION', 'PCODE', 'CTRY'}
    sub_interfaces = {'POBOX', 'EXTADD', 'STREET', 'LOCALITY',
                      'REGION', 'PCODE', 'CTRY'}
    bool_interfaces = {'HOME', 'WORK', 'DOM', 'INTL', 'PREF'}


class Telephone(ElementBase):
    name = 'TEL'
    namespace = 'vcard-temp'
    plugin_attrib = name
    plugin_multi_attrib = 'telephone_numbers'
    interfaces = {'HOME', 'WORK', 'VOICE', 'FAX', 'PAGER', 'MSG',
                  'CELL', 'VIDEO', 'BBS', 'MODEM', 'ISDN', 'PCS',
                  'PREF', 'NUMBER'}
    sub_interfaces = {'NUMBER'}
    bool_interfaces = {'HOME', 'WORK', 'VOICE', 'FAX', 'PAGER',
                       'MSG', 'CELL', 'VIDEO', 'BBS', 'MODEM',
                       'ISDN', 'PCS', 'PREF'}

    def setup(self, xml=None):
        super().setup(xml=xml)
        ## this blanks out numbers received from server
        ##self._set_sub_text('NUMBER', '', keep=True)

    def set_number(self, value):
        self._set_sub_text('NUMBER', value, keep=True)

    def del_number(self):
        self._set_sub_text('NUMBER', '', keep=True)


class Label(ElementBase):
    name = 'LABEL'
    namespace = 'vcard-temp'
    plugin_attrib = name
    plugin_multi_attrib = 'labels'
    interfaces = {'HOME', 'WORK', 'POSTAL', 'PARCEL', 'DOM', 'INT',
                  'PREF', 'lines'}
    bool_interfaces = {'HOME', 'WORK', 'POSTAL', 'PARCEL', 'DOM',
                       'INT', 'PREF'}

    def add_line(self, value):
        line = ET.Element('{%s}LINE' % self.namespace)
        line.text = value
        self.xml.append(line)

    def get_lines(self):
        lines = self.xml.find('{%s}LINE' % self.namespace)
        if lines is None:
            return []
        return [line.text for line in lines]

    def set_lines(self, values):
        self.del_lines()
        for line in values:
            self.add_line(line)

    def del_lines(self):
        lines = self.xml.find('{%s}LINE' % self.namespace)
        if lines is None:
            return
        for line in lines:
            self.xml.remove(line)


class Geo(ElementBase):
    name = 'GEO'
    namespace = 'vcard-temp'
    plugin_attrib = name
    plugin_multi_attrib = 'geolocations'
    interfaces = {'LAT', 'LON'}
    sub_interfaces = interfaces


class Org(ElementBase):
    name = 'ORG'
    namespace = 'vcard-temp'
    plugin_attrib = name
    plugin_multi_attrib = 'organizations'
    interfaces = {'ORGNAME', 'ORGUNIT', 'orgunits'}
    sub_interfaces = {'ORGNAME', 'ORGUNIT'}

    def add_orgunit(self, value):
        orgunit = ET.Element('{%s}ORGUNIT' % self.namespace)
        orgunit.text = value
        self.xml.append(orgunit)

    def get_orgunits(self):
        orgunits = self.xml.find('{%s}ORGUNIT' % self.namespace)
        if orgunits is None:
            return []
        return [orgunit.text for orgunit in orgunits]

    def set_orgunits(self, values):
        self.del_orgunits()
        for orgunit in values:
            self.add_orgunit(orgunit)

    def del_orgunits(self):
        orgunits = self.xml.find('{%s}ORGUNIT' % self.namespace)
        if orgunits is None:
            return
        for orgunit in orgunits:
            self.xml.remove(orgunit)


class Photo(ElementBase):
    name = 'PHOTO'
    namespace = 'vcard-temp'
    plugin_attrib = name
    plugin_multi_attrib = 'photos'
    interfaces = {'TYPE', 'EXTVAL'}
    sub_interfaces = interfaces


class Logo(ElementBase):
    name = 'LOGO'
    namespace = 'vcard-temp'
    plugin_attrib = name
    plugin_multi_attrib = 'logos'
    interfaces = {'TYPE', 'EXTVAL'}
    sub_interfaces = interfaces


class Sound(ElementBase):
    name = 'SOUND'
    namespace = 'vcard-temp'
    plugin_attrib = name
    plugin_multi_attrib = 'sounds'
    interfaces = {'PHONETC', 'EXTVAL'}
    sub_interfaces = interfaces


class BinVal(ElementBase):
    name = 'BINVAL'
    namespace = 'vcard-temp'
    plugin_attrib = name
    interfaces = {'BINVAL'}
    is_extension = True

    def setup(self, xml=None):
        self.xml = ET.Element('')
        return True

    def set_binval(self, value):
        self.del_binval()
        parent = self.parent()
        if value:
            xml = ET.Element('{%s}BINVAL' % self.namespace)
            xml.text = bytes(base64.b64encode(value)).decode('utf-8')
            parent.append(xml)

    def get_binval(self):
        parent = self.parent()
        xml = parent.xml.find('{%s}BINVAL' % self.namespace)
        if xml is not None:
            return base64.b64decode(bytes(xml.text))
        return b''

    def del_binval(self):
        self.parent()._del_sub('{%s}BINVAL' % self.namespace)


class Classification(ElementBase):
    name = 'CLASS'
    namespace = 'vcard-temp'
    plugin_attrib = name
    plugin_multi_attrib = 'classifications'
    interfaces = {'PUBLIC', 'PRIVATE', 'CONFIDENTIAL'}
    bool_interfaces = interfaces


class Categories(ElementBase):
    name = 'CATEGORIES'
    namespace = 'vcard-temp'
    plugin_attrib = name
    plugin_multi_attrib = 'categories'
    interfaces = {name}
    is_extension = True

    def set_categories(self, values):
        self.del_categories()
        for keyword in values:
            item = ET.Element('{%s}KEYWORD' % self.namespace)
            item.text = keyword
            self.xml.append(item)

    def get_categories(self):
        items = self.xml.findall('{%s}KEYWORD' % self.namespace)
        if items is None:
            return []
        keywords = []
        for item in items:
            keywords.append(item.text)
        return keywords

    def del_categories(self):
        items = self.xml.findall('{%s}KEYWORD' % self.namespace)
        for item in items:
            self.xml.remove(item)


class Birthday(ElementBase):
    name = 'BDAY'
    namespace = 'vcard-temp'
    plugin_attrib = name
    plugin_multi_attrib = 'birthdays'
    interfaces = {name}
    is_extension = True

    def set_bday(self, value):
        if isinstance(value, dt.datetime):
            value = xep_0082.format_datetime(value)
        self.xml.text = value

    def get_bday(self):
        if not self.xml.text:
            return None
        try:
            return xep_0082.parse(self.xml.text)
        except ValueError:
            return self.xml.text


class Rev(ElementBase):
    name = 'REV'
    namespace = 'vcard-temp'
    plugin_attrib = name
    plugin_multi_attrib = 'revision_dates'
    interfaces = {name}
    is_extension = True

    def set_rev(self, value):
        if isinstance(value, dt.datetime):
            value = xep_0082.format_datetime(value)
        self.xml.text = value

    def get_rev(self):
        if not self.xml.text:
            return None
        try:
            return xep_0082.parse(self.xml.text)
        except ValueError:
            return self.xml.text


class Title(ElementBase):
    name = 'TITLE'
    namespace = 'vcard-temp'
    plugin_attrib = name
    plugin_multi_attrib = 'titles'
    interfaces = {name}
    is_extension = True

    def set_title(self, value):
        self.xml.text = value

    def get_title(self):
        return self.xml.text


class Role(ElementBase):
    name = 'ROLE'
    namespace = 'vcard-temp'
    plugin_attrib = name
    plugin_multi_attrib = 'roles'
    interfaces = {name}
    is_extension = True

    def set_role(self, value):
        self.xml.text = value

    def get_role(self):
        return self.xml.text


class Note(ElementBase):
    name = 'NOTE'
    namespace = 'vcard-temp'
    plugin_attrib = name
    plugin_multi_attrib = 'notes'
    interfaces = {name}
    is_extension = True

    def set_note(self, value):
        self.xml.text = value

    def get_note(self):
        return self.xml.text


class Desc(ElementBase):
    name = 'DESC'
    namespace = 'vcard-temp'
    plugin_attrib = name
    plugin_multi_attrib = 'descriptions'
    interfaces = {name}
    is_extension = True

    def set_desc(self, value):
        self.xml.text = value

    def get_desc(self):
        return self.xml.text


class URL(ElementBase):
    name = 'URL'
    namespace = 'vcard-temp'
    plugin_attrib = name
    plugin_multi_attrib = 'urls'
    interfaces = {name}
    is_extension = True

    def set_url(self, value):
        self.xml.text = value

    def get_url(self):
        return self.xml.text


class UID(ElementBase):
    name = 'UID'
    namespace = 'vcard-temp'
    plugin_attrib = name
    plugin_multi_attrib = 'uids'
    interfaces = {name}
    is_extension = True

    def set_uid(self, value):
        self.xml.text = value

    def get_uid(self):
        return self.xml.text


class ProdID(ElementBase):
    name = 'PRODID'
    namespace = 'vcard-temp'
    plugin_attrib = name
    plugin_multi_attrib = 'product_ids'
    interfaces = {name}
    is_extension = True

    def set_prodid(self, value):
        self.xml.text = value

    def get_prodid(self):
        return self.xml.text


class Mailer(ElementBase):
    name = 'MAILER'
    namespace = 'vcard-temp'
    plugin_attrib = name
    plugin_multi_attrib = 'mailers'
    interfaces = {name}
    is_extension = True

    def set_mailer(self, value):
        self.xml.text = value

    def get_mailer(self):
        return self.xml.text


class SortString(ElementBase):
    name = 'SORT-STRING'
    namespace = 'vcard-temp'
    plugin_attrib = 'SORT_STRING'
    plugin_multi_attrib = 'sort_strings'
    interfaces = {name}
    is_extension = True

    def set_sort_string(self, value):
        self.xml.text = value

    def get_sort_string(self):
        return self.xml.text


class Agent(ElementBase):
    name = 'AGENT'
    namespace = 'vcard-temp'
    plugin_attrib = name
    plugin_multi_attrib = 'agents'
    interfaces = {'EXTVAL'}
    sub_interfaces = interfaces


class JabberID(ElementBase):
    name = 'JABBERID'
    namespace = 'vcard-temp'
    plugin_attrib = name
    plugin_multi_attrib = 'jids'
    interfaces = {name}
    is_extension = True

    def set_jabberid(self, value):
        self.xml.text = JID(value).bare

    def get_jabberid(self):
        return JID(self.xml.text)


class TimeZone(ElementBase):
    name = 'TZ'
    namespace = 'vcard-temp'
    plugin_attrib = name
    plugin_multi_attrib = 'timezones'
    interfaces = {name}
    is_extension = True

    def set_tz(self, value):
        time = xep_0082.time(offset=value)
        if time[-1] == 'Z':
            self.xml.text = 'Z'
        else:
            self.xml.text = time[-6:]

    def get_tz(self):
        if not self.xml.text:
            return dt.timezone.utc
        try:
            time = xep_0082.parse('00:00:00%s' % self.xml.text)
            return time.tzinfo
        except ValueError:
            return self.xml.text


register_stanza_plugin(VCardTemp, Name)
register_stanza_plugin(VCardTemp, Address, iterable=True)
register_stanza_plugin(VCardTemp, Agent, iterable=True)
register_stanza_plugin(VCardTemp, Birthday, iterable=True)
register_stanza_plugin(VCardTemp, Categories, iterable=True)
register_stanza_plugin(VCardTemp, Desc, iterable=True)
register_stanza_plugin(VCardTemp, Email, iterable=True)
register_stanza_plugin(VCardTemp, Geo, iterable=True)
register_stanza_plugin(VCardTemp, JabberID, iterable=True)
register_stanza_plugin(VCardTemp, Label, iterable=True)
register_stanza_plugin(VCardTemp, Logo, iterable=True)
register_stanza_plugin(VCardTemp, Mailer, iterable=True)
register_stanza_plugin(VCardTemp, Note, iterable=True)
register_stanza_plugin(VCardTemp, Nickname, iterable=True)
register_stanza_plugin(VCardTemp, Org, iterable=True)
register_stanza_plugin(VCardTemp, Photo, iterable=True)
register_stanza_plugin(VCardTemp, ProdID, iterable=True)
register_stanza_plugin(VCardTemp, Rev, iterable=True)
register_stanza_plugin(VCardTemp, Role, iterable=True)
register_stanza_plugin(VCardTemp, SortString, iterable=True)
register_stanza_plugin(VCardTemp, Sound, iterable=True)
register_stanza_plugin(VCardTemp, Telephone, iterable=True)
register_stanza_plugin(VCardTemp, Title, iterable=True)
register_stanza_plugin(VCardTemp, TimeZone, iterable=True)
register_stanza_plugin(VCardTemp, UID, iterable=True)
register_stanza_plugin(VCardTemp, URL, iterable=True)

register_stanza_plugin(Photo, BinVal)
register_stanza_plugin(Logo, BinVal)
register_stanza_plugin(Sound, BinVal)

register_stanza_plugin(Agent, VCardTemp)
