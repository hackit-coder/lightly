# coding: utf-8

"""
    Lightly API

    Lightly.ai enables you to do self-supervised learning in an easy and intuitive way. The lightly.ai OpenAPI spec defines how one can interact with our REST API to unleash the full potential of lightly.ai  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@lightly.ai
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from enum import Enum
from aenum import no_arg  # type: ignore


try:
    # Pydantic >=v1.10.17
    
    pass # Add pass to avoid empty try/except if no imports are generated for this file.
except ImportError:
    # Pydantic v1
    
    pass # Add pass to avoid empty try/except if no imports are generated for this file.


class Sector(str, Enum):
    """
    Sector
    """

    """
    allowed enum values
    """
    ADVERTISING = 'ADVERTISING'
    AGRICULTURE = 'AGRICULTURE'
    AUTOMOTIVE = 'AUTOMOTIVE'
    EDUCATION = 'EDUCATION'
    ENERGY = 'ENERGY'
    ENTERTAINMENT = 'ENTERTAINMENT'
    ENVIRONMENTAL = 'ENVIRONMENTAL'
    FINANCE = 'FINANCE'
    FOOD = 'FOOD'
    HEALTHCARE = 'HEALTHCARE'
    INTERNET_OF_THINGS = 'INTERNET_OF_THINGS'
    LOGISTICS = 'LOGISTICS'
    MACHINE_LEARNING = 'MACHINE_LEARNING'
    MANUFACTURING = 'MANUFACTURING'
    MEDICINE = 'MEDICINE'
    RECYCLING = 'RECYCLING'
    RETAIL = 'RETAIL'
    ROBOTICS = 'ROBOTICS'
    SECURITY = 'SECURITY'
    SOFTWARE_DEVELOPMENT = 'SOFTWARE_DEVELOPMENT'
    SPORTS = 'SPORTS'
    SURVEILLANCE = 'SURVEILLANCE'
    TRANSPORTATION = 'TRANSPORTATION'
    OTHER = 'OTHER'

    @classmethod
    def from_json(cls, json_str: str) -> 'Sector':
        """Create an instance of Sector from a JSON string"""
        return Sector(json.loads(json_str))


