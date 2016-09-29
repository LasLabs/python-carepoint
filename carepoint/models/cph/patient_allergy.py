# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        Integer,
                        String,
                        Text,
                        DateTime,
                        ForeignKey,
                        )


class PatientAllergy(Carepoint.BASE):
    __tablename__ = 'cppat_alr'
    __dbname__ = 'cph'

    ptalr_id = Column(
        Integer, 
        primary_key=True,
    )
    pat_id = Column(
        Integer,
        ForeignKey('cppat.pat_id'),
    )
    name = Column(
        String(60),
    )
    hicl_seqno = Column(
        Integer,
        ForeignKey('fdrhiclsq.hicl_seqno'),
    )
    hic = Column(
        String(6),
        ForeignKey('fdrhicd.hic'),
    )
    dam_agcsp = Column(
        Integer,
        ForeignKey('fdrdamagd.dam_agcsp'),
    )
    alr_type_cn = Column(
        Integer,
    )
    onset_date = Column(
        DateTime,
    )
    resolution_status_cn = Column(
        Integer,
    )
    resolution_date = Column(
        DateTime,
    )
    screen_yn = Column(
        Integer,
    )
    cmt = Column(
        Text,
    )
    status_cn = Column(
        Integer,
    )
    app_flags = Column(
        Integer,
    )
    timestmp = Column(
        DateTime,
    )
    ncd = Column(
        String(11),
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
    chg_date = Column(
        DateTime,
    )
