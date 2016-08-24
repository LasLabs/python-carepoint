# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from mixer.backend.sqlalchemy import mixer
from datetime import datetime


dt_now = datetime.now()
__model__ = 'carepoint.models.cph.store_param.StoreParam'


store_param_default = mixer.blend(
    __model__,
    store_id=1,
    param_code='SC_MOD_RD_PROD_IMAGE_DIR',
    descr='SC_MOD_RD_PROD_IMAGE_DIR',
    data_value='\\GRXServer\images',
    app_flags=0,
    timestmp=dt_now
)


def store_param_rnd(cnt):
    return mixer.cycle(cnt).blend(__model__)
