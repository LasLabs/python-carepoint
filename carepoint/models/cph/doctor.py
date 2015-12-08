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

from carepoint import Carepoint
from sqlalchemy import (Column, Integer, String, DateTime, Boolean,
                        ForeignKey, Text, SmallInteger)
from sqlalchemy.orm import relationship, backref


class Doctor(Carepoint.BASE):
    __table__ = 'cpmd'
    __db__ = 'cph'
    
    md_id = Column(Integer, primary_key=True)
    lname = Column(String)
    lname_sdx = Column(String)
    fname = Column(String)
    fname_sdx = Column(String)
    mname = Column(String)
    title_lu = Column(String)
    suffix_lu = Column(String)
    degree_lu = Column(String)
    prescriber_type_cn = Column(Integer)
    email = Column(String)
    url = Column(String)
    pref_meth_contact_cn = Column(Integer)
    best_cont_time = Column(String)
    specialty_cd = Column(String)
    dea_no = Column(String)
    dea_suffix = Column(String)
    spin_no = Column(String)
    upin_no = Column(String)
    other_id = Column(String)
    fed_tax_id = Column(String)
    hin_id = Column(String)
    champus_id = Column(String)
    state_lic_id = Column(String)
    ncpdp_id = Column(String)
    medicaid_id = Column(String)
    medicare_id = Column(String)
    blue_shield_id = Column(String)
    blue_cross_id = Column(String)
    npi_id = Column(String)
    practice_org_id = Column(Integer)
    cmt = Column(Text)
    status_cn = Column(Integer)
    conv_code = Column(String)
    app_flags = Column(Integer)
    timestamp = Column(Datetime)
    state_issued_id = Column(String)
    sname = Column(String)
    medicaid_restricted_yn = Column(Boolean)
    fac_id = Column(Integer)
    C2Restricted_yn = Column(Boolean)
    co_md_id = Column(
        Integer,
        ForeignKey('cpmd.md_id'),
    )
    do_not_refer = Column(Integer)
    deceased_yn = Column(Boolean)
    C0restricted_yn = Column(Boolean)
    C3restricted_yn = Column(Boolean)
    C4restricted_yn = Column(Boolean)
    C5restricted_yn = Column(Boolean)
    study_drugs_yn = Column(Boolean)
    tracking_cn = Column(Integer)
    CTP_no = Column(String)
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
