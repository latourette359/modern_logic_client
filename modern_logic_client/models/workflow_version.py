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

class WorkflowVersion(object):
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
        'version_number': 'int',
        'name': 'str',
        'publish_date': 'date',
        'is_active': 'bool'
    }

    attribute_map = {
        'version_number': 'versionNumber',
        'name': 'name',
        'publish_date': 'publishDate',
        'is_active': 'isActive'
    }

    def __init__(self, version_number=None, name=None, publish_date=None, is_active=None):  # noqa: E501
        """WorkflowVersion - a model defined in Swagger"""  # noqa: E501
        self._version_number = None
        self._name = None
        self._publish_date = None
        self._is_active = None
        self.discriminator = None
        if version_number is not None:
            self.version_number = version_number
        if name is not None:
            self.name = name
        if publish_date is not None:
            self.publish_date = publish_date
        if is_active is not None:
            self.is_active = is_active

    @property
    def version_number(self):
        """Gets the version_number of this WorkflowVersion.  # noqa: E501


        :return: The version_number of this WorkflowVersion.  # noqa: E501
        :rtype: int
        """
        return self._version_number

    @version_number.setter
    def version_number(self, version_number):
        """Sets the version_number of this WorkflowVersion.


        :param version_number: The version_number of this WorkflowVersion.  # noqa: E501
        :type: int
        """

        self._version_number = version_number

    @property
    def name(self):
        """Gets the name of this WorkflowVersion.  # noqa: E501


        :return: The name of this WorkflowVersion.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkflowVersion.


        :param name: The name of this WorkflowVersion.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def publish_date(self):
        """Gets the publish_date of this WorkflowVersion.  # noqa: E501


        :return: The publish_date of this WorkflowVersion.  # noqa: E501
        :rtype: date
        """
        return self._publish_date

    @publish_date.setter
    def publish_date(self, publish_date):
        """Sets the publish_date of this WorkflowVersion.


        :param publish_date: The publish_date of this WorkflowVersion.  # noqa: E501
        :type: date
        """

        self._publish_date = publish_date

    @property
    def is_active(self):
        """Gets the is_active of this WorkflowVersion.  # noqa: E501


        :return: The is_active of this WorkflowVersion.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this WorkflowVersion.


        :param is_active: The is_active of this WorkflowVersion.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

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
        if issubclass(WorkflowVersion, dict):
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
        if not isinstance(other, WorkflowVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other