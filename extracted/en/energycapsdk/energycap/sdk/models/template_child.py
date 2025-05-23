# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class TemplateChild(Model):
    """TemplateChild.

    :param template_id:
    :type template_id: int
    :param template_code:
    :type template_code: str
    :param template_info:
    :type template_info: str
    """

    _attribute_map = {
        'template_id': {'key': 'templateId', 'type': 'int'},
        'template_code': {'key': 'templateCode', 'type': 'str'},
        'template_info': {'key': 'templateInfo', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(TemplateChild, self).__init__(**kwargs)
        self.template_id = kwargs.get('template_id', None)
        self.template_code = kwargs.get('template_code', None)
        self.template_info = kwargs.get('template_info', None)
