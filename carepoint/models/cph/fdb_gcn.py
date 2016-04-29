# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        Integer,
                        Boolean,
                        String,
                        )


class FdbGcn(Carepoint.BASE):
    __tablename__ = 'fdrgcn'
    __dbname__ = 'cph'

    gcn_seqno = Column(Integer, primary_key=True)
    gcn = Column(String)
    update_yn = Column(Boolean)
