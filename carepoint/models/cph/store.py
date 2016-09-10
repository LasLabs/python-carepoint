# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        Integer,
                        String,
                        DateTime,
                        Boolean,
                        ForeignKey,
                        Text,
                        )


class Store(Carepoint.BASE):
    __tablename__ = 'csstore'
    __dbname__ = 'cph'

    store_id = Column(
        Integer, 
        primary_key=True,
        autoincrement=False,
    )
    store_type_cn = Column(Integer)
    name = Column(String)
    store_hours = Column(String)
    store_no = Column(String)
    fed_tax_id = Column(String)
    url = Column(String)
    email = Column(String)
    mgr_cont_id = Column(Integer)
    cont_id = Column(Integer)
    carepoint_acct_no = Column(String)
    cmt = Column(Text)
    status_cn = Column(Integer)
    app_flags = Column(Integer)
    nabp = Column(String)
    medicaid_no = Column(String)
    timestmp = Column(DateTime)
    region_id = Column(Integer)
    NPI = Column(String)
    pharmacy_service_type_cn = Column(Integer)
    web_refill_yn = Column(Boolean)
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
