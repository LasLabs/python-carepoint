# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        Integer,
                        ForeignKey,
                        )


class Account(Carepoint.BASE):
    __tablename__ = 'cp_acct'
    __dbname__ = 'cph'

    ID = Column(Integer, primary_key=True)
    pat_id = Column(
        Integer,
        ForeignKey('cppat.pat_id'),
    )
    acct_type_cn = Column(Integer)
    resp_pty_yn = Column(Integer)
    chromis_id = Column(Integer)
