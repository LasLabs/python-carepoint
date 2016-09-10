# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        Integer,
                        String,
                        DateTime,
                        ForeignKey,
                        )


class Vendor(Carepoint.BASE):
    __dbname__ = 'cph'
    __tablename__ = 'VEND'

    ID = Column(
        Integer, 
        primary_key=True,
        autoincrement=False,
    )
    COMPANY = Column(String)
    ADDR1 = Column(String)
    ADDR2 = Column(String)
    CITY = Column(String)
    STATE = Column(String)
    ZIP = Column(String)
    FEDID = Column(String)
    CONTACT = Column(String)
    PHONE = Column(String)
    ISSUE1099 = Column(String)
    ONETIME = Column(String)
    FAX = Column(String)
    ACCT = Column(String)
    TERMS = Column(String)
    COSTTYPE = Column(Integer)
    compound_vendor_yn = Column(String)
    POPrefix = Column(String)
    po_alpha_align_cn = Column(Integer)
    po_alpha_used = Column(String)
    po_next_id_int = Column(Integer)
    DocumentNumber = Column(String)
    NumberOfDigits = Column(Integer)
    LastPODate = Column(DateTime)
    DocCounter = Column(Integer)
    grid_color = Column(Integer)
    bold_yn = Column(Integer)
    italic_yn = Column(Integer)
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
