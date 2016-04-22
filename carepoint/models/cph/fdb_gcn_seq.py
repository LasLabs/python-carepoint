# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        Integer,
                        String,
                        Boolean,
                        )


class FdbGcnSeq(Carepoint.BASE):
    __tablename__ = 'fdrgcnseq'
    __dbname__ = 'cph'

    gcn_seqno = Column(Integer, primary_key=True)
    hic3 = Column(String)
    hicl_seqno = Column(Integer)
    gcdf = Column(String)
    gcrt = Column(String)
    str = Column(String)
    gtc = Column(Integer)
    tc = Column(Integer)
    dcc = Column(Integer)
    gcnseq_gi = Column(Integer)
    gender = Column(Integer)
    hic3_seqn = Column(Integer)
    str60 = Column(String)
    update_yn = Column(Boolean)
