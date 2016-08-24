# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from sqlalchemy import (Column,
                        Integer,
                        DateTime,
                        ForeignKey
                        )
from sqlalchemy.ext.declarative import declared_attr


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
