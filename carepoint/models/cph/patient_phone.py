# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from carepoint.models.phone_mixin import PhoneMixin
from sqlalchemy import (Column,
                        Integer,
                        )


class PatientPhone(PhoneMixin, Carepoint.BASE):
    __dbname__ = 'cph'
    __tablename__ = 'cppat_phone'
    pat_id = Column(
        Integer, 
        primary_key=True,
        autoincrement=False,
    )
