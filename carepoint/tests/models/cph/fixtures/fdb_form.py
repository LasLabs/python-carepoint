# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

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
