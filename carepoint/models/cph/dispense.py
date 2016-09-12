# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        Integer,
                        String,
                        DateTime,
                        ForeignKey,
                        Numeric,
                        Text,
                        SmallInteger)


class Dispense(Carepoint.BASE):
    __tablename__ = 'cprx_disp'
    __dbname__ = 'cph'

    rxdisp_id = Column(
        Integer, 
        primary_key=True,
        autoincrement=False,
    )
    rx_id = Column(
        Integer,
        ForeignKey('cprx.rx_id'),
    )
    store_id = Column(
        Integer,
        ForeignKey('csstore.store_id'),
    )
    disp_ndc = Column(String)
    disp_drug_name = Column(String)
    prod_expire_date = Column(DateTime)
    mfg = Column(String)
    orig_mfg = Column(String)
    pkg_size = Column(Numeric)
    fill_no = Column(Integer)
    dispense_date = Column(DateTime)
    dispense_qty = Column(Numeric)
    disp_days_supply = Column(Numeric)
    sig_text = Column(String)
    sched_of_admin_cn = Column(Integer)
    freq_of_admin = Column(Numeric)
    units_per_dose = Column(Numeric)
    lot_number = Column(String)
    disp_awp = Column(Numeric)
    disp_aac = Column(Numeric)
    disp_mac = Column(Numeric)
    disp_ful = Column(Numeric)
    disp_udef = Column(Numeric)
    tech_initials = Column(String)
    rph_initials = Column(String)
    cnsl_initials = Column(String)
    icd9 = Column(String)
    daw_disp_cn = Column(Integer)
    level_of_service = Column(Integer)
    cmt = Column(Text)
    status_cn = Column(Integer)
    alt_pick_up_id = Column(Integer)
    alt_pick_up_cn = Column(Integer)
    clarification_fill = Column(Integer)
    trip_no = Column(Integer)
    gpi_disp = Column(Integer)
    label_3pty_yn = Column(Integer)
    reject_3pty_yn = Column(Integer)
    pay_type_cn = Column(Integer)
    price_differs_yn = Column(Integer)
    pat_loc_cn = Column(Integer)
    billing_units = Column(String)
    price_table_id = Column(Integer)
    app_flags = Column(Integer)
    timestmp = Column(DateTime)
    price_meth_cn = Column(Integer)
    uu = Column(String)
    p_tbl_override_yn = Column(Integer)
    label_id = Column(Integer)
    billing_hold = Column(Integer)
    post_bal_yn = Column(Integer)
    inv_no = Column(String)
    disp_qty_delta = Column(Numeric)
    brand_med_nec_yn = Column(Integer)
    Other_coverage_cd = Column(Integer)
    epsdt_yn = Column(Integer)
    exempt_cd = Column(Integer)
    num_labels = Column(Integer)
    location = Column(String)
    qty_override = Column(Numeric)
    dur_summary = Column(Text)
    cov_overrides = Column(Integer)
    use_secondary_ins_yn = Column(Integer)
    hp_blnRxExtr = Column(SmallInteger)
    item_id = Column(Integer)
    ud_override = Column(String)
    disp_status_cn = Column(Integer)
    order_id = Column(Integer)
    sig_id = Column(Integer)
    counsel_yn = Column(Integer)
    processing_date = Column(DateTime)
    hcpcs_mod_cn = Column(Integer)
    acct_id = Column(Integer)
    track_pat_resp_yn = Column(Integer)
    track_org_resp_yn = Column(Integer)
    label_fac_id = Column(Integer)
    extern_process_cn = Column(Integer)
    price_ovr_user_id = Column(Integer)
    price_ovr_reason_cn = Column(Integer)
    wf_status_cn = Column(Integer)
    verify_user_id = Column(Integer)
    verify_timestamp = Column(DateTime)
    ar_hold = Column(Integer)
    disp_type_cn = Column(Integer)
    own_use_pricing_yn = Column(Integer)
    pos_processed_yn = Column(Integer)
    prescriber_cn = Column(Integer)
    visit_nbr = Column(String)
    disp_udef = Column(Integer)
    SecondaryICD9 = Column(String)
    uandc_pricing_used_yn = Column(Integer)
    special_pkg_ind_cn = Column(Integer)
    delay_reason_cn = Column(Integer)
    place_of_service_cn = Column(Integer)
    pat_residence_cn = Column(Integer)
    compound_type_cn = Column(Integer)
    pharmacy_service_type_cn = Column(Integer)
    admin_start_date = Column(DateTime)
    ClariFill_2 = Column(Integer)
    ClariFill_3 = Column(Integer)
    other_coverage_cd_2 = Column(Integer)
    pat_assign_ind_yn = Column(Integer)
    prov_assign_ind_yn = Column(Integer)
    route_of_admin_ovr = Column(String)
    csr_pickup_id = Column(Integer)
    icd10 = Column(String)
    secondaryicd10 = Column(String)
    add_user_id = Column(
        Integer,
        ForeignKey('csuser.user_id'),
    )
    add_date = Column(DateTime)
    chg_user_id = Column(
        Integer,
        ForeignKey('csuser.user_id'),
    )
    chg_date = Column(DateTime)
