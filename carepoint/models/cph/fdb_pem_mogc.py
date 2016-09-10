# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        Integer,
                        Boolean,
                        ForeignKey,
                        )


class FdbPemMogc(Carepoint.BASE):
    __tablename__ = 'fdrpemogc'
    __dbname__ = 'cph'

    gcn_seqno = Column(
        Integer, 
        primary_key=True,
        autoincrement=False,
    )
    pemono = Column(
        Integer,
        ForeignKey('fdrpemmoe.pemono'),
        primary_key=True,
    )
    update_yn = Column(Boolean)
