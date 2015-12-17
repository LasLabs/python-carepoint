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

from mixer.backend.sqlalchemy import mixer
from datetime import datetime, date


dt_now = datetime.now()
__model__ = 'carepoint.models.cph.user.User'

user_default = mixer.blend(
    __model__,
    user_id = 1,
    user_type_cd = 'UserType',
    login_name = 'LoginName',
    lname = 'Lname',
    fname = 'Fname',
    mname = 'Mname',
    title_lu = 'TitleLu',
    suffix_lu = 'SuffixLu',
    degree_lu = 'Degree',
    initials = 'Initials',
    job_title_lu = 'JobTitle',
    anote = 'Anote',
    employee_no = 'EmployeeNo',
    ssn = 'Social',
    last_login_date = dt_now,
    email = 'Email',
    db_password = 'DbPassword',
    es_password = 'EsPassword',
    cmt = 'Cmt',
    system_yn = 1,
    license_no = 'LicenseNo',
    license_state_cd = 'LicenseStateCd',
    status_cn = 1,
    app_flags = 1,
    timestmp = dt_now,
    must_change_password_yn = 1,
    password_date = dt_now,
    add_user_id = 1,
    add_date = dt_now,
    chg_user_id = 1,
    chg_date = dt_now,
)

user_rnd = lambda cnt: mixer.cycle(cnt).blend(__model__)