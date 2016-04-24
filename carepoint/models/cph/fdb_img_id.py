# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        String,
                        Integer,
                        )


class FdbImgId(Carepoint.BASE):
    __tablename__ = 'fdbrimgudg'
    __dbname__ = 'cph'

    IMGUNIQID = Column(Integer, primary_key=True)
    IMGDFID = Column(Integer)
    IMGNDC = Column(String)
    IMGMFGID = Column(Integer)
