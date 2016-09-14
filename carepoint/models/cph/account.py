# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        Integer,
                        ForeignKey,
                        )


class Account(Carepoint.BASE):
    __tablename__ = 'cp_acct'
    __dbname__ = 'cph'

    pat_id = Column(
        Integer,
        ForeignKey('cppat.pat_id'),
        primary_key=True,
    )
    ID = Column(
        Integer,
        primary_key=True,
    )
    acct_type_cn = Column(Integer)
    resp_pty_yn = Column(Integer)
    chromis_id = Column(Integer)
