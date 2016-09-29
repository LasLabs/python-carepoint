# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        String,
                        Integer,
                        Boolean,
                        )


class FdbAllergenGroup(Carepoint.BASE):
    __tablename__ = 'fdrdamagd'
    __dbname__ = 'cph'

    dam_agcsp = Column(
        Integer,
        primary_key=True,
    )
    dam_agcspd = Column(
        String(50),
    )
    potentially_inactive = Column(
        Boolean,
    )
    dam_agcsp_status = Column(
        Integer,
    )
