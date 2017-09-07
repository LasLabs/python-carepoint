# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import unittest
from sqlalchemy.schema import Table
from carepoint.tests.db.db import DatabaseTest
from carepoint.models.cph.image_data import ImageData


class TestImageData(DatabaseTest):

    def test_table_initialization(self):
        self.assertIsInstance(ImageData.__table__, Table)

    def test_compute_image_path(self):
        """It should return the full image path."""
        image = ImageData(
            RootFolderName='root',
            FullFileName='file',
        )
        self.assertEqual(image.image_path, 'root/file')

    def test_image_type(self):
        """It should return the canonical name for the type."""
        image = ImageData(
            image_type_cn=2,
        )
        self.assertEqual(image.image_type, 'prescription')


if __name__ == '__main__':
    unittest.main()
