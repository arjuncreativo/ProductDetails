# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Price(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, value: float=None, currency_code: str=None):  # noqa: E501
        """Price - a model defined in Swagger

        :param value: The value of this Price.  # noqa: E501
        :type value: float
        :param currency_code: The currency_code of this Price.  # noqa: E501
        :type currency_code: str
        """
        self.swagger_types = {
            'value': float,
            'currency_code': str
        }

        self.attribute_map = {
            'value': 'value',
            'currency_code': 'currency_code'
        }

        self._value = value
        self._currency_code = currency_code

    @classmethod
    def from_dict(cls, dikt) -> 'Price':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Price of this Price.  # noqa: E501
        :rtype: Price
        """
        return util.deserialize_model(dikt, cls)

    @property
    def value(self) -> float:
        """Gets the value of this Price.


        :return: The value of this Price.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value: float):
        """Sets the value of this Price.


        :param value: The value of this Price.
        :type value: float
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def currency_code(self) -> str:
        """Gets the currency_code of this Price.


        :return: The currency_code of this Price.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code: str):
        """Sets the currency_code of this Price.


        :param currency_code: The currency_code of this Price.
        :type currency_code: str
        """
        if currency_code is None:
            raise ValueError("Invalid value for `currency_code`, must not be `None`")  # noqa: E501

        self._currency_code = currency_code
