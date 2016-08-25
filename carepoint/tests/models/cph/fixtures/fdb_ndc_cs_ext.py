# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from mixer.backend.sqlalchemy import mixer
from datetime import datetime


dt_now = datetime.now()
__model__ = 'carepoint.models.cph.fdb_ndc_cs_ext.FdbNdcCsExt'


fdb_ndc_cs_ext_default = mixer.blend(
    __model__,
    ndc='0002032902',
    short_name='An item',
    lot_no='A lot',
    orig_mfg='Orig Mfg',
    pref_gen_yn=True,
    active_yn=True,
    drug_expire_days='Drug Expire Days',
    formulary_yn=True,
    compound_yn=True,
    sup_upd_gen_yn=True,
    sup_upd_phys_yn=True,
    sup_upd_clin_yn=True,
    sup_upd_fin_yn=True,
    sup_upd_med_yn=True,
    dn_form='TABLET',
    dn_str='250 MG',
    dn_route='ORAL',
    rx_only_yn=True,
    manual_yn=True,
    brand_ndc='0002032902',
    add_user_id=1,
    add_date=dt_now,
    chg_user_id=1,
    app_flags='',
    timestmp=dt_now,
    comp_yn=True,
    dea='Dea Num',
    dea_chg_user=1,
    dea_chg_date=dt_now,
    ln='Ln ',
    ln_chg_user=1,
    ln_chg_date=dt_now,
    fdb_chg_date=dt_now,
    ud_svc_code='Ud Svc Code',
    gpi='Gpi',
    gpi_chg_user=1,
    gpi_chg_date=dt_now,
    bill_increment=1,
    formula_id=1,
    alt_iptside1='Alt IptSide1',
    alt_iptside2='Alt IptSide2',
    dose_multiplier='Dose Multiplier',
    default_daw_override='Daw Override',
    manual_price_yn=True,
    compound_type_cn=1,
    refrig_cn=1,
)


def fdb_ndc_cs_ext_rnd(cnt):
    return mixer.cycle(cnt).blend(__model__)
