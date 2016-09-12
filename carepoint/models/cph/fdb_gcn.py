# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        Integer,
                        Boolean,
                        String,
                        )


class FdbGcn(Carepoint.BASE):
    __tablename__ = 'fdrgcn'
    __dbname__ = 'cph'

    gcn_seqno = Column(
        Integer, 
        primary_key=True,
        autoincrement=False,
    )
    gcn = Column(String)
    update_yn = Column(Boolean)
