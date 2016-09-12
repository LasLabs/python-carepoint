# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        Integer,
                        String,
                        DateTime,
                        ForeignKey,
                        Text,
                        )


class PatientDisease(Carepoint.BASE):
    __tablename__ = 'cppat_dx'
    __dbname__ = 'cph'

    ptdx_id = Column(
        Integer, 
        primary_key=True,
        autoincrement=False,
    )
    pat_id = Column(
        Integer,
        ForeignKey('cppat.pat_id'),
    )
    fdbdx = Column(String)
    icd9 = Column(String)
    name = Column(String)
    dx_date = Column(DateTime)
    caring_md_id = Column(
        Integer,
        ForeignKey('cpmd.md_id'),
    )
    onset_date = Column(DateTime)
    resolution_status_cn = Column(Integer)
    screen_yn = Column(Integer)
    mar_cmt = Column(Text)
    cmt = Column(Text)
    status_cn = Column(Integer)
    app_flags = Column(Integer)
    timestmp = Column(DateTime)
    primary_yn = Column(Integer)
    dxid = Column(Integer)
    icd10 = Column(String)
    icd10_name = Column(String)
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
