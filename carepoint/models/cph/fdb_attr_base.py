# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        String,
                        Integer,
                        ForeignKey,
                        )


class FdbAttrBase(Carepoint.BASE):
    __tablename__ = 'fdbriptbsc'
    __dbname__ = 'cph'

    IPTBSCDID = Column(Integer, primary_key=True)
    IPTCATID = Column(
        Integer,
        ForeignKey('fdbriptcat.IPTCATID'),
        primary_key=True,
    )
    IPTBSCDESC = Column(String)
