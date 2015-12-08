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
import unittest
import mock
from carepoint import Carepoint


class ModelPluginTest(unittest.TestCase):
    
    MODEL_DIR = os.path.join(os.path.dirname(__file__), 'test_models')

    @mock.patch('carepoint.db.carepoint.Db')
    @mock.patch('carepoint.db.carepoint.Settings')
    def setUp(self, settings_mock, db_mock):
        self.cp_args = {
            'user': 'User',
            'passwd': 'Passwd',
            'server': 'Server',
        }
        cp = Carepoint(**self.cp_args)
        cp.register_model_dir(self.MODEL_DIR)
        self.carepoint = cp
        self.settings_mock = settings_mock
        self.db_mock = db_mock

    def test_cph_db_init(self, ):
        self.cp_args['db'] = 'cph'
        self.db_mock.assert_called_once_with(**self.cp_args)
        
    def test_cph_db_assign(self, ):
        self.carepoint.dbs['cph'] = self.db_mock
        
    def test_cph_settings_init(self, ):
        self.settings_mock.assert_called_once_with()

    def test_non_dir(self, ):
        ''' Test to make sure that an EnvironmentError is raised with an invalid model dir '''
        with self.assertRaises(EnvironmentError):
            self.carepoint.register_model_dir(os.path.join(self.MODEL_DIR, 'not_a_dir'))

    def test_model_import_getitem(self, ):
        ''' Test if model is correctly initialized '''
        self.carepoint.find_models()
        result = self.carepoint.get('TestModel', None)
        self.assertNotEqual(result, None)
        
    def test_model_import_getattr(self, ):
        ''' Test if model is correctly initialized '''
        self.carepoint.find_models()
        result = getattr(self.carepoint, 'TestModel', None)
        self.assertIn('TestModel', self.carepoint)
        
    def test_model_methods(self, ):
        ''' Test if model is correctly initialized '''
        self.carepoint.set_iter_refresh()
        model_obj = self.carepoint['TestModel']
        self.assertTrue(model_obj.run()) #< classmethods are exposed

    def test_iter_init_empty(self, ):
        self.assertEqual(len([i for i in self.carepoint]), 0)
    
    def test_values_init_empty(self, ):
        self.assertEqual(len(self.carepoint.values()), 0)
    
    def test_keys_init_empty(self, ):
        self.assertEqual(len(self.carepoint.keys()), 0)
    
    def test_items_init_empty(self, ):
        self.assertEqual(len(self.carepoint.items()), 0)
    
    def test_iteritems_init_empty(self, ):
        self.assertEqual(len([i for i in self.carepoint.iteritems()]), 0)
    
    def test_itervalues_init_empty(self, ):
        self.assertEqual(len([i for i in self.carepoint.itervalues()]), 0)
    
    def test_iterkeys_init_empty(self, ):
        self.assertEqual(len([i for i in self.carepoint.iterkeys()]), 0)

    def test_set_iter_refresh(self, ):
        self.carepoint.set_iter_refresh()
        self.assertTrue(self.carepoint.iter_refresh)

    def test_iter_after_refresh(self, ):
        self.carepoint.set_iter_refresh()
        self.assertEqual(len([i for i in self.carepoint]), 1)

    def test_values_after_refresh(self, ):
        self.carepoint.set_iter_refresh()
        self.assertEqual(len(self.carepoint.values()), 1)

    def test_keys_after_refresh(self, ):
        self.carepoint.set_iter_refresh()
        self.assertEqual(len(self.carepoint.keys()), 1)

    def test_items_after_refresh(self, ):
        self.carepoint.set_iter_refresh()
        self.assertEqual(len(self.carepoint.items()), 1)

    def test_iteritems_after_refresh(self, ):
        self.carepoint.set_iter_refresh()
        self.assertEqual(len([i for i in self.carepoint.iteritems()]), 1)

    def test_itervalues_after_refresh(self, ):
        self.carepoint.set_iter_refresh()
        self.assertEqual(len([i for i in self.carepoint.itervalues()]), 1)

    def test_iterkeys_after_refresh(self, ):
        self.carepoint.set_iter_refresh()
        self.assertEqual(len([i for i in self.carepoint.iterkeys()]), 1)

    def test_wrong_model_getitem(self, ):
        ''' Test to verify that a KeyError is raised for invalid model name '''
        with self.assertRaises(KeyError):
            self.carepoint.set_iter_refresh()
            self.carepoint['ThisIsNotAModelThatExists']
            
    def test_wrong_model_getattr(self, ):
        ''' Test to verify that a KeyError is raised for invalid model name '''
        with self.assertRaises(AttributeError):
            self.carepoint.set_iter_refresh()
            self.carepoint.ThisIsNotAModelThatExists


if __name__ == '__main__':
    unittest.main()
