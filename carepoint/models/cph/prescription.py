# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        Integer,
                        String,
                        DateTime,
                        Boolean,
                        ForeignKey,
                        Numeric,
                        Text,
                        )


class Prescription(Carepoint.BASE):
    __tablename__ = 'cprx'
    __dbname__ = 'cph'

    rx_id = Column(
        Integer, 
        primary_key=True,
        autoincrement=False,
    )
    script_no = Column(String)
    old_script_no = Column(String)
    pat_id = Column(
        Integer,
        ForeignKey('cppat.pat_id'),
    )
    store_id = Column(
        Integer,
        ForeignKey('csstore.store_id'),
    )
    md_id = Column(
        Integer,
        ForeignKey('cpmd.md_id'),
    )
    ndc = Column(String)
    gcn_seqno = Column(Integer)
    mfg = Column(String)
    drug_name = Column(String)
    input_src_cn = Column(Integer)
    src_pat_meds_cn = Column(Integer)
    start_date = Column(DateTime)
    expire_date = Column(DateTime)
    stop_date = Column(DateTime)
    sig_code = Column(String)
    sig_text = Column(String)
    written_qty = Column(Numeric)
    starter_qty = Column(Numeric)
    days_supply = Column(Numeric)
    pkg_size = Column(Numeric)
    units_per_dose = Column(Numeric)
    units_entered = Column(String)
    awp = Column(Numeric)
    udef = Column(Numeric)
    ful = Column(Numeric)
    mac = Column(Numeric)
    aac = Column(Numeric)
    freq_entered = Column(String)
    freq_of_admin = Column(Numeric)
    sched_of_admin_cn = Column(Integer)
    daw_yn = Column(Boolean)
    refills_orig = Column(Numeric)
    refills_left = Column(Numeric)
    last_rxdisp_id = Column(
        Integer,
        ForeignKey('cprx_disp.rxdisp_id'),
    )
    last_refill_qty = Column(Numeric)
    last_refill_date = Column(DateTime)
    refill_date = Column(DateTime)
    src_org_id = Column(
        Integer,
        ForeignKey('csorg.org_id'),
    )
    cmt = Column(Text)
    exit_state_cn = Column(Integer)
    script_status_cn = Column(Integer)
    sched_date = Column(DateTime)
    sched_time = Column(DateTime)
    scheduled_yn = Column(Boolean)
    drug_dea_class = Column(String)
    manual_add_yn = Column(Boolean)
    status_cn = Column(Integer)
    life_date = Column(DateTime)
    self_prescribed_yn = Column(Boolean)
    last_transfer_type_io = Column(String)
    last_disp_prod = Column(String)
    transfer_cnt = Column(Numeric)
    wc_claim_id = Column(String)
    injury_date = Column(DateTime)
    gpi_rx = Column(Integer)
    auth_by = Column(String)
    orig_disp_date = Column(DateTime)
    short_term_yn = Column(Integer)
    orig_date = Column(DateTime)
    refills_used = Column(Numeric)
    wc_emp_id = Column(Integer)
    dose_unit = Column(String)
    dosage_multiplier = Column(Numeric)
    df = Column(String)
    uu = Column(String)
    app_flags = Column(Integer)
    timestmp = Column(DateTime)
    sched2_no = Column(String)
    orig_expire_date = Column(DateTime)
    rxq_status_cn = Column(Integer)
    IVRCmt = Column(String)
    wc_bodypart = Column(String)
    comp_ndc = Column(String)
    treatment_yn = Column(Boolean)
    ivr_callback = Column(String)
    autofill_yn = Column(Boolean)
    autofill_resume_date = Column(DateTime)
    workflow_status_cn = Column(Integer)
    extern_process_cn = Column(Integer)
    md_fac_id = Column(Integer)
    owner_store_id = Column(Integer)
    study_id = Column(Integer)
    min_days_until_refill = Column(Integer)
    sig_text_english = Column(String)
    order_fullfillment_cn = Column(Integer)
    taxable = Column(Integer)
    MAR_flag = Column(Integer)
    FreeFormStrength = Column(String)
    priority_cn = Column(Integer)
    ecs_yn = Column(Boolean)
    edit_locked_yn = Column(Boolean)
    locked_yn = Column(Boolean)
    locked_id = Column(Integer)
    locked_user_id = Column(
        Integer,
        ForeignKey('csuser.user_id'),
    )
    daw_rx_cn = Column(Integer)
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
