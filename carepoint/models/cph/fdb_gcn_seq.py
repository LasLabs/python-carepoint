# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        Integer,
                        String,
                        Boolean,
                        ForeignKey,
                        )


class FdbGcnSeq(Carepoint.BASE):
    __tablename__ = 'fdrgcnseq'
    __dbname__ = 'cph'

    gcn_seqno = Column(
        Integer, 
        primary_key=True,
        autoincrement=False,
    )
    hic3 = Column(String)
    hicl_seqno = Column(Integer)
    gcdf = Column(
        String,
        ForeignKey('fdrdosed.gcdf'),
    )
    gcrt = Column(
        String,
        ForeignKey('fdrrouted.gcrt'),
    )
    str = Column(String)
    gtc = Column(Integer)
    tc = Column(Integer)
    dcc = Column(Integer)
    gcnseq_gi = Column(Integer)
    gender = Column(Integer)
    hic3_seqn = Column(Integer)
    str60 = Column(String)
    update_yn = Column(Boolean)
