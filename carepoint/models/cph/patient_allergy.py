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


class PatientAllergy(Carepoint.BASE):
    __tablename__ = 'cppat_alr'
    __dbname__ = 'cph'

    ptalr_id = Column(
        Integer, 
        primary_key=True,
        autoincrement=False,
    )
    pat_id = Column(
        Integer,
        ForeignKey('cppat.pat_id'),
    )
    name = Column(String)
    hicl_seqno = Column(Integer)
    hic = Column(Integer)
    dam_agcsp = Column(Integer)
    alr_type_cn = Column(Integer)
    onset_date = Column(DateTime)
    resolution_status_cn = Column(Integer)
    resolution_date = Column(DateTime)
    screen_yn = Column(Integer)
    cmt = Column(String)
    status_cn = Column(Integer)
    app_flags = Column(Integer)
    timestmp = Column(DateTime)
    ncd = Column(String)
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
