# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        String,
                        Integer,
                        Boolean,
                        )


class FdbAllergenDesc(Carepoint.BASE):
    __tablename__ = 'fdrhiclsq'
    __dbname__ = 'cph'

    hicl_seqno = Column(
        Integer,
        primary_key=True,
    )
    gnn = Column(
        String(30),
    )
    gnn60 = Column(
        String(60),
    )
    update_yn = Column(
        Boolean,
    )
