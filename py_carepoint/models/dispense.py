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


class Dispense(Base):
    __tablename__ = 'cprx_disp'
    
    rx_id = Column(Integer)
    store_id = Column(Integer)
    disp_ndc = Column(String)
    disp_drug_name = Column(String)
    prod_expire_date = Column(Datetime)
    mfg = Column(String)
    orig_mfg = Column(String)
    pkg_size = Column(Numeric)
    rxdisp_id = Column(Integer, primary_key=True)
    fill_no = Column(Integer)
    dispense_date = Column(Datetime)
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
    tech_initals = Column(String)
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
    label_3pty_yn = Column(Boolean)
    reject_3pty_yn = Column(Boolean)
    pay_type_cn = Column(Integer)
    price_differs_yn = Column(Boolean)
    pat_loc_cn = Column(Integer)
    billing_units = Column(String)
    price_table_id = Column(Integer)
    add_date = Column(Datetime)
    add_user_id = Column(Integer)
    chg_date = Column(Datetime)
    chg_user_id = Column(Integer)
    app_flags = Column(Integer)
    timestmp = Column(Datetime)
    price_meth_cn = Column(Integer)
    uu = Column(String)
    p_tbl_override_yn = Column(Boolean)
    label_id = Column(Integer)
    billing_hold = Column(Integer)
    post_bal_yn = Column(Boolean)
    inv_no = Column(String)
    disp_qty_delta = Column(Numeric)
    brand_med_nec_yn = Column(Boolean)
    Other_coverage_cd = Column(Integer)
    epsdt_yn = Column(Boolean)
    exempt_cd = Column(Integer)
    num_labels = Column(Integer)
    location = Column(String)
    qty_override = Column(Numeric)
    dur_summary = Column(Text)
    cov_overrides = Column(Integer)
    use_secondary_ins_yn = Column(Boolean)
    hp_blnRxExtr = Column(SmallInteger)
    hp_ExtAtt = Column(SmallInteger)
    user_def_1 = Column(String)
    user_def_2 = Column(String)
    user_def_3 = Column(String)
    user_def_4 = Column(String)
    sc_pat_id = Column(Integer)
    resp_party_id = Column(Integer)
    auto_refill_cn = Column(Integer)
    fill_yn = Column(Boolean)
    fill_stop_date = Column(Datetime)
    fill_resume_date = Column(Datetime)
    fill_stop_reason_cn = Column(Integer)
    fill_stop_user_id = Column(Integer)
    registration_date = Column(Datetime)
    anonymous_yn = Column(Boolean)
    market_yn = Column(Boolean)
    representative = Column(String)
    discharge_date = Column(Datetime)
    do_not_resuscitate_yn = Column(Boolean)
    discharge_exp_date = Column(Datetime)
    pat_loc_cn = Column(Integer)
    rx_priority_default_cn = Column(Integer)
    ship_cn = Column(Integer)
    residence_cn = Column(Integer)
