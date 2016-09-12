# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        String,
                        Integer,
                        ForeignKey,
                        )


class FdbAttr(Carepoint.BASE):
    __tablename__ = 'fdbriptdes'
    __dbname__ = 'cph'

    IPTDESCID = Column(
        Integer, 
        primary_key=True,
        autoincrement=False,
    )
    IPTCATID = Column(
        Integer,
        ForeignKey('fdbriptcat.IPTCATID'),
        primary_key=True,
    )
    IPTBSCDID = Column(
        Integer,
        ForeignKey('fdbriptbsc.IPTBSCDID'),
    )
    IPTDESC = Column(String)
