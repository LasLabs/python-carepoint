# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from mixer.backend.sqlalchemy import mixer
from datetime import datetime


dt_now = datetime.now()
__model__ = 'carepoint.models.cph.fdb_gcn_seq.FdbGcnSeq'


fdb_gcn_seq_default = mixer.blend(
    __model__,
    gcn_seqno=1,
    hic3='A1A',
    hicl_seqno=1,
    gcdf='TA',
    gcrt=1,
    str='100 MG',
    gtc=38,
    tc=74,
    dcc=0,
    gcnseq_gi=1,
    gender=0,
    hic3_seqn=139,
    str60='100 mg',
    update_yn=0,
)


def fdb_gcn_seq_rnd(cnt):
    return mixer.cycle(cnt).blend(__model__)
