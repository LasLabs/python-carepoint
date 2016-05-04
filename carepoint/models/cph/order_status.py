# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        Integer,
                        String,
                        )


class OrderStatus(Carepoint.BASE):
    __tablename__ = 'CsOmStatus'
    __dbname__ = 'cph'

    OmStatus = Column(Integer, primary_key=True)
    state_cn = Column(Integer)
    descr = Column(String)
