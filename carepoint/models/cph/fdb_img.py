# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from sqlalchemy.orm import relationship
from sqlalchemy import (Column,
                        String,
                        Numeric,
                        )


class FdbImg(Carepoint.BASE):
    __tablename__ = 'fdbrimgimg'
    __dbname__ = 'cph'

    IMGID = Column(
        Numeric(10, 0),
        primary_key=True,
    )
    IMGFILENM = Column(
        String,
    )
    IMAGE_ROOTS = relationship(
        'StoreParam',
        primaryjoin=""" and_(
            remote(literal_column('1')) == foreign(StoreParam.store_id),
            'SC_MOD_IMAGE_ROOT' == foreign(StoreParam.param_code)
        ) """,
        viewonly=True,
        innerjoin=True,
    )
    IMAGE_PATH = property(lambda s: s._compute_image_path())

    def _compute_image_path(self):
        root = self.IMAGE_ROOTS[0].data_value.strip().strip('\\')
        root = root.replace('\\', '/')
        return '%s/%s.JPG' % (root, self.IMGFILENM.strip())
