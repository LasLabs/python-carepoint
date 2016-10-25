# -*- coding: utf-8 -*-
# Copyright 2016-TODAY LasLabs Inc.
# License MIT (https://opensource.org/licenses/MIT).

import imp
import operator
import os
import urllib2

from contextlib import contextmanager

from sqlalchemy import bindparam
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text


from .db import Db
from smb.SMBHandler import SMBHandler


Base = declarative_base()
Base.get = lambda s, k, v=None: getattr(s, k, v)
Base.__getitem__ = lambda s, k, v=None: getattr(s, k, v)
Base.__setitem__ = lambda s, k, v: setattr(s, k, v)


models, env, dbs = {}, {}, {}


class Carepoint(dict):
    """ Base CarePoint db connector object """

    BASE = Base
    DEFAULT_DB = 'cph'

    # Default path to search for models - change with register_model_dir
    model_path = os.path.join(os.path.dirname(__file__), '..', 'models')

    FILTERS = {
        '>=': operator.ge,
        '>': operator.gt,
        '<=': operator.le,
        '<': operator.lt,
        '=': operator.eq,
        '==': operator.eq,
    }

    def __init__(
        self, server, user, passwd, smb_user=None, smb_passwd=None,
        db_args=None, **engine_args
    ):
        """ It initializes new Carepoint object

        Args:
            server (str): IP or Hostname to database
            user (str): Username for database
            passwd (str): Password for database
            smb_user (str): Username to use for SMB connection, ``None`` to
                use the database user
            smd_passwd (str): Password to use for the SMB connection, ``None``
                to use the database password
            db_args (dict): Dictionary of arguments to send during initial
                db creation
            **engine_args (mixed): Kwargs to pass to ``create_engine``
        """

        super(Carepoint, self).__init__()
        global dbs
        self.env = {}
        self.dbs = dbs
        self.iter_refresh = False
        params = {
            'user': user,
            'passwd': passwd,
            'server': server,
            'db': 'cph',
        }
        if db_args is not None:
            params.update(db_args)
        if engine_args:
            params.update(engine_args)
        if smb_user is None:
            self.smb_creds = {
                'user': user,
                'passwd': passwd,
            }
        else:
            self.smb_creds = {
                'user': smb_user,
                'passwd': smb_passwd,
            }
        self.db_params = params
        self._init_env(False)

    def _init_env(self, clear=False):
        """ It initializes the global db and environments

        Params:
            clear: (bool) True to clear the global session
        """
        if clear:
            self.dbs.clear()
        # @TODO: Lazy load, once other dbs needed
        if not self.dbs.get('cph'):
            self.dbs['cph'] = Db(**self.db_params)
        if not self.env.get('cph'):
            self.env['cph'] = sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self.dbs['cph'],
                expire_on_commit=True,
            )

    def _get_model_session(self, model_obj):
        """ It yields a session for the model_obj """
        return self._get_session(model_obj.__dbname__)

    @contextmanager
    def _get_session(self, db_name):
        session = self.env[db_name]()
        try:
            yield session
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

    @property
    def _smb_prefix(self):
        """ Return URI prefix for SMB share """
        return 'smb://{user}:{passwd}@'.format(**self.smb_creds)

    def get_file(self, path):
        """ Return a file-like object for the SMB path

        Args:
            path: :type:`str` SMB path to fetch

        Returns:
            :type:`file` File interface object representing remote resource
        """
        opener = urllib2.build_opener(SMBHandler)
        return opener.open('%s%s' % (self._smb_prefix, path))

    def send_file(self, path, file_obj):
        """ Send a file-like object to the SMB path

        Args:
            path: :type:`str` SMB path to fetch
            file_obj: :type:`file` File interface object to send to server

        Returns:
            :type:`bool` Success
        """
        with urllib2.build_opener(SMBHandler) as opener:
            opener.open('%s%s' % (self._smb_prefix, path), data=file_obj)
        return True

    def _create_criterion(self, model_obj, col_name, operator, query):
        """ Create a SQLAlchemy criterion from filter parts

        Args:
            model_obj: :class:`sqlalchemy.Table` Table class to search
            col_name: :type:`str` Name of column to query
            operator: :type:`str` Domain operator to use in query
            query: :type:`str` Text to search for

        Returns:
            SQLAlchemy criterion representing a single WHERE clause

        Raises:
            NotImplementedError: When query operator is not implemented
            AttributeError: When col_name does not exist in the model_obj
        """

        try:
            col_obj = getattr(model_obj, col_name)
            operator_obj = self.FILTERS[operator]
            return operator_obj(col_obj, query)

        except KeyError:
            raise

        except AttributeError:
            raise

    def _unwrap_filters(self, model_obj, filters=None):
        """ Unwrap a dictionary of filters into something usable by SQLAlchemy
        :param model_obj: Table class to search
        :type model_obj: :class:`sqlalchemy.Table`
        :param filters: Filters, keyed by col name
        :type filters: dict
        :rtype: list
        """

        if filters is None:
            filters = {}

        new_filters = []
        for col_name, col_filter in filters.items():

            if isinstance(col_filter, dict):
                for _operator, _filter in col_filter.items():
                    new_filters.append(self._create_criterion(
                        model_obj, col_name, _operator, _filter
                    ))

            else:
                new_filters.append(self._create_criterion(
                    model_obj, col_name, '==', col_filter
                ))

        return new_filters

    def _create_entities(self, model_obj, cols):
        """ Return list of entities matching cols
        :param model_obj: Table class to search
        :type model_obj: :class:`sqlalchemy.Table`
        :param cols: List of col names
        :type cols: list
        :rtype: :type:`list` of :class:`sqlalchemy.Column`
        """
        out = []
        for col in cols:
            try:
                out.append(getattr(model_obj, col))
            except AttributeError:
                pass
        return out

    def read(self, model_obj, record_id, with_entities=None):
        """ Get record by id and return the object
        :param model_obj: Table class to search
        :type model_obj: :class:`sqlalchemy.Table`
        :param record_id: Id of record to manipulate
        :param with_entities: Attributes to rcv from db. None for *
        :type with_entities: list or None
        :param with_entities: List of col names to select, None for all
        :type with_entities: list or None
        :rtype: :class:`sqlalchemy.engine.ResultProxy`
        """
        with self._get_model_session(model_obj) as session:
            res = session.query(model_obj).get(record_id)
            if with_entities:
                res.with_entities(*self._create_entities(
                    model_obj, with_entities
                ))
            return res

    def search(self, model_obj, filters=None, with_entities=None):
        """ Search table by filters and return records
        :param model_obj: Table class to search
        :type model_obj: :class:`sqlalchemy.schema.Table`
        :param filters: Filters to apply to search
        :type filters: dict or None
        :param with_entities: List of col names to select, None for all
        :type with_entities: list or None
        :rtype: :class:`sqlalchemy.engine.ResultProxy`
        """
        with self._get_model_session(model_obj) as session:
            if filters is None:
                filters = {}
            filters = self._unwrap_filters(model_obj, filters)
            res =  session.query(model_obj).filter(*filters)
            if with_entities:
                res.with_entities(*self._create_entities(
                    model_obj, with_entities
                ))
            return res

    def create(self, model_obj, vals):
        """ Wrapper to create a record in Carepoint
        :param model_obj: Table class to create with
        :type model_obj: :class:`sqlalchemy.schema.Table`
        :param vals: Data to create record with
        :type vals: dict
        :rtype: :class:`sqlalchemy.ext.declarative.Declarative`
        """
        with self._get_model_session(model_obj) as session:
            record = model_obj(**vals)
            session.add(record)
            return record

    def update(self, model_obj, record_id, vals):
        """ Wrapper to update a record in Carepoint
        :param model_obj: Table class to update
        :type model_obj: :class:`sqlalchemy.schema.Table`
        :param record_id: Id of record to manipulate
        :type record_id: int
        :param vals: Data to create record with
        :type vals: dict
        :rtype: :class:`sqlalchemy.ext.declarative.Declarative`
        """
        with self._get_model_session(model_obj) as session:
            record = self.read(model_obj, record_id)
            for key, val in vals.items():
                setattr(record, key, val)
            return record

    def delete(self, model_obj, record_id):
        """ Wrapper to delete a record in Carepoint
        :param model_obj: Table class to update
        :type model_obj: :class:`sqlalchemy.schema.Table`
        :param record_id: Id of record to manipulate
        :type record_id: int
        :return: Whether the record was found, and deleted
        :rtype: bool
        """
        with self._get_model_session(model_obj) as session:
            record = self.read(model_obj, record_id)
            result_cnt = record.count()
            if result_cnt == 0:
                return False
            assert result_cnt == 1
            session.delete(record)
        return True

    def get_pks(self, model_obj):
        """ Return the Primary keys in the model
        :param model_obj: Table class to update
        :type model_obj: :class:`sqlalchemy.schema.Table`
        :return: Tuple of primary key name strings
        :rtype: tuple
        """
        return tuple(k.name for k in inspect(model_obj).primary_key)

    def get_next_sequence(self, sequence_name, db_name='cph'):
        """ It generates and returns the next int in sequence
        Params:
            sequence_name: ``str`` Name of the sequence in Carepoint DB
            db_name: ``str`` Name of DB containing sequence stored proc
        Return:
            Integer to use as pk
        """
        with self._get_session(db_name) as session:  
            res = session.connection().execute(
                text(
                    "SET NOCOUNT ON;"
                    "DECLARE @out int = 0;"
                    "EXEC CsGenerateIntId :seq_name, @out output;"
                    "SELECT @out;"
                    "SET NOCOUNT OFF;",
                    bindparams=[bindparam('seq_name')],
                ),
                seq_name=sequence_name,
            )
            id_int = res.fetchall()[0][0]
            return id_int

    def __getattr__(self, key):
        """ Re-implement __getattr__ to use __getitem__ if attr not found """
        try:
            return super(Carepoint, self).__getattr__(key)
        except AttributeError:
            try:
                self.__getitem__(key)
            except KeyError:
                raise AttributeError()

    def __setitem__(self, key, val, __global=False, *args, **kwargs):
        """ Re-implement __setitem__ to allow for global model sync """
        super(Carepoint, self).__setitem__(key, val, *args, **kwargs)
        if not __global:
            global models
            models[key] = val

    def __getitem__(self, key, retry=True, default=False):
        """ Re-implement __getitem__ to scan for models if key missing  """
        global models
        for k, v in models.iteritems():
            self.__setitem__(k, v, True)
        try:
            return super(Carepoint, self).__getitem__(key)
        except KeyError:
            if default is not False:
                return default
            elif retry:
                self.find_models()
                return self.__getitem__(key, False)
            else:
                raise KeyError(
                    'Plugin "%s" not found in model_dir "%s"' % (
                        key, self.model_path
                    )
                )

    def set_iter_refresh(self, refresh=True):
        """ Toggle flag to search for new models before iteration
        :param refresh: Whether to refresh before iteration
        :type refresh: bool
        """
        self.iter_refresh = refresh

    def __refresh_models__(self):
        if self.iter_refresh:
            self.find_models()

    def __iter__(self):
        """ Reimplement __iter__ to allow for optional model refresh """
        self.__refresh_models__()
        return super(Carepoint, self).__iter__()

    def values(self):
        """ Reimplement values to allow for optional model refresh """
        self.__refresh_models__()
        return super(Carepoint, self).values()

    def keys(self):
        """ Reimplement keys to allow for optional model refresh """
        self.__refresh_models__()
        return super(Carepoint, self).keys()

    def items(self):
        """ Reimplement items to allow for optional model refresh """
        self.__refresh_models__()
        return super(Carepoint, self).items()

    def itervalues(self):
        """ Reimplement itervalues to allow for optional model refresh """
        self.__refresh_models__()
        return super(Carepoint, self).itervalues()

    def iterkeys(self):
        """ Reimplement iterkeys to allow for optional model refresh """
        self.__refresh_models__()
        return super(Carepoint, self).iterkeys()

    def iteritems(self):
        """ Reimplement iteritems to allow for optional model refresh """
        self.__refresh_models__()
        return super(Carepoint, self).iteritems()

    def register_model(self, model_obj):
        """ Registration logic + append to models struct
        :param model_obj: Model object to register
        :type model_obj: :class:`sqlalchemy.ext.declarative.Declarative`
        """
        self[model_obj.__name__] = model_obj

    def register_model_dir(self, model_path):
        """ This function sets the model path to be searched
        :param model_path: Path of models
        :type model_path: str
        """
        if os.path.isdir(model_path):
            self.model_path = model_path
        else:
            raise EnvironmentError('%s is not a directory' % model_path)

    def find_models(self, model_path=None):
        """ Traverse registered model directory and import non-loaded modules
        """

        if model_path is None:
            model_path = self.model_path

        if model_path is not None and not os.path.isdir(model_path):
            raise EnvironmentError('%s is not a directory' % model_path)

        for dir_name, subdirs, files in os.walk(model_path):

            if dir_name.startswith('__'):
                continue
            dir_name = os.path.abspath(dir_name)
            parent_module = dir_name.replace(model_path, '')
            parent_module = parent_module.replace(os.path.sep, '.')

            for file_ in files:
                if file_.endswith('.py') and file_ != '__init__.py':
                    module = file_[:-3]
                    mod_obj = globals().get(module)
                    if mod_obj is None:
                        f, filename, desc = imp.find_module(
                            module, [dir_name]
                        )
                        mod_obj = imp.load_module(
                            module, f, filename, desc
                        )
                        cls = [
                            m for m in dir(mod_obj) if not m.startswith('__')
                        ]
                        for model_cls in cls:
                            model_obj = getattr(mod_obj, model_cls)
                            if hasattr(model_obj, '__tablename__'):
                                if not hasattr(model_obj, '__dbname__'):
                                    model_obj.__dbname__ = self.DEFAULT_DB
                                self.register_model(model_obj)
