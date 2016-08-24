# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        DateTime,
                        Numeric,
                        String,
                        )


class FdbPrice(Carepoint.BASE):
    __tablename__ = 'fdrnp_inc'
    __dbname__ = 'cph'

    ndc = Column(String, primary_key=True)
    npt_type = Column(String, primary_key=True)
    npt_datec = Column(DateTime, primary_key=True)
    npt_price = Column(Numeric)
