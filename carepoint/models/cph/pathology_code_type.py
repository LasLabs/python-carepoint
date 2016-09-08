# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        String,
                        )


class PathologyCodeType(Carepoint.BASE):
    __tablename__ = 'fdrfmlitd_10'
    __dbname__ = 'cph'

    icd_cd_type = Column(
        String,
        primary_key=True,
    )
    icd_cd_type_desc = Column(
        String,
    )
