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
    
    PLUGIN_DIR = os.path.join(os.path.dirname(__file__), 'test_models')

    def setUp(self, ):
        Meta.register_model_dir(self.PLUGIN_DIR)

    def test_non_dir(self, ):
        ''' Test to make sure that an EnvironmentError is raise with an invalid model dir '''
        with self.assertRaises(EnvironmentError):
            Meta.register_model_dir(
                os.path.join(self.PLUGIN_DIR, 'not_a_dir')
            )

    def test_model(self, ):
        ''' Test if model is correctly initialized '''
        model_obj = Carepoint.models['TestModel']
        self.assertIsInstance(model_obj, PlugPy) #< Needs to be of type PlugPy, verifies import
        self.assertTrue(model_obj.initialized) #< Plugin was initialized
        self.assertTrue(model_obj.run()) #< Methods are exposed
        
    def test_iter(self, ):
        ''' Test to verify correct reimplemention of lookups  '''
        models = Carepoint.models
        
        #   These should all be zero because the models haven't been scanned
        self.assertEqual(len([i for i in models]), 0) #< __iter__
        self.assertEqual(len(models.values()), 0) #< values
        self.assertEqual(len(models.keys()), 0) #< keys
        self.assertEqual(len(models.items()), 0) #< itervalues
        self.assertEqual(len([i for i in models.iteritems()]), 0) #< iteritems
        self.assertEqual(len([i for i in models.itervalues()]), 0) #< itervalues
        self.assertEqual(len([i for i in models.iterkeys()]), 0) #< iterkeys
        
        #   Set to scan and retry iters, there should now be one model
        PlugPy.models.set_iter_refresh()
        self.assertTrue(Carepoint.models.iter_refresh)
        self.assertEqual(len([i for i in models]), 1) #< __iter__
        self.assertEqual(len(models.values()), 1) #< values
        self.assertEqual(len(models.keys()), 1) #< keys
        self.assertEqual(len(models.items()), 1) #< itervalues
        self.assertEqual(len([i for i in models.iteritems()]), 1) #< iteritems
        self.assertEqual(len([i for i in models.itervalues()]), 1) #< itervalues
        self.assertEqual(len([i for i in models.iterkeys()]), 1) #< iterkeys
        
    def test_wrong_model(self, ):
        ''' Test to verify that a KeyError is raised for invalid model name '''
        with self.assertRaises(KeyError):
            Carepoint.models['ThisIsNotAModelThatExists'] #< Fake
