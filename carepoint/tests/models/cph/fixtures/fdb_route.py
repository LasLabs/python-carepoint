# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

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
