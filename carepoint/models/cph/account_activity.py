# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        Integer,
                        Numeric,
                        ForeignKey,
                        DateTime,
                        String,
                        )


class AccountActivity(Carepoint.BASE):
    __tablename__ = 'CsSArActivity'
    __dbname__ = 'cph'

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=False,
    )
    acct_id = Column(
        Integer,
        ForeignKey('cp_acct.ID'),
    )
    order_id = Column(
        Integer,
        ForeignKey('CsOm.order_id'),
    )
    pat_id = Column(
        Integer,
        ForeignKey('cppat.pat_id'),
    )
    rxdisp_id = Column(
        Integer,
        ForeignKey('cprx_disp.rxdisp_id'),
    )
    org_id = Column(
        Integer,
        ForeignKey('csorg.org_id'),
    )
    orig_org_id = Column(
        Integer,
        ForeignKey('csorg.org_id'),
    )
    item_id = Column(
        Integer,
        ForeignKey('item.item_id'),
    )
    descr = Column(String)
    refno = Column(String)
    ct_id = Column(Integer)
    code_num = Column(Integer)
    amt = Column(Numeric)
    reason_cn = Column(Integer)
    rpt_cat = Column(Integer)
    qty = Column(Numeric)
    tax = Column(Numeric)
    nonrx_order_line_id = Column(Integer)
    store_id = Column(
        Integer,
        ForeignKey('csstore.store_id'),
    )
    batch_id = Column(Integer)
    batch_no = Column(String)
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
