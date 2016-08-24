# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from mixer.backend.sqlalchemy import mixer


__model__ = 'carepoint.models.cph.fdb_lbl_rid.FdbLblRid'


fdb_lbl_rid_default = mixer.blend(
    __model__,
    lblrid='A00002',
    mfg='ELI LILLY & CO.',
    update_yn=False,
)


def fdb_lbl_rid_rnd(cnt):
    return mixer.cycle(cnt).blend(__model__)
