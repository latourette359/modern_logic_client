# coding: utf-8

"""
    Modern Logic Api

    Manage and version your customer decision logic outside of your codebase  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: info@usemodernlogic.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Customer(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'extra_properties': 'object',
        'customer_id': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'email': 'str',
        'phone': 'str',
        'address_street': 'str',
        'address_street2': 'str',
        'address_city': 'str',
        'address_state_code': 'str',
        'address_zip': 'str',
        'address_country_code': 'str',
        'dob': 'date'
    }

    attribute_map = {
        'extra_properties': 'extraProperties',
        'customer_id': 'customerId',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'email': 'email',
        'phone': 'phone',
        'address_street': 'addressStreet',
        'address_street2': 'addressStreet2',
        'address_city': 'addressCity',
        'address_state_code': 'addressStateCode',
        'address_zip': 'addressZip',
        'address_country_code': 'addressCountryCode',
        'dob': 'dob'
    }

    def __init__(self, extra_properties=None, customer_id=None, first_name=None, last_name=None, email=None, phone=None, address_street=None, address_street2=None, address_city=None, address_state_code=None, address_zip=None, address_country_code=None, dob=None):  # noqa: E501
        """Customer - a model defined in Swagger"""  # noqa: E501
        self._extra_properties = None
        self._customer_id = None
        self._first_name = None
        self._last_name = None
        self._email = None
        self._phone = None
        self._address_street = None
        self._address_street2 = None
        self._address_city = None
        self._address_state_code = None
        self._address_zip = None
        self._address_country_code = None
        self._dob = None
        self.discriminator = None
        if extra_properties is not None:
            self.extra_properties = extra_properties
        if customer_id is not None:
            self.customer_id = customer_id
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if email is not None:
            self.email = email
        if phone is not None:
            self.phone = phone
        if address_street is not None:
            self.address_street = address_street
        if address_street2 is not None:
            self.address_street2 = address_street2
        if address_city is not None:
            self.address_city = address_city
        if address_state_code is not None:
            self.address_state_code = address_state_code
        if address_zip is not None:
            self.address_zip = address_zip
        if address_country_code is not None:
            self.address_country_code = address_country_code
        if dob is not None:
            self.dob = dob

    @property
    def extra_properties(self):
        """Gets the extra_properties of this Customer.  # noqa: E501


        :return: The extra_properties of this Customer.  # noqa: E501
        :rtype: object
        """
        return self._extra_properties

    @extra_properties.setter
    def extra_properties(self, extra_properties):
        """Sets the extra_properties of this Customer.


        :param extra_properties: The extra_properties of this Customer.  # noqa: E501
        :type: object
        """

        self._extra_properties = extra_properties

    @property
    def customer_id(self):
        """Gets the customer_id of this Customer.  # noqa: E501

        Way that you uniquely identify customers  # noqa: E501

        :return: The customer_id of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this Customer.

        Way that you uniquely identify customers  # noqa: E501

        :param customer_id: The customer_id of this Customer.  # noqa: E501
        :type: str
        """

        self._customer_id = customer_id

    @property
    def first_name(self):
        """Gets the first_name of this Customer.  # noqa: E501

        Legal first name of the user being evaluated.  # noqa: E501

        :return: The first_name of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this Customer.

        Legal first name of the user being evaluated.  # noqa: E501

        :param first_name: The first_name of this Customer.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this Customer.  # noqa: E501

        Legal last name (surname) of the user being evaluated.  # noqa: E501

        :return: The last_name of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this Customer.

        Legal last name (surname) of the user being evaluated.  # noqa: E501

        :param last_name: The last_name of this Customer.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this Customer.  # noqa: E501

        Email address provided by user being evaluated.  # noqa: E501

        :return: The email of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Customer.

        Email address provided by user being evaluated.  # noqa: E501

        :param email: The email of this Customer.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def phone(self):
        """Gets the phone of this Customer.  # noqa: E501

        Phone number of user being evaluated.  # noqa: E501

        :return: The phone of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this Customer.

        Phone number of user being evaluated.  # noqa: E501

        :param phone: The phone of this Customer.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def address_street(self):
        """Gets the address_street of this Customer.  # noqa: E501

        Home address of user being evaluated  # noqa: E501

        :return: The address_street of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._address_street

    @address_street.setter
    def address_street(self, address_street):
        """Sets the address_street of this Customer.

        Home address of user being evaluated  # noqa: E501

        :param address_street: The address_street of this Customer.  # noqa: E501
        :type: str
        """

        self._address_street = address_street

    @property
    def address_street2(self):
        """Gets the address_street2 of this Customer.  # noqa: E501


        :return: The address_street2 of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._address_street2

    @address_street2.setter
    def address_street2(self, address_street2):
        """Sets the address_street2 of this Customer.


        :param address_street2: The address_street2 of this Customer.  # noqa: E501
        :type: str
        """

        self._address_street2 = address_street2

    @property
    def address_city(self):
        """Gets the address_city of this Customer.  # noqa: E501


        :return: The address_city of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._address_city

    @address_city.setter
    def address_city(self, address_city):
        """Sets the address_city of this Customer.


        :param address_city: The address_city of this Customer.  # noqa: E501
        :type: str
        """

        self._address_city = address_city

    @property
    def address_state_code(self):
        """Gets the address_state_code of this Customer.  # noqa: E501


        :return: The address_state_code of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._address_state_code

    @address_state_code.setter
    def address_state_code(self, address_state_code):
        """Sets the address_state_code of this Customer.


        :param address_state_code: The address_state_code of this Customer.  # noqa: E501
        :type: str
        """

        self._address_state_code = address_state_code

    @property
    def address_zip(self):
        """Gets the address_zip of this Customer.  # noqa: E501


        :return: The address_zip of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._address_zip

    @address_zip.setter
    def address_zip(self, address_zip):
        """Sets the address_zip of this Customer.


        :param address_zip: The address_zip of this Customer.  # noqa: E501
        :type: str
        """

        self._address_zip = address_zip

    @property
    def address_country_code(self):
        """Gets the address_country_code of this Customer.  # noqa: E501


        :return: The address_country_code of this Customer.  # noqa: E501
        :rtype: str
        """
        return self._address_country_code

    @address_country_code.setter
    def address_country_code(self, address_country_code):
        """Sets the address_country_code of this Customer.


        :param address_country_code: The address_country_code of this Customer.  # noqa: E501
        :type: str
        """

        self._address_country_code = address_country_code

    @property
    def dob(self):
        """Gets the dob of this Customer.  # noqa: E501

        Date of birth for user being evaluated  # noqa: E501

        :return: The dob of this Customer.  # noqa: E501
        :rtype: date
        """
        return self._dob

    @dob.setter
    def dob(self, dob):
        """Sets the dob of this Customer.

        Date of birth for user being evaluated  # noqa: E501

        :param dob: The dob of this Customer.  # noqa: E501
        :type: date
        """

        self._dob = dob

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Customer, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Customer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
