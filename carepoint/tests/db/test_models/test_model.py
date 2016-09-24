# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).


class TestModel(object):
    __tablename__ = '__test__'
    __dbname__ = 'cph'
    test_col = 'Test'

    @classmethod
    def run(self):
        return True
