# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from sqlalchemy.types import Enum
from sqlalchemy import (Column,
                        Integer,
                        String
                        )

from carepoint.models.state import EnumOrderState


class OrderStatus(Carepoint.BASE):
    __tablename__ = 'CsOmStatus'
    __dbname__ = 'cph'

    OmStatus = Column(
        Integer, 
        primary_key=True,
        autoincrement=False,
    )
    state_cn = Column(
        Integer,
    )
    descr = Column(String)

    @property
    def state(self):
        return EnumOrderState(self.state_cn)
