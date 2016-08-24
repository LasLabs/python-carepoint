# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from mixer.backend.sqlalchemy import mixer
from datetime import datetime


dt_now = datetime.now()
__model__ = 'carepoint.models.cph.address.Address'


address_default = mixer.blend(
    __model__,
    addr_id=1,
    parent_addr_id=None,
    inherited_yn=False,
    owner_type_cn=1,
    alt_name='Alt Name',
    addr1='Addr1',
    addr2='Addr2',
    addr3='Addr3',
    city='City',
    state_cd='StateCd',
    zip='Zip',
    zip_plus4='ZipPlus4',
    country_cd='CountryCd',
    mailing_yn=False,
    anote='ANote',
    app_flags=1,
    timestmp=dt_now,
    add_user_id=1,
    add_date=dt_now,
    chd_user_id=1,
    chg_date=dt_now,
)


def addresses_rnd(cnt):
    return mixer.cycle(cnt).blend(__model__)
