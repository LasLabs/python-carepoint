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
from sqlalchemy import (Column,
                        Integer,
                        String,
                        DateTime,
                        Boolean,
                        ForeignKey,
                        Text,
                        SmallInteger)
from sqlalchemy.orm import relationship, backref


class User(Carepoint.BASE):
    __tablename__ = 'csuser'
    __dbname__ = 'cph'

    user_id = Column(Integer, primary_key=True)
    user_type_cd = Column(String)
    login_name = Column(String)
    lname = Column(String)
    fname = Column(String)
    mname = Column(String)
    title_lu = Column(String)
    suffix_lu = Column(String)
    degree_lu = Column(String)
    initials = Column(String)
    job_title_lu = Column(String)
    anote = Column(String)
    employee_no = Column(String)
    ssn = Column(String)
    last_login_date = Column(DateTime)
    email = Column(String)
    db_password = Column(String)
    es_password = Column(String)
    cmt = Column(Text)
    system_yn = Column(Integer)
    license_no = Column(String)
    license_state_cd = Column(String)
    status_cn = Column(Integer)
    app_flags = Column(Integer)
    timestmp = Column(DateTime)
    must_change_password_yn = Column(Integer)
    password_date = Column(DateTime)
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
