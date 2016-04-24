# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        Integer,
                        )


class FdbImg(Carepoint.BASE):
    __tablename__ = 'fdbrimgimg'
    __dbname__ = 'cph'

    IMGID = Column(Integer, primary_key=True)
    IMGFILENM = Column(Integer)
