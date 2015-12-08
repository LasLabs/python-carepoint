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
from carepoint.models.cph.user import User
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Boolean,
    ForeignKey,
    Text,
    SmallInteger
)
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Address(Carepoint.BASE):
    __tablename__ = 'csaddr'
    __dbname__ = 'cph'
    
    addr_id = Column(Integer, primary_key=True)
    parent_addr_id = Column(
        Integer,
        ForeignKey(Address.addr_id),
    )
    inherited_yn = Column(Boolean)
    owner_type_cn = Column(Integer)
    alt_name = Column(String)
    addr1 = Column(String)
    addr2 = Column(String)
    addr3 = Column(String)
    city = Column(String)
    state_cd = Column(String)
    zip = Column(String)
    zip_plus4 = Column(String)
    country_cd = Column(String)
    mailing_yn = Column(Boolean)
    anote = Column(String)
    app_flags = Column(Integer)
    timestmp = Column(Datetime)
    add_user_id = Column(
        Integer,
        ForeignKey(User.user_id),
    )
    add_date = Column(DateTime)
    chg_user_id = Column(
        Integer,
        ForeignKey(User.user_id),
    )
    chg_date = Column(DateTime)
