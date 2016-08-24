# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from mixer.backend.sqlalchemy import mixer
from datetime import datetime


dt_now = datetime.now()
__model__ = 'carepoint.models.cph.fdb_gcn.FdbGcn'


fdb_gcn_default = mixer.blend(
    __model__,
    gcn_seqno=1,
    gcn=11,
    update_yn=False,
)


def fdb_gcn_rnd(cnt):
    return mixer.cycle(cnt).blend(__model__)
