# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        DateTime,
                        Boolean,
                        String,
                        )


class FdbPriceType(Carepoint.BASE):
    __tablename__ = 'fdrnptypd'
    __dbname__ = 'cph'

    npt_type = Column(String, primary_key=True)
    npt_desc = Column(DateTime)
    update_yn = Column(Boolean)
