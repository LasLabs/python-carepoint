# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        Integer,
                        Boolean,
                        String,
                        ForeignKey,
                        DateTime,
                        )


class FdbNdcCsExt(Carepoint.BASE):
    __tablename__ = 'csext_fdrndc'
    __dbname__ = 'cph'

    ndc = Column(String, primary_key=True)
    short_name = Column(String)
    lot_no = Column(String)
    orig_mfg = Column(String)
    pref_gen_yn = Column(Boolean)
    active_yn = Column(Boolean)
    drug_expire_days = Column(String)
    formulary_yn = Column(Boolean)
    compound_yn = Column(Boolean)
    sup_upd_gen_yn = Column(Boolean)
    sup_upd_phys_yn = Column(Boolean)
    sup_upd_clin_yn = Column(Boolean)
    sup_upd_fin_yn = Column(Boolean)
    sup_upd_med_yn = Column(Boolean)
    dn_form = Column(String)
    dn_str = Column(String)
    dn_route = Column(String)
    rx_only_yn = Column(Boolean)
    manual_yn = Column(Boolean)
    brand_ndc = Column(String)
    add_user_id = Column(
        Integer,
        ForeignKey('csuser.user_id'),
    )
    add_date = Column(DateTime)
    chg_user_id = Column(
        Integer,
        ForeignKey('csuser.user_id'),
    )
    app_flags = Column(String)
    timestmp = Column(DateTime)
    comp_yn = Column(Boolean)
    dea = Column(String)
    dea_chg_user = Column(
        Integer,
        ForeignKey('csuser.user_id'),
    )
    dea_chg_date = Column(DateTime)
    ln = Column(String)
    ln_chg_user = Column(
        Integer,
        ForeignKey('csuser.user_id'),
    )
    ln_chg_date = Column(DateTime)
    fdb_chg_date = Column(DateTime)
    ud_svc_code = Column(String)
    gpi = Column(String)
    gpi_chg_user = Column(
        Integer,
        ForeignKey('csuser.user_id'),
    )
    gpi_chg_date = Column(DateTime)
    bill_increment = Column(Integer)
    formula_id = Column(Integer)
    alt_iptside1 = Column(String)
    alt_iptside2 = Column(String)
    dose_multiplier = Column(String)
    default_daw_override = Column(String)
    manual_price_yn = Column(Boolean)
    compound_type_cn = Column(Integer)
    refrig_cn = Column(Integer)
