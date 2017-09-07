# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import enum

from sqlalchemy import (Column,
                        Integer,
                        DateTime,
                        ForeignKey,
                        )
from sqlalchemy.types import Enum
from sqlalchemy.ext.declarative import declared_attr


class EnumImageType(enum.Enum):
    """Provide a PEP-0435 compliant Carepoint Image Type Enumerable."""

    prescription = 2
    unknown_3 = 3
    unknown_7 = 7
    unknown_1001 = 1001
