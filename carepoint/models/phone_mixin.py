# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import enum

from sqlalchemy import (Column,
                        Integer,
                        DateTime,
                        ForeignKey,
                        )
from sqlalchemy.types import Enum
from sqlalchemy.ext.declarative import declared_attr


class EnumPhoneType(enum.Enum):
    """ It provides PEP-0435 compliant Carepoint Phone Type Enumerable """

    assistant = 1
    business = 2
    business_2 = 3
    business_fax = 4
    car = 5
    home = 6
    home_2 = 7
    home_fax = 8
    mobile = 9
    beeper = 10
    other_fax = 11


class PhoneMixin(object):
    """ This is a mixin for Phone Many2Many bindings """

    priority = Column(Integer)
    phone_type_cn = Column(Integer)
    app_flags = Column(Integer)
    timestmp = Column(DateTime)

    @declared_attr
    def phone_id(cls):
        return Column(
            Integer,
            ForeignKey('csphone.phone_id'),
            primary_key=True,
        )

    @property
    def phone_type(self):
        return EnumPhoneType(self.phone_type_cn)
