# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from mixer.backend.sqlalchemy import mixer
from datetime import datetime


dt_now = datetime.now()
__model__ = 'carepoint.models.cph.user.User'


user_default = mixer.blend(
    __model__,
    user_id=1,
    user_type_cd='UserType',
    login_name='LoginName',
    lname='Lname',
    fname='Fname',
    mname='Mname',
    title_lu='TitleLu',
    suffix_lu='SuffixLu',
    degree_lu='Degree',
    initials='Initials',
    job_title_lu='JobTitle',
    anote='Anote',
    employee_no='EmployeeNo',
    ssn='Social',
    last_login_date=dt_now,
    email='Email',
    db_password='DbPassword',
    es_password='EsPassword',
    cmt='Cmt',
    system_yn=1,
    license_no='LicenseNo',
    license_state_cd='LicenseStateCd',
    status_cn=1,
    app_flags=1,
    timestmp=dt_now,
    must_change_password_yn=1,
    password_date=dt_now,
    add_user_id=1,
    add_date=dt_now,
    chg_user_id=1,
    chg_date=dt_now,
)


def user_rnd(cnt):
    return mixer.cycle(cnt).blend(__model__)
