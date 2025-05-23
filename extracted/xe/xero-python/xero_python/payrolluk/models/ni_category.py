# coding: utf-8

"""
    Xero Payroll UK

    This is the Xero Payroll API for orgs in the UK region.  # noqa: E501

    Contact: api@xero.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401

from xero_python.models import BaseModel


class NICategory(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        "start_date": "date",
        "ni_category": "NICategoryLetter",
        "ni_category_id": "float",
        "date_first_employed_as_civilian": "date",
        "workplace_postcode": "str",
    }

    attribute_map = {
        "start_date": "startDate",
        "ni_category": "niCategory",
        "ni_category_id": "niCategoryID",
        "date_first_employed_as_civilian": "dateFirstEmployedAsCivilian",
        "workplace_postcode": "workplacePostcode",
    }

    def __init__(
        self,
        start_date=None,
        ni_category=None,
        ni_category_id=None,
        date_first_employed_as_civilian=None,
        workplace_postcode=None,
    ):  # noqa: E501
        """NICategory - a model defined in OpenAPI"""  # noqa: E501

        self._start_date = None
        self._ni_category = None
        self._ni_category_id = None
        self._date_first_employed_as_civilian = None
        self._workplace_postcode = None
        self.discriminator = None

        if start_date is not None:
            self.start_date = start_date
        self.ni_category = ni_category
        if ni_category_id is not None:
            self.ni_category_id = ni_category_id
        if date_first_employed_as_civilian is not None:
            self.date_first_employed_as_civilian = date_first_employed_as_civilian
        self.workplace_postcode = workplace_postcode

    @property
    def start_date(self):
        """Gets the start_date of this NICategory.  # noqa: E501

        The start date of the NI category (YYYY-MM-DD)  # noqa: E501

        :return: The start_date of this NICategory.  # noqa: E501
        :rtype: date
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this NICategory.

        The start date of the NI category (YYYY-MM-DD)  # noqa: E501

        :param start_date: The start_date of this NICategory.  # noqa: E501
        :type: date
        """

        self._start_date = start_date

    @property
    def ni_category(self):
        """Gets the ni_category of this NICategory.  # noqa: E501


        :return: The ni_category of this NICategory.  # noqa: E501
        :rtype: NICategoryLetter
        """
        return self._ni_category

    @ni_category.setter
    def ni_category(self, ni_category):
        """Sets the ni_category of this NICategory.


        :param ni_category: The ni_category of this NICategory.  # noqa: E501
        :type: NICategoryLetter
        """
        if ni_category is None:
            raise ValueError(
                "Invalid value for `ni_category`, must not be `None`"
            )  # noqa: E501

        self._ni_category = ni_category

    @property
    def ni_category_id(self):
        """Gets the ni_category_id of this NICategory.  # noqa: E501

        Xero unique identifier for the NI category  # noqa: E501

        :return: The ni_category_id of this NICategory.  # noqa: E501
        :rtype: float
        """
        return self._ni_category_id

    @ni_category_id.setter
    def ni_category_id(self, ni_category_id):
        """Sets the ni_category_id of this NICategory.

        Xero unique identifier for the NI category  # noqa: E501

        :param ni_category_id: The ni_category_id of this NICategory.  # noqa: E501
        :type: float
        """

        self._ni_category_id = ni_category_id

    @property
    def date_first_employed_as_civilian(self):
        """Gets the date_first_employed_as_civilian of this NICategory.  # noqa: E501

        The date in which the employee was first employed as a civilian (YYYY-MM-DD)  # noqa: E501

        :return: The date_first_employed_as_civilian of this NICategory.  # noqa: E501
        :rtype: date
        """
        return self._date_first_employed_as_civilian

    @date_first_employed_as_civilian.setter
    def date_first_employed_as_civilian(self, date_first_employed_as_civilian):
        """Sets the date_first_employed_as_civilian of this NICategory.

        The date in which the employee was first employed as a civilian (YYYY-MM-DD)  # noqa: E501

        :param date_first_employed_as_civilian: The date_first_employed_as_civilian of this NICategory.  # noqa: E501
        :type: date
        """

        self._date_first_employed_as_civilian = date_first_employed_as_civilian

    @property
    def workplace_postcode(self):
        """Gets the workplace_postcode of this NICategory.  # noqa: E501

        The workplace postcode  # noqa: E501

        :return: The workplace_postcode of this NICategory.  # noqa: E501
        :rtype: str
        """
        return self._workplace_postcode

    @workplace_postcode.setter
    def workplace_postcode(self, workplace_postcode):
        """Sets the workplace_postcode of this NICategory.

        The workplace postcode  # noqa: E501

        :param workplace_postcode: The workplace_postcode of this NICategory.  # noqa: E501
        :type: str
        """
        if workplace_postcode is None:
            raise ValueError(
                "Invalid value for `workplace_postcode`, must not be `None`"
            )  # noqa: E501

        self._workplace_postcode = workplace_postcode
