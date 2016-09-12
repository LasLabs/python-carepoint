# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from carepoint.models.address_mixin import AddressMixin
from sqlalchemy import (Column,
                        Integer,
                        )


class OrganizationAddress(AddressMixin, Carepoint.BASE):
    __dbname__ = 'cph'
    __tablename__ = 'csorg_addr'
    org_id = Column(
        Integer, 
        primary_key=True,
        autoincrement=False,
    )
