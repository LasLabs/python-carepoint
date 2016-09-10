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
                        Numeric,
                        )


class Organization(Carepoint.BASE):
    __dbname__ = 'cph'
    __tablename__ = 'csorg'

    org_id = Column(
        Integer, 
        primary_key=True,
        autoincrement=False,
    )
    name = Column(String)
    name_sdx = Column(String)
    url = Column(String)
    email = Column(String)
    contact = Column(String)
    fed_tax_id = Column(String)
    clinic_no = Column(String)
    cmt = Column(Text)
    system_yn = Column(Boolean)
    ins_type_cn = Column(Integer)
    status_cn = Column(Integer)
    app_flags = Column(Integer)
    timestmp = Column(DateTime)
    cont_id = Column(Integer)
    per_diem = Column(Numeric(18, 8))
    external_id = Column(String)
    tf_days = Column(Integer)
    dea_no = Column(String)
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
