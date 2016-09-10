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
                        Text,
                        )


class Doctor(Carepoint.BASE):
    __tablename__ = 'cpmd'
    __dbname__ = 'cph'

    md_id = Column(
        Integer, 
        primary_key=True,
        autoincrement=False,
    )
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
    practice_org_id = Column(
        Integer,
        ForeignKey('csorg.org_id'),
    )
    cmt = Column(Text)
    status_cn = Column(Integer)
    conv_code = Column(String)
    app_flags = Column(Integer)
    timestmp = Column(DateTime)
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
