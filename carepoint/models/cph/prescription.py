# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Vinnie Corcoran <vcorcoran@laslabs.com>
#    Copyright: 2015 LasLabs, Inc [https://laslabs.com]
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from .base import Base
from sqlalchemy import (Column, Integer, String, DateTime, Boolean,
                        ForeignKey, Text, SmallInteger)
from sqlalchemy.orm import relationship, backref


class Prescription(Base):
    __tablename__ = 'cprx'
    
    rx_id = Column(Integer, primary_key=True)
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
    start_date = Column(Datetime)
    expire_date = Column(Datetime)
    stop_date = Column(Datetime)
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
    last_refill_date = Column(Datetime)
    refill_date = Column(Datetime)
    src_org_id = Column(Integer)
    cmt = Column(Text)
    exit_state_cn = Column(Integer)
    script_status_cn = Column(Integer)
    sched_date = Column(Datetime)
    sched_time = Column(Datetime)
    scheduled_yn = Column(Boolean)
    drug_dea_class = Column(String)
    manual_add_yn = Column(Boolean)
    status_cn = Column(Integer)
    life_date = Column(Datetime)
    self_prescribed_yn = Column(Boolean)
    last_transfer_type_io = Column(String)
    last_disp_prod = Column(String)
    transfer_cnt = Column(Numeric)
    wc_claim_id = Column(String)
    injury_date = Column(Datetime)
    gpi_rx = Column(Integer)
    auth_by = Column(String)
    orig_disp_date = Column(Datetime)
    short_term_ym = Column(Integer)
    orig_date = Column(Datetime)
    refills_used = Column(Numeric)
    wc_emp_id = Column(Integer)
    dose_unit = Column(String)
    doseage_multiplier = Column(Numeric)
    df = Column(String)
    uu = Column(String)
    app_flags = Column(Integer)
    timestmp = Column(Datetime)
    sched2_no = Column(String)
    orig_expire_date = Column(Datetime)
    rxq_status_cn = Column(Integer)
    IVRCmt = Column(String)
    wc_bodypart = Column(String)
    comp_ndc = Column(String)
    treatment_yn = Column(Boolean)
    ivr_callback = Column(String)
    autofill_yn = Column(Boolean)
    autofill_resume_date = Column(Datetime)
    worflow_status_cn = Column(Integer)
    extern_process_cn = Column(Integer)
    md_fac_id = Column(Integer)
    owner_store_id = Column(Integer)
    study_id = Column(Integer)
    min_days_until_refill = Column(Integer)
    sig_text_english = Column(String)
    order_fulfillment_cn = Column(Integer)
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
