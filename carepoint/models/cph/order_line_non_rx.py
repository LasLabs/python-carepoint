# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        Integer,
                        String,
                        DateTime,
                        ForeignKey,
                        Numeric,
                        )


class OrderLineNonRx(Carepoint.BASE):
    __tablename__ = 'CsOmNonRxLine'
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
    org_id = Column(
        Integer,
        ForeignKey('csorg.org_id'),
    )
    pat_id = Column(
        Integer,
        ForeignKey('cppat.pat_id'),
    )
    item_id = Column(
        Integer,
        ForeignKey('item.item_id'),
    )
    descr = Column(String)
    qty = Column(Numeric)
    unit_amt = Column(Numeric)
    tax = Column(Numeric)
    rxdisp_id = Column(
        Integer,
        ForeignKey('cprx_disp.rxdisp_id'),
    )
    rxdisp_id = Column(
        Integer,
        ForeignKey('cprx_disp.rxdisp_id'),
    )
    replace_rxdisp_id = Column(
        Integer,
        ForeignKey('cprx_disp.rxdisp_id'),
    )
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
