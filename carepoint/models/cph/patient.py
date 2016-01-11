# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Dave Lasley <dave@laslabs.com>
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

from carepoint import Carepoint
from sqlalchemy import (Column,
                        Integer,
                        String,
                        DateTime,
                        Boolean,
                        ForeignKey,
                        Text,
                        SmallInteger)
from sqlalchemy.orm import relationship, backref


class Patient(Carepoint.BASE):
    __dbname__ = 'cph'
    __tablename__ = 'cppat'

    pat_id = Column(Integer, primary_key=True)
    cmt_id = Column(Integer)
    pat_status_cn = Column(Integer)
    pat_type_cn = Column(Integer)
    nh_pat_id = Column(String)
    chart_id = Column(String)
    lname = Column(String)
    lname_sdx = Column(String)
    mname = Column(String)
    title_lu = Column(String)
    suffix_lu = Column(String)
    alias = Column(String)
    mmname = Column(String)
    alt1_id = Column(String)
    pref_meth_cont_cn = Column(String)
    best_cont_time = Column(String)
    ssn = Column(String)
    dln = Column(String)
    dln_state_cd = Column(String)
    email = Column(String)
    gender_cd = Column(String)
    birth_date = Column(DateTime)
    death_date = Column(DateTime)
    no_safety_caps_yn = Column(Boolean)
    generics_yn = Column(Boolean)
    label_style_cn = Column(Integer)
    primary_md_id = Column(
        Integer,
        ForeignKey('cpmd.md_id')
    )
    secondary_md_id = Column(
        Integer,
        ForeignKey('cpmd.md_id')
    )
    edu_level_cn = Column(Integer)
    ethnicity_cd = Column(String)
    maritial_status_cd = Column(String)
    religion_cn = Column(Integer)
    name_spouse = Column(String)
    primary_lang_cd = Column(String)
    rec_release_status_cn = Column(Integer)
    rec_release_date = Column(DateTime)
    hh_relation_cn = Column(Integer)
    hh_pat_id = Column(
        Integer,
        ForeignKey('cppat.pat_id'),
    )
    fam_relation_cn = Column(String)
    fam_pat_id = Column(
        Integer,
        ForeignKey('cppat.pat_id'),
    )
    primary_store_id = Column(
        Integer,
        ForeignKey('csstore.store_id'),
    )
    bad_check_yn = Column(Boolean)
    price_formula_id = Column(Integer)
    cmt = Column(Text)
    status_cn = Column(Integer)
    facility_pat_yn = Column(Boolean)
    conv_code = Column(String)
    app_flags = Column(Integer)
    timestmp = Column(DateTime)
    comp_cn = Column(Integer)
    hp_blnAdmExt = Column(SmallInteger)
    hp_ExtAtt = Column(SmallInteger)
    user_def_1 = Column(String)
    user_def_2 = Column(String)
    user_def_3 = Column(String)
    user_def_4 = Column(String)
    sc_pat_id = Column(
        Integer,
        ForeignKey('cppat.pat_id'),
    )
    resp_party_id = Column(Integer)
    auto_refill_cn = Column(Integer)
    fill_yn = Column(Boolean)
    fill_stop_date = Column(DateTime)
    fill_resume_date = Column(DateTime)
    fill_stop_reason_cn = Column(Integer)
    fill_stop_user_id = Column(
        Integer,
        ForeignKey('csuser.user_id'),
    )
    registration_date = Column(DateTime)
    anonymous_yn = Column(Boolean)
    market_yn = Column(Boolean)
    representative = Column(String)
    discharge_date = Column(DateTime)
    do_not_resuscitate_yn = Column(Boolean)
    discharge_exp_date = Column(DateTime)
    pat_loc_cn = Column(Integer)
    rx_priority_default_cn = Column(Integer)
    ship_cn = Column(Integer)
    residence_cn = Column(Integer)
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
