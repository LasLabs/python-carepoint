# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        String,
                        Integer,
                        ForeignKey,
                        )


class FdbAttr(Carepoint.BASE):
    __tablename__ = 'fdbriptdes'
    __dbname__ = 'cph'

    IPTDESCID = Column(Integer, primary_key=True)
    IPTCATID = Column(
        Integer,
        ForeignKey('fdbriptcat.IPTCATID'),
        primary_key=True,
    )
    IPTBSCDID = Column(Integer)
    IPTDESC = Column(String)
