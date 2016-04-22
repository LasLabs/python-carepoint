# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

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
