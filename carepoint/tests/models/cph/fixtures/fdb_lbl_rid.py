# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

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
