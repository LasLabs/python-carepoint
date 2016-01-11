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
                        Numeric,
                        Float,
                        Text,
                        SmallInteger)
from sqlalchemy.orm import relationship, backref


class Item(Carepoint.BASE):
    __tablename__ = 'item'
    __dbname__ = 'cph'

    ITEMMSTR = Column(String)
    DESCR = Column(String)
    TAXABLE = Column(String)
    CLASS = Column(String)
    UOFMSALES = Column(String)
    UOFMORDERS = Column(String)
    FACTOR = Column(Float)
    ONHAND = Column(Numeric)
    ONORDER = Column(Numeric)
    VENDOR = Column(String)
    COST = Column(Numeric)
    INQTY = Column(Numeric)
    INDATE = Column(DateTime)
    OUTQTY = Column(Numeric)
    OUTDATE = Column(DateTime)
    ADJQTY = Column(Numeric)
    ADJDATE = Column(DateTime)
    MTD_ISSUE = Column(Numeric)
    MTD_RCPTS = Column(Numeric)
    MTD_ADJ = Column(Numeric)
    COMMENTS = Column(Text)
    IMIN = Column(Numeric)
    IMAX = Column(Numeric)
    UPCCODE = Column(String)
    POSLOC = Column(String)
    VENDITEMMO = Column(String)
    EXCLUDE = Column(String)
    NDC = Column(String)
    SKU = Column(String)
    AUTO_ORD = Column(Integer)
    FIXED_QTY = Column(Numeric)
    ACTIVE_YN = Column(Integer)
    AVG_UNIT_COST = Column(Numeric)
    location = Column(String)
    item_id = Column(Integer, primary_key=True)
    store_id = Column(
        Integer,
        ForeignKey('csstore.store_id'),
    )
    chemical_id = Column(Integer)
    allocated = Column(Numeric)
    machine_id = Column(Integer)
    special_pkg_ind_cn = Column(Integer)
    refrig_cn = Column(Integer)
    order_multiples_of = Column(Integer)
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
