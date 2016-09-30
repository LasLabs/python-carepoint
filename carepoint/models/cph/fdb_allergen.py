# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        String,
                        Integer,
                        Boolean,
                        ForeignKey,
                        )


class FdbAllergen(Carepoint.BASE):
    __tablename__ = 'fdrhicl'
    __dbname__ = 'cph'

    hicl_seqno = Column(
        Integer,
        ForeignKey('fdrhiclsq.hicl_seqno'),
        primary_key=True,
    )
    hic_seqn = Column(
        Integer,
        ForeignKey('fdrhicd.hic_seqn'),
        primary_key=True,
    )
    hic_rel_no = Column(
        Integer,
    )
    hic = Column(
        String(6),
        ForeignKey('fdrhicd.hic'),
    )
    update_yn = Column(
        Boolean,
    )
