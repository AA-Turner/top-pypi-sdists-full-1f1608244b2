# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class FormTemplateChild(Model):
    """FormTemplateChild.

    :param form_template_id:
    :type form_template_id: int
    :param display_order:
    :type display_order: int
    :param template:
    :type template: ~energycap.sdk.models.TemplateChild
    :param begin_date:
    :type begin_date: datetime
    :param end_date:
    :type end_date: datetime
    """

    _attribute_map = {
        'form_template_id': {'key': 'formTemplateId', 'type': 'int'},
        'display_order': {'key': 'displayOrder', 'type': 'int'},
        'template': {'key': 'template', 'type': 'TemplateChild'},
        'begin_date': {'key': 'beginDate', 'type': 'iso-8601'},
        'end_date': {'key': 'endDate', 'type': 'iso-8601'},
    }

    def __init__(self, *, form_template_id: int=None, display_order: int=None, template=None, begin_date=None, end_date=None, **kwargs) -> None:
        super(FormTemplateChild, self).__init__(**kwargs)
        self.form_template_id = form_template_id
        self.display_order = display_order
        self.template = template
        self.begin_date = begin_date
        self.end_date = end_date
