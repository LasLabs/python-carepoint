# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Dave Lasley <dave@laslabs.com>
#    Copyright: 2015 LasLabs, Inc [https://laslabs.com]
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

import os
from unittest import TestCase
from carepoint.db import *


class ModelPluginTest(TestCase):
    
    MODEL_DIR = os.path.join(os.path.dirname(__file__), 'test_models')

    def setUp(self, ):
        Meta.register_model_dir(self.MODEL_DIR)

    def test_non_dir(self, ):
        ''' Test to make sure that an EnvironmentError is raise with an invalid model dir '''
        with self.assertRaises(EnvironmentError):
            Meta.register_model_dir(
                os.path.join(self.MODEL_DIR, 'not_a_dir')
            )

    def test_model(self, ):
        ''' Test if model is correctly initialized '''
        model_obj = Carepoint.models['TestModel']
        self.assertIsInstance(model_obj, PlugPy) #< Needs to be of type PlugPy, verifies import
        self.assertTrue(model_obj.initialized) #< Plugin was initialized
        self.assertTrue(model_obj.run()) #< Methods are exposed

    def test_iter_init_empty(self, ):
        for i in Carepoint.models:
            print "MODEL - %s " % i
        self.assertEqual(len([i for i in Carepoint.models]), 0)

    def test_values_init_empty(self, ):
        self.assertEqual(len(Carepoint.models.values()), 0)

    def test_keys_init_empty(self, ):
        self.assertEqual(len(Carepoint.models.keys()), 0)

    def test_items_init_empty(self, ):
        self.assertEqual(len(Carepoint.models.items()), 0)

    def test_iteritems_init_empty(self, ):
        self.assertEqual(len([i for i in Carepoint.models.iteritems()]), 0)

    def test_itervalues_init_empty(self, ):
        self.assertEqual(len([i for i in Carepoint.models.itervalues()]), 0)

    def test_iterkeys_init_empty(self, ):
        self.assertEqual(len([i for i in Carepoint.models.iterkeys()]), 0)

    def test_set_iter_refresh(self, ):
        Carepoint.models.set_iter_refresh()
        self.assertTrue(Carepoint.models.iter_refresh)

    def test_iter_after_refresh(self, ):
        Carepoint.models.set_iter_refresh()
        self.assertEqual(len([i for i in Carepoint.models]), 1)

    def test_values_after_refresh(self, ):
        Carepoint.models.set_iter_refresh()
        self.assertEqual(len(Carepoint.models.values()), 1)

    def test_keys_after_refresh(self, ):
        Carepoint.models.set_iter_refresh()
        self.assertEqual(len(Carepoint.models.keys()), 1)

    def test_items_after_refresh(self, ):
        Carepoint.models.set_iter_refresh()
        self.assertEqual(len(Carepoint.models.items()), 1)

    def test_iteritems_after_refresh(self, ):
        Carepoint.models.set_iter_refresh()
        self.assertEqual(len([i for i in Carepoint.models.iteritems()]), 1)

    def test_itervalues_after_refresh(self, ):
        Carepoint.models.set_iter_refresh()
        self.assertEqual(len([i for i in Carepoint.models.itervalues()]), 1)

    def test_iterkeys_after_refresh(self, ):
        Carepoint.models.set_iter_refresh()
        self.assertEqual(len([i for i in Carepoint.models.iterkeys()]), 1)

    def test_wrong_model(self, ):
        ''' Test to verify that a KeyError is raised for invalid model name '''
        with self.assertRaises(KeyError):
            Carepoint.models['ThisIsNotAModelThatExists'] #< Fake
