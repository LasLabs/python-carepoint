# -*- coding: utf-8 -*-
# Copyright 2017-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

from carepoint import Carepoint
from sqlalchemy import (Column,
                        DateTime,
                        ForeignKey,
                        Integer,
                        String,
                        Numeric,
                        )


class ImageData(Carepoint.BASE):
    __tablename__ = 'cpimage_data'
    __dbname__ = 'cph'

    image_id = Column(
        Integer,
        # Column is not actually a primary key in DB.
        primary_key=True,
    )
    image_type_cn = Column(
        Integer,
    )
    related_id = Column(
        Integer,
        # Column is not actually a primary key in DB.
        primary_key=True,
    )
    RootFolderName = Column(
        String,
    )
    FullFileName = Column(
        String,
    )
    related_store_id = Column(
        Integer,
        ForeignKey('csstore.store_id'),
    )
    related_pat_id = Column(
        Integer,
        ForeignKey('cppat.pat_id'),
    )
    add_user_id = Column(
        Integer,
        ForeignKey('csuser.user_id'),
    )
    add_date = Column(DateTime)
    chg_user_id = Column(
        Integer,
        ForeignKey('csuser.user_id'),
    )
    chg_date = Column(DateTime)
    image_path = property(lambda s: s._compute_image_path())

    def _compute_image_path(self):
        return '%s/%s' % (self.RootFolderName, self.FullFileName)
