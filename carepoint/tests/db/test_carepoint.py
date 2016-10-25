# -*- coding: utf-8 -*-
# Copyright 2015-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import os
import unittest
import mock
from contextlib import contextmanager

from carepoint import Carepoint


class EndTestException(Exception):
    pass


class CarepointTest(unittest.TestCase):

    MODEL_DIR = os.path.join(os.path.dirname(__file__), 'test_models')

    @mock.patch('carepoint.db.carepoint.Db')
    def setUp(self, db_mock):
        self.cp_args = {
            'user': 'User',
            'passwd': 'Passwd',
            'server': 'Server',
        }
        cp = Carepoint(**self.cp_args)
        cp.register_model_dir(self.MODEL_DIR)
        self.carepoint = cp
        self.db_mock = db_mock

    def __get_model_obj(self):
        self.carepoint.find_models()
        model_obj = self.carepoint['TestModel']
        return model_obj

    @contextmanager
    def __get_mock_session(self, unwrapped=True):
        with mock.patch.object(self.carepoint, '_get_model_session') as mk:
            enter, session = mock.MagicMock(), mock.MagicMock()
            enter.return_value = enter
            mk.return_value = session
            session.__enter__.return_value = enter
            yield enter if unwrapped else mk

    #
    # Test Initializations and other core stuff
    #

    @mock.patch('carepoint.db.carepoint.Db')
    @mock.patch('carepoint.db.carepoint.super')
    def test_carepoint_init(self, sup_mk, db_mk):
        cp = Carepoint(**self.cp_args)
        sup_mk.assert_called_once_with(Carepoint, cp)

    def test_carepoint_initial_iter_refresh(self):
        self.assertFalse(
            self.carepoint.iter_refresh
        )

    def test_carepoint_assigns_instance_env(self):
        self.assertTrue(
            self.carepoint.env['cph'],
        )

    def test_cph_db_init(self):
        self.assertTrue(
            self.carepoint.dbs['cph']
        )

    def test_cph_db_assign(self):
        self.carepoint.dbs['cph'] = self.db_mock

    def test_carepoint_assigns_db_params(self):
        """ It should assign the database params as an instance var """
        self.assertIsInstance(self.carepoint.db_params, dict)

    def test_non_dir(self):
        '''
        Test to make sure that an EnvironmentError is raised with an
        invalid model dir
        '''
        with self.assertRaises(EnvironmentError):
            self.carepoint.register_model_dir(
                os.path.join(self.MODEL_DIR, 'not_a_dir'))

    def test_model_import_getitem(self):
        ''' Test if model is correctly initialized '''
        self.carepoint.find_models()
        result = self.carepoint.get('TestModel', None)
        self.assertNotEqual(result, None)

    def test_model_import_getattr(self):
        ''' Test if model is correctly initialized '''
        self.carepoint.find_models()
        self.assertIn('TestModel', self.carepoint)

    def test_model_methods(self):
        ''' Test if model is correctly initialized '''
        self.carepoint.set_iter_refresh()
        model_obj = self.carepoint['TestModel']
        self.assertTrue(model_obj.run())  # < classmethods are exposed

    def test_init_env_clear(self):
        """ It should clear the global environment when True """
        with mock.patch.object(self.carepoint, 'dbs') as dbs:
            dbs.clear.side_effect = EndTestException
            with self.assertRaises(EndTestException):
                self.carepoint._init_env(True)

    #
    # Test the session handler
    #

    def test_get_model_session_gets_session(self):
        """ It should get session for the database """
        model_obj = self.__get_model_obj()
        with mock.patch.object(self.carepoint, 'env') as env:
            with self.carepoint._get_model_session(model_obj):
                pass
            env[model_obj.__dbname__].assert_called_once_with()

    def test_get_model_session_yields_session(self):
        """ It should yield session for the database """
        model_obj = self.__get_model_obj()
        with mock.patch.object(self.carepoint, 'env') as env:
            with self.carepoint._get_model_session(model_obj) as res:
                self.assertEqual(
                    env[model_obj.__dbname__](),
                    res,
                )

    def test_get_model_session_commit(self):
        """ It should commit session after yield """
        model_obj = self.__get_model_obj()
        with mock.patch.object(self.carepoint, 'env') as env:
            with self.carepoint._get_model_session(model_obj):
                pass
            env[model_obj.__dbname__]().commit.assert_called_once_with()

    def test_get_model_session_rollback(self):
        """ It should roll session back on error """
        model_obj = self.__get_model_obj()
        with mock.patch.object(self.carepoint, 'env') as env:
            env[model_obj.__dbname__]().commit.side_effect = EndTestException
            with self.assertRaises(EndTestException):
                with self.carepoint._get_model_session(model_obj):
                    pass
            env[model_obj.__dbname__]().rollback.assert_called_once_with()

    def test_get_model_session_close(self):
        """ It should always close session """
        model_obj = self.__get_model_obj()
        with mock.patch.object(self.carepoint, 'env') as env:
            with self.carepoint._get_model_session(model_obj):
                pass
            env[model_obj.__dbname__]().close.assert_called_once_with()

    #
    # Test the SMB handlers
    #

    def test_smb_prefix(self):
        expect = 'smb://%s:%s@' % (self.cp_args['user'],
                                   self.cp_args['passwd'])
        self.assertEqual(
            expect, self.carepoint._smb_prefix,
            'SMB prefix not correct. Expect %s - Got %s' % (
                expect, self.carepoint._smb_prefix,
            )
        )

    @mock.patch('carepoint.db.carepoint.urllib2')
    @mock.patch('carepoint.db.carepoint.SMBHandler')
    def test_get_file_builds_opener(self, smb_mk, url_mk):
        self.carepoint.get_file('expect')
        url_mk.build_opener.assert_called_once_with(smb_mk)

    @mock.patch('carepoint.db.carepoint.urllib2')
    @mock.patch('carepoint.db.carepoint.SMBHandler')
    def test_get_file_opens_uri(self, smb_mk, url_mk):
        expect = 'Test'
        self.carepoint.get_file(expect)
        url_mk.build_opener().open.assert_called_once_with(
            '%s%s' % (self.carepoint._smb_prefix, expect)
        )

    @mock.patch('carepoint.db.carepoint.urllib2')
    @mock.patch('carepoint.db.carepoint.SMBHandler')
    def test_get_file_returns_opened_handler(self, smb_mk, url_mk):
        expect = 'Test'
        res = self.carepoint.get_file(expect)
        self.assertEqual(
            url_mk.build_opener().open(), res,
        )

    @mock.patch('carepoint.db.carepoint.urllib2')
    @mock.patch('carepoint.db.carepoint.SMBHandler')
    def test_send_file_builds_opener(self, smb_mk, url_mk):
        self.carepoint.send_file('expect', '')
        url_mk.build_opener.assert_called_once_with(smb_mk)

    @mock.patch('carepoint.db.carepoint.urllib2')
    @mock.patch('carepoint.db.carepoint.SMBHandler')
    def test_send_file_sends_file(self, smb_mk, url_mk):
        expect = 'Test'
        data = 'data'
        self.carepoint.send_file(expect, data)
        url_mk.build_opener().__enter__().open.assert_called_once_with(
            '%s%s' % (self.carepoint._smb_prefix, expect), data=data,
        )

    @mock.patch('carepoint.db.carepoint.urllib2')
    @mock.patch('carepoint.db.carepoint.SMBHandler')
    def test_send_file_returns_true(self, smb_mk, url_mk):
        res = self.carepoint.send_file('expect', '')
        self.assertTrue(res)

    #
    # Test the database convenience handlers
    #

    # Read

    def test_read_calls_query_with_model_obj(self):
        model_obj = self.__get_model_obj()
        record_id = 1
        with self.__get_mock_session() as mk:
            self.carepoint.read(model_obj, record_id)
            mk.query.assert_called_once_with(model_obj)

    def test_read_calls_get_with_record_id(self):
        model_obj = self.__get_model_obj()
        record_id = 1
        with self.__get_mock_session() as mk:
            mk.query.return_value = query_mk = mock.MagicMock()
            self.carepoint.read(model_obj, record_id)
            query_mk.get.assert_called_once_with(record_id)

    def test_read_returns_response(self):
        model_obj = self.__get_model_obj()
        record_id = 1
        expect = 'Response'
        with self.__get_mock_session() as mk:
            mk.query.return_value = query_mk = mock.MagicMock()
            query_mk.get.return_value = expect
            response = self.carepoint.read(model_obj, record_id)
            self.assertEqual(response, expect)

    # Search
    def test_search_calls_query_with_model_obj(self):
        filters = {'test_col': 'Test'}
        with self.__get_mock_session() as mk:
            model_obj = self.__get_model_obj()
            self.carepoint.search(model_obj, filters)
            mk.query.assert_called_once_with(model_obj)

    def test_search_calls_filter_with_filters(self):
        model_obj = self.__get_model_obj()
        filters = {'test_col': 'Test'}
        with self.__get_mock_session() as mk:
            mk.query.return_value = query_mk = mock.MagicMock()
            self.carepoint.search(model_obj, filters)
            query_mk.filter.assert_called_once_with(
                *self.carepoint._unwrap_filters(model_obj, filters)
            )

    def test_search_calls_filter_when_no_filters(self):
        model_obj = self.__get_model_obj()
        with self.__get_mock_session() as mk:
            mk.query.return_value = query_mk = mock.MagicMock()
            self.carepoint.search(model_obj)
            query_mk.filter.assert_called_once_with(**{})

    def test_search_returns_response(self):
        model_obj = self.__get_model_obj()
        filters = {'test_col': 'Test'}
        with self.__get_mock_session() as mk:
            with mock.patch.object(self.carepoint, 'read') as read_mk:
                response = self.carepoint.read(model_obj, filters)
                self.assertEqual(
                    read_mk(),
                    response,
                )

    # Get Next Sequence

    def test_get_next_sequence_session(self):
        """ It should get session for db """
        expect = 'expect'
        with mock.patch.object(self.carepoint, '_get_session') as mk:
            res = self.carepoint.get_next_sequence(None, expect)
            mk.assert_called_once_with(expect)

    @mock.patch('carepoint.db.carepoint.text')
    def test_get_next_sequence_execute(self, text):
        """ It should execute stored procedure on connection """
        expect = 'expect'
        with mock.patch.object(self.carepoint, '_get_session') as mk:
            self.carepoint.get_next_sequence(expect)
            mk().__enter__().connection().execute.assert_called_once_with(
                text(), seq_name=expect,
            )

    def test_get_next_sequence_fetch(self):
        """ It should return result of fetch """
        with mock.patch.object(self.carepoint, '_get_session') as mk:
            res = self.carepoint.get_next_sequence(None)
            expect = mk().__enter__().connection().execute().fetchall()[0][0]
            self.assertEqual(
                expect, res,
            )

    # Create
    def test_create_calls_get_model_session_with_model_obj(self):
        model_obj = mock.MagicMock()
        with self.__get_mock_session(False) as mk:
            self.carepoint.create(model_obj, {})
            mk.assert_called_once_with(model_obj)

    def test_create_initializes_new_model_obj_with_vals(self):
        model_obj = mock.MagicMock()
        vals = {'test_col': 'Test'}
        with self.__get_mock_session() as mk:
            self.carepoint.create(model_obj, vals)
            model_obj.assert_called_once_with(**vals)

    def test_create_adds_new_record_to_session(self):
        model_obj = mock.MagicMock()
        response_expect = 'ResponseExpect'
        model_obj.return_value = response_expect
        vals = {'test_col': 'Test'}
        with self.__get_mock_session() as mk:
            self.carepoint.create(model_obj, vals)
            mk.add.assert_called_once_with(response_expect)

    def test_create_returns_new_record(self):
        model_obj = mock.MagicMock()
        response_expect = 'ResponseExpect'
        model_obj.return_value = response_expect
        vals = {'test_col': 'Test'}
        with self.__get_mock_session() as mk:
            response = self.carepoint.create(model_obj, vals)
            self.assertEqual(response, response_expect)

    # Update
    def test_update_calls_get_model_session_with_model_obj(self):
        model_obj = self.__get_model_obj()
        record_id = 1
        with self.__get_mock_session(False) as mk:
            with mock.patch.object(self.carepoint, 'read'):
                self.carepoint.update(model_obj, record_id, {})
                mk.assert_called_once_with(model_obj)

    def test_update_calls_read_with_model_and_record_id(self):
        model_obj = self.__get_model_obj()
        record_id = 1
        vals = {'test_col': 'Test'}
        with self.__get_mock_session():
            with mock.patch.object(self.carepoint, 'read') as read_mk:
                self.carepoint.update(model_obj, record_id, vals)
                read_mk.assert_called_once_with(model_obj, record_id)

    def test_update_calls_update_with_vals(self):
        model_obj = self.__get_model_obj()
        record_id = 1
        vals = {'test_col': 'Test'}
        with self.__get_mock_session() as mk:
            mk.query.return_value = query_mk = mock.MagicMock()
            query_mk.get.return_value = get_mk = mock.MagicMock()
            self.carepoint.update(model_obj, record_id, vals)
            self.assertEqual(
                mk().query().get().test_col,
                get_mk.test_col,
                'Record attribute was not updated. Expect Test, Got %s' % (
                    get_mk.test_col,
                )
            )

    def test_update_returns_record(self):
        model_obj = self.__get_model_obj()
        record_id = 1
        vals = {'test_col': 'Test'}
        with self.__get_mock_session() as mk:
            with mock.patch.object(self.carepoint, 'read') as read:
                response = self.carepoint.update(model_obj, record_id, vals)
                self.assertEqual(read(), response)

    # Delete
    def test_delete_calls_get_model_session_with_model_obj(self):
        model_obj = self.__get_model_obj()
        record_id = 1
        with self.__get_mock_session(False) as mk:
            with mock.patch.object(self.carepoint, 'read') as read_mk:
                read_mk.return_value = read_mk
                read_mk.count.return_value = 0
                self.carepoint.delete(model_obj, record_id)
                mk.assert_called_once_with(model_obj)

    def test_delete_calls_read_with_model_and_record_id(self):
        model_obj = self.__get_model_obj()
        record_id = 1
        with self.__get_mock_session():
            with mock.patch.object(self.carepoint, 'read') as read_mk:
                read_mk.return_value = read_mk
                read_mk.count.return_value = 0
                self.carepoint.delete(model_obj, record_id)
                read_mk.assert_called_once_with(model_obj, record_id)

    def test_delete_asserts_result_count_eq_1(self):
        model_obj = self.__get_model_obj()
        record_id = 1
        with self.__get_mock_session():
            with mock.patch.object(self.carepoint, 'read') as read_mk:
                read_mk.return_value = read_mk
                read_mk.count.return_value = 2
                with self.assertRaises(AssertionError):
                    self.carepoint.delete(model_obj, record_id)

    def test_delete_calls_session_delete_with_record_result(self):
        model_obj = self.__get_model_obj()
        record_id = 1
        expect_return = mock.MagicMock()
        with self.__get_mock_session() as mk:
            with mock.patch.object(self.carepoint, 'read') as read_mk:
                read_mk.return_value = expect_return
                expect_return.count.return_value = 1
                self.carepoint.delete(model_obj, record_id)
                mk.delete.assert_called_once_with(expect_return)

    def test_delete_returns_false_on_no_records(self):
        model_obj = self.__get_model_obj()
        record_id = 1
        with self.__get_mock_session():
            with mock.patch.object(self.carepoint, 'read') as read_mk:
                read_mk.return_value = read_mk
                read_mk.count.return_value = 0
                response = self.carepoint.delete(model_obj, record_id)
                self.assertFalse(response)

    def test_delete_returns_true_on_delete(self):
        model_obj = self.__get_model_obj()
        record_id = 1
        with self.__get_mock_session():
            with mock.patch.object(self.carepoint, 'read') as read_mk:
                read_mk.return_value = read_mk
                read_mk.count.return_value = 1
                response = self.carepoint.delete(model_obj, record_id)
                self.assertTrue(response)

    #
    # Test filter criterion generators
    #

    def __setup_criterion_test(self, operator, query='Query'):
        self.carepoint.find_models()
        model_obj = self.carepoint['TestModel']
        attr_name = 'test_col'
        col_obj = getattr(model_obj, attr_name)
        return [col_obj, model_obj, attr_name, operator, query]

    def test_create_criterion_returns_correct_double_eq(self):
        args = self.__setup_criterion_test('==')
        self.assertEqual(
            self.carepoint._create_criterion(*args[1:]),
            args[0] == args[-1]
        )

    def test_create_criterion_returns_correct_eq(self):
        args = self.__setup_criterion_test('=')
        self.assertEqual(
            self.carepoint._create_criterion(*args[1:]),
            args[0] == args[-1]
        )

    def test_create_criterion_returns_correct_lt(self):
        args = self.__setup_criterion_test('<')
        self.assertEqual(
            self.carepoint._create_criterion(*args[1:]),
            args[0] < args[-1]
        )

    def test_create_criterion_returns_correct_le(self):
        args = self.__setup_criterion_test('<=')
        self.assertEqual(
            self.carepoint._create_criterion(*args[1:]),
            args[0] <= args[-1]
        )

    def test_create_criterion_returns_correct_gt(self):
        args = self.__setup_criterion_test('>')
        self.assertEqual(
            self.carepoint._create_criterion(*args[1:]),
            args[0] > args[-1]
        )

    def test_create_criterion_returns_correct_ge(self):
        args = self.__setup_criterion_test('>=')
        self.assertEqual(
            self.carepoint._create_criterion(*args[1:]),
            args[0] >= args[-1]
        )

    def test_create_criterion_raises_not_implemented_error(self):
        args = self.__setup_criterion_test('===')
        with self.assertRaises(KeyError):
            self.carepoint._create_criterion(*args[1:])

    def test_create_criterion_raises_attribute_error(self):
        args = self.__setup_criterion_test('==')
        args[2] = 'Nope'
        with self.assertRaises(AttributeError):
            self.carepoint._create_criterion(*args[1:])

    #
    # Test filter dictionary unwrapping
    #

    def test_unwrap_filters_empty(self):
        model_obj = self.__get_model_obj()
        expect = []
        self.assertEqual(
            self.carepoint._unwrap_filters(model_obj, {}), expect,
        )

    def test_unwrap_filters_none(self):
        model_obj = self.__get_model_obj()
        expect = []
        self.assertEqual(
            self.carepoint._unwrap_filters(model_obj), expect,
        )

    def test_unwrap_filters_dict(self):
        model_obj = self.__get_model_obj()
        col_expect = 'test_col'
        query_expect = ['test_1', 'test_2', ]
        ops_expect = ['>=', '==', ]
        filters = {
            col_expect: {
                ops_expect[0]: query_expect[0],
                ops_expect[1]: query_expect[1],
            }
        }
        expect = [
            mock.call(model_obj, col_expect, ops_expect[0], query_expect[0]),
            mock.call(model_obj, col_expect, ops_expect[1], query_expect[1]),
        ]
        with mock.patch.object(self.carepoint, '_create_criterion') as mk:
            self.carepoint._unwrap_filters(model_obj, filters)
            mk.assert_has_calls(expect, any_order=True)

    def test_unwrap_filters_str(self):
        model_obj = self.__get_model_obj()
        col_expect = 'test_col'
        query_expect = 'test_1'
        op_expect = '=='
        filters = {col_expect: query_expect}
        with mock.patch.object(self.carepoint, '_create_criterion') as mk:
            self.carepoint._unwrap_filters(model_obj, filters)
            mk.assert_called_once_with(
                model_obj, col_expect, op_expect, query_expect
            )

    def test_unwrap_filters_returns_list(self):
        model_obj = self.__get_model_obj()
        self.assertIsInstance(
            self.carepoint._unwrap_filters(model_obj), list
        )

    #
    # Test dictionary overrides for model lookups
    #

    def test_iter_init_empty(self):
        self.assertEqual(len([i for i in self.carepoint]), 0)

    def test_values_init_empty(self):
        self.assertEqual(len(self.carepoint.values()), 0)

    def test_keys_init_empty(self):
        self.assertEqual(len(self.carepoint.keys()), 0)

    def test_items_init_empty(self):
        self.assertEqual(len(self.carepoint.items()), 0)

    def test_iteritems_init_empty(self):
        self.assertEqual(len([i for i in self.carepoint.iteritems()]), 0)

    def test_itervalues_init_empty(self):
        self.assertEqual(len([i for i in self.carepoint.itervalues()]), 0)

    def test_iterkeys_init_empty(self):
        self.assertEqual(len([i for i in self.carepoint.iterkeys()]), 0)

    def test_set_iter_refresh(self):
        self.carepoint.set_iter_refresh()
        self.assertTrue(self.carepoint.iter_refresh)

    def test_iter_after_refresh(self):
        self.carepoint.set_iter_refresh()
        self.assertEqual(len([i for i in self.carepoint]), 1)

    def test_values_after_refresh(self):
        self.carepoint.set_iter_refresh()
        self.assertEqual(len(self.carepoint.values()), 1)

    def test_keys_after_refresh(self):
        self.carepoint.set_iter_refresh()
        self.assertEqual(len(self.carepoint.keys()), 1)

    def test_items_after_refresh(self):
        self.carepoint.set_iter_refresh()
        self.assertEqual(len(self.carepoint.items()), 1)

    def test_iteritems_after_refresh(self):
        self.carepoint.set_iter_refresh()
        self.assertEqual(len([i for i in self.carepoint.iteritems()]), 1)

    def test_itervalues_after_refresh(self):
        self.carepoint.set_iter_refresh()
        self.assertEqual(len([i for i in self.carepoint.itervalues()]), 1)

    def test_iterkeys_after_refresh(self):
        self.carepoint.set_iter_refresh()
        self.assertEqual(len([i for i in self.carepoint.iterkeys()]), 1)

    def test_wrong_model_getitem(self):
        ''' Test to verify that a KeyError is raised for invalid model name '''
        with self.assertRaises(KeyError):
            self.carepoint.set_iter_refresh()
            self.carepoint['ThisIsNotAModelThatExists']

    def test_wrong_model_getattr(self):
        ''' Test to verify that a KeyError is raised for invalid model name '''
        with self.assertRaises(AttributeError):
            self.carepoint.set_iter_refresh()
            self.carepoint.ThisIsNotAModelThatExists

if __name__ == '__main__':
    unittest.main()
