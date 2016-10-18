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


class EnumAddressType(enum.Enum):
    """ It provides PEP-0435 compliant Carepoint Address Type Enumerable """

    business = 1
    home = 2
    school = 3
    vacation = 4
    other = 5
    billing = 6
    shipping = 7


class AddressMixin(object):
    """ This is a mixin for Address Many2Many bindings """

    priority = Column(Integer)
    addr_type_cn = Column(Integer)
    app_flags = Column(Integer)
    timestmp = Column(DateTime)

    @declared_attr
    def addr_id(cls):
        return Column(
            Integer,
            ForeignKey('csaddr.addr_id'),
            primary_key=True,
        )

    @property
    def addr_type(self):
        return EnumAddressType(self.addr_type_cn)
