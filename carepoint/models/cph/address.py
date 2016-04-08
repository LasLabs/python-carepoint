# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from carepoint import Carepoint
from .user import User
from sqlalchemy import (Column,
                        Integer,
                        String,
                        DateTime,
                        Boolean,
                        ForeignKey,
                        )


class Address(Carepoint.BASE):
    __tablename__ = 'csaddr'
    __dbname__ = 'cph'

    addr_id = Column(Integer, primary_key=True)
    parent_addr_id = Column(
        Integer,
        ForeignKey('csaddr.addr_id'),
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
    timestmp = Column(DateTime)
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
