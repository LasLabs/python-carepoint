# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from mixer.backend.sqlalchemy import mixer


__model__ = 'carepoint.models.cph.fdb_form.FdbForm'


fdb_form_default = mixer.blend(
    __model__,
    gcdf='0A',
    dose='UNIDENT',
    gcdf_desc='UNIDENTIFIED',
    update_yn=False,
)


def fdb_form_rnd(cnt):
    return mixer.cycle(cnt).blend(__model__)
