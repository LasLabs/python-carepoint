# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        Integer,
                        String,
                        DateTime,
                        ForeignKey,
                        Boolean,
                        Float,
                        )


class Order(Carepoint.BASE):
    __tablename__ = 'CsOm'
    __dbname__ = 'cph'

    order_id = Column(Integer, primary_key=True)
    acct_id = Column(Integer)
    invoice_nbr = Column(Integer)
    order_state_cn = Column(Integer)
    order_status_cn = Column(Integer)
    hold_yn = Column(Boolean)
    priority_cn = Column(Integer)
    submit_date = Column(DateTime)
    fax_sent = Column(DateTime)
    fax_returned = Column(DateTime)
    ship_text = Column(String)
    rph_id = Column(Integer)
    tech_fill = Column(String)
    rph_check = Column(String)
    comments = Column(String)
    liCount = Column(Integer)
    c2Count = Column(Integer)
    ship_cn = Column(Integer)
    sat_deliv_yn = Column(Boolean)
    ship_amt = Column(Float)
    store_id = Column(
        Integer,
        ForeignKey('csstore.store_id'),
    )
    ship_flag_cn = Column(Integer)
    Locked_yn = Column(Boolean)
    locked_id = Column(Integer)
    lock_user_id = Column(
        Integer,
        ForeignKey('csuser.user_id'),
    )
    ship_date = Column(DateTime)
    expected_by = Column(DateTime)
    owner_store_id = Column(
        Integer,
        ForeignKey('csstore.store_id'),
    )
    auto_charge_cc_id = Column(Integer)
    auto_charge_cc_state_cn = Column(Integer)
    send_pos_state_cn = Column(Integer)
    automated_yn = Column(Boolean)
    status_cn = Column(Integer)
    order_category_cn = Column(Integer)
    route_store_id = Column(
        Integer,
        ForeignKey('csstore.store_id'),
    )
    DestStateCD = Column(String)
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
