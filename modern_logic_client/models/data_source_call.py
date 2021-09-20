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

class DataSourceCall(object):
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
        'id': 'int',
        'execution_id': 'int',
        'data_source_id': 'int',
        'request': 'object',
        'response': 'object',
        'date_time_of_call': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'execution_id': 'executionId',
        'data_source_id': 'dataSourceId',
        'request': 'request',
        'response': 'response',
        'date_time_of_call': 'dateTimeOfCall'
    }

    def __init__(self, id=None, execution_id=None, data_source_id=None, request=None, response=None, date_time_of_call=None):  # noqa: E501
        """DataSourceCall - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._execution_id = None
        self._data_source_id = None
        self._request = None
        self._response = None
        self._date_time_of_call = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if execution_id is not None:
            self.execution_id = execution_id
        if data_source_id is not None:
            self.data_source_id = data_source_id
        if request is not None:
            self.request = request
        if response is not None:
            self.response = response
        if date_time_of_call is not None:
            self.date_time_of_call = date_time_of_call

    @property
    def id(self):
        """Gets the id of this DataSourceCall.  # noqa: E501


        :return: The id of this DataSourceCall.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DataSourceCall.


        :param id: The id of this DataSourceCall.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def execution_id(self):
        """Gets the execution_id of this DataSourceCall.  # noqa: E501


        :return: The execution_id of this DataSourceCall.  # noqa: E501
        :rtype: int
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        """Sets the execution_id of this DataSourceCall.


        :param execution_id: The execution_id of this DataSourceCall.  # noqa: E501
        :type: int
        """

        self._execution_id = execution_id

    @property
    def data_source_id(self):
        """Gets the data_source_id of this DataSourceCall.  # noqa: E501


        :return: The data_source_id of this DataSourceCall.  # noqa: E501
        :rtype: int
        """
        return self._data_source_id

    @data_source_id.setter
    def data_source_id(self, data_source_id):
        """Sets the data_source_id of this DataSourceCall.


        :param data_source_id: The data_source_id of this DataSourceCall.  # noqa: E501
        :type: int
        """

        self._data_source_id = data_source_id

    @property
    def request(self):
        """Gets the request of this DataSourceCall.  # noqa: E501


        :return: The request of this DataSourceCall.  # noqa: E501
        :rtype: object
        """
        return self._request

    @request.setter
    def request(self, request):
        """Sets the request of this DataSourceCall.


        :param request: The request of this DataSourceCall.  # noqa: E501
        :type: object
        """

        self._request = request

    @property
    def response(self):
        """Gets the response of this DataSourceCall.  # noqa: E501


        :return: The response of this DataSourceCall.  # noqa: E501
        :rtype: object
        """
        return self._response

    @response.setter
    def response(self, response):
        """Sets the response of this DataSourceCall.


        :param response: The response of this DataSourceCall.  # noqa: E501
        :type: object
        """

        self._response = response

    @property
    def date_time_of_call(self):
        """Gets the date_time_of_call of this DataSourceCall.  # noqa: E501


        :return: The date_time_of_call of this DataSourceCall.  # noqa: E501
        :rtype: datetime
        """
        return self._date_time_of_call

    @date_time_of_call.setter
    def date_time_of_call(self, date_time_of_call):
        """Sets the date_time_of_call of this DataSourceCall.


        :param date_time_of_call: The date_time_of_call of this DataSourceCall.  # noqa: E501
        :type: datetime
        """

        self._date_time_of_call = date_time_of_call

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
        if issubclass(DataSourceCall, dict):
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
        if not isinstance(other, DataSourceCall):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
