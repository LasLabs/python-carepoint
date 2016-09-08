# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        String,
                        DateTime,
                        Numeric,
                        Text,
                        ForeignKey,
                        )


class Pathology(Carepoint.BASE):
    __tablename__ = 'fdrfmlinm_10'
    __dbname__ = 'cph'

    icd_cd = Column(
        String,
        primary_key=True,
    )
    icd_cd_type = Column(
        String,
        ForeignKey('fdrfmlitd_10.icd_cd_type'),
        primary_key=True,
    )
    icd_desc = Column(Text)
    icd_desc_source_cd = Column(String)
    icd_status_cd = Column(String)
    icd_first_dt = Column(DateTime)
    icd_last_dt = Column(DateTime)
    icd_billable_ind = Column(Numeric(1, 0))
