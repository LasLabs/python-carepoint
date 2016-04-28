# -*- coding: utf-8 -*-
# © 2016 LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from sqlalchemy import (Column,
                        Integer,
                        DateTime,
                        ForeignKey
                        )


class AddressMixin(object):
    """ This is a mixin for Address Many2Many bindings """

    addr_id = Column(
        Integer,
        ForeignKey('csaddr.addr_id'),
        primary_key=True,
    )
    priority = Column(Integer)
    addr_type_cn = Column(Integer)
    app_flags = Column(Integer)
    timestmp = Column(DateTime)
