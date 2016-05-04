# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from sqlalchemy import (Column,
                        Integer,
                        DateTime,
                        ForeignKey
                        )
from sqlalchemy.ext.declarative import declared_attr


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
