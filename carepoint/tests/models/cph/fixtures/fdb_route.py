# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from mixer.backend.sqlalchemy import mixer


__model__ = 'carepoint.models.cph.fdb_route.FdbRoute'


fdb_route_default = mixer.blend(
    __model__,
    gcrt='K',
    rt='INTRAARTIC',
    gcrt2='UI',
    gcrt_desc='INTRAARTICULAR',
    systemic='S',
    update_yn=False,
)


def fdb_route_rnd(cnt):
    return mixer.cycle(cnt).blend(__model__)
