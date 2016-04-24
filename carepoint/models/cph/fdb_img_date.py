# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        DateTime,
                        Integer,
                        )


class FdbImgDate(Carepoint.BASE):
    __tablename__ = 'fdbrimguij'
    __dbname__ = 'cph'

    IMGUNIQID = Column(Integer, primary_key=True)
    IMGSTRTDT = Column(DateTime)
    IMGSTOPDT = Column(DateTime)
    IMGID = Column(Integer)
