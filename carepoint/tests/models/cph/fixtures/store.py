# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from mixer.backend.sqlalchemy import mixer
from datetime import datetime


dt_now = datetime.now()
__model__ = 'carepoint.models.cph.store.Store'

store_default = mixer.blend(
    __model__,
    store_id=1,
    store_type_cn=1,
    name='Name',
    store_hours='StoreHours',
    store_no='StoreNo',
    fed_tax_id='FedTaxId',
    url='Url',
    email='Email',
    mgr_cont_id=1,
    cont_id=1,
    carepoint_acct_no='CarepointAcctNo',
    cmt='Cmt',
    status_cn=1,
    app_flags=1,
    nabp='Nabp',
    medcaid_no='Medicaid',
    timestamp=dt_now,
    region_id=1,
    NPI='Npi',
    pharmacy_service_type_cn=1,
    web_refill_yn=False,
    add_user_id=1,
    add_date=dt_now,
    chg_user_id=1,
    chg_date=dt_now,
)

store_rnd = lambda cnt: mixer.cycle(cnt).blend(__model__)
