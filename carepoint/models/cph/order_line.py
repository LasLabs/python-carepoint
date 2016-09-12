# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        Integer,
                        Boolean,
                        DateTime,
                        ForeignKey,
                        )


class OrderLine(Carepoint.BASE):
    __tablename__ = 'CsOmLine'
    __dbname__ = 'cph'

    line_id = Column(
        Integer, 
        primary_key=True,
        autoincrement=False,
    )
    order_id = Column(
        Integer,
        ForeignKey('CsOm.order_id'),
    )
    rx_id = Column(
        Integer,
        ForeignKey('cprx.rx_id'),
    )
    rxdisp_id = Column(
        Integer,
        ForeignKey('cprx_disp.rxdisp_id'),
    )
    line_state_cn = Column(Integer)
    line_status_cn = Column(Integer)
    hold_yn = Column(Boolean)
    add_user_id = Column(
        Integer,
        ForeignKey('csuser.user_id'),
    )
    add_date = Column(DateTime)
    chg_user_id = Column(
        Integer,
        ForeignKey('csuser.user_id'),
    )
    chg_date = Column(DateTime)
