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
                        )


class Phone(Carepoint.BASE):
    __tablename__ = 'csphone'
    __dbname__ = 'cph'

    phone_id = Column(
        Integer, 
        primary_key=True,
        autoincrement=False,
    )
    parent_phone_id = Column(
        Integer,
        ForeignKey('csphone.phone_id'),
    )
    inherited_yn = Column(Boolean)
    owner_type_cn = Column(Integer)
    area_code = Column(String)
    phone_no = Column(String)
    extension = Column(String)
    when_in_use = Column(String)
    anote = Column(String)
    app_flags = Column(Integer)
    timestmp = Column(DateTime)
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
