# -*- coding: utf-8 -*-
# © 2015-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


class TestModel(object):
    __tablename__ = '__test__'
    test_col = 'Test'

    @classmethod
    def run(self):
        return True
