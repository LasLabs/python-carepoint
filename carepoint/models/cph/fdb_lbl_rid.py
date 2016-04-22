# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        String,
                        Boolean,
                        )


class FdbLblRid(Carepoint.BASE):
    __tablename__ = 'fdrlblrid'
    __dbname__ = 'cph'

    lblrid = Column(String, primary_key=True)
    mfg = Column(String)
    update_yn = Column(Boolean)
