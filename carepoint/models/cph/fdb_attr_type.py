# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        String,
                        Integer,
                        )


class FdbAttrType(Carepoint.BASE):
    __tablename__ = 'fdbriptcat'
    __dbname__ = 'cph'

    IPTCATID = Column(
        Integer, 
        primary_key=True,
        autoincrement=False,
    )
    IPTCATDESC = Column(String)
