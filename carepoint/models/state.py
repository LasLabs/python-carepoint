# -*- coding: utf-8 -*-
# Copyright 2016 LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import enum


class EnumOrderState(enum.Enum):
    """ It provides PEP-0435 compliant Carepoint State Enumerable """

    entered = 10
    verified = 20
    adjudicated = 30
    processed = 35
    approved = 40
    shipped = 50
    returned = 60
