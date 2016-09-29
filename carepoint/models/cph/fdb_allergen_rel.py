# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        String,
                        Integer,
                        Boolean,
                        )


class FdbAllergenRel(Carepoint.BASE):
    __tablename__ = 'fdrhicd'
    __dbname__ = 'cph'

    hic_seqn = Column(
        Integer,
    )
    hic = Column(
        String(6),
        primary_key=True,
    )
    hic_desc = Column(
        String(50),
    )
    hic_root = Column(
        Integer,
    )
    potentially_inactive = Column(
        Integer,
    )
    ing_status = Column(
        Integer,
    )
    update_yn = Column(
        Boolean,
    )
