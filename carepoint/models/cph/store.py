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


class Store(Carepoint.BASE):
    __tablename__ = 'csstore'
    __dbname__ = 'cph'

    store_id = Column(Integer, primary_key=True)
    store_type_cn = Column(Integer)
    name = Column(String)
    store_hours = Column(String)
    store_no = Column(String)
    fed_tax_id = Column(String)
    url = Column(String)
    email = Column(String)
    mgr_cont_id = Column(Integer)
    cont_id = Column(Integer)
    carepoint_acct_no = Column(String)
    cmt = Column(Text)
    status_cn = Column(Integer)
    app_flags = Column(Integer)
    nabp = Column(String)
    medcaid_no = Column(String)
    timestamp = Column(DateTime)
    region_id = Column(Integer)
    NPI = Column(String)
    pharmacy_service_type_cn = Column(Integer)
    web_refill_yn = Column(Boolean)
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
