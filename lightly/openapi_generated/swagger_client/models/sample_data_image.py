# coding: utf-8

"""
    Lightly API

    Lightly.ai enables you to do self-supervised learning in an easy and intuitive way. The lightly.ai OpenAPI spec defines how one can interact with our REST API to unleash the full potential of lightly.ai  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@lightly.ai
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from lightly.openapi_generated.swagger_client.configuration import Configuration


class SampleDataImage(object):
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
        'meta_data': 'SampleMetaData',
        'custom_meta_data': 'CustomSampleMetaData'
    }

    attribute_map = {
        'meta_data': 'metaData',
        'custom_meta_data': 'customMetaData'
    }

    def __init__(self, meta_data=None, custom_meta_data=None, _configuration=None):  # noqa: E501
        """SampleDataImage - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._meta_data = None
        self._custom_meta_data = None
        self.discriminator = None

        if meta_data is not None:
            self.meta_data = meta_data
        if custom_meta_data is not None:
            self.custom_meta_data = custom_meta_data

    @property
    def meta_data(self):
        """Gets the meta_data of this SampleDataImage.  # noqa: E501


        :return: The meta_data of this SampleDataImage.  # noqa: E501
        :rtype: SampleMetaData
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """Sets the meta_data of this SampleDataImage.


        :param meta_data: The meta_data of this SampleDataImage.  # noqa: E501
        :type: SampleMetaData
        """

        self._meta_data = meta_data

    @property
    def custom_meta_data(self):
        """Gets the custom_meta_data of this SampleDataImage.  # noqa: E501


        :return: The custom_meta_data of this SampleDataImage.  # noqa: E501
        :rtype: CustomSampleMetaData
        """
        return self._custom_meta_data

    @custom_meta_data.setter
    def custom_meta_data(self, custom_meta_data):
        """Sets the custom_meta_data of this SampleDataImage.


        :param custom_meta_data: The custom_meta_data of this SampleDataImage.  # noqa: E501
        :type: CustomSampleMetaData
        """

        self._custom_meta_data = custom_meta_data

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
        if issubclass(SampleDataImage, dict):
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
        if not isinstance(other, SampleDataImage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SampleDataImage):
            return True

        return self.to_dict() != other.to_dict()
