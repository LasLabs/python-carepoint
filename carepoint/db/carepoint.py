# -*- coding: utf-8 -*-
# © 2016-TODAY LasLabs Inc.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import os
import imp
import operator
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.inspection import inspect
from .db import Db

Base = declarative_base()

import pdb


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

    def __init__(self, server, user, passwd, ):

        super(Carepoint, self).__init__()
        self.iter_refresh = False
        params = {
            'user': user,
            'passwd': passwd,
            'server': server,
            'db': 'cph',
        }
        #   @TODO: Lazy load, once other dbs needed
        self.dbs = {
            'cph': Db(**params),
        }
        self.env = {
            'cph': sessionmaker(bind=self.dbs['cph']),
        }
        self.sessions = {}

    def _get_session(self, model_obj, ):
        try:
            return self.sessions[model_obj.__dbname__]
        except KeyError:
            session = self.env[model_obj.__dbname__]()
            self.sessions[model_obj.__dbname__] = session
            return session

    def _create_criterion(self, model_obj, col_name, operator, query, ):
        """ Create a SQLAlchemy criterion from filter parts
        :param model_obj: Table class to search
        :type model_obj: :class:`sqlalchemy.schema.Table`
        :param col_name: Name of column to query
        :type col_name: str
        :param operator: Domain operator to use in query
        :type operator: str
        :param query: Text to search for
        :type query: str
        :return: SQLAlchemy criterion representing a single WHERE clause
        :raises NotImplementedError: When query operator is not implemented
        :raises AttributeError: When col_name does not exist in the model_obj
        """

        try:
            col_obj = getattr(model_obj, col_name)
            operator_obj = self.FILTERS[operator]
            return operator_obj(col_obj, query)

        except KeyError:
            raise

        except AttributeError:
            raise

    def _unwrap_filters(self, model_obj, filters=None, ):
        """ Unwrap a dictionary of filters into something usable by SQLAlchemy
        :param model_obj: Table class to search
        :type model_obj: :class:`sqlalchemy.schema.Table`
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

    def read(self, model_obj, record_id, attributes=None, ):
        """ Get record by id and return the object
        :param model_obj: Table class to search
        :type model_obj: :class:`sqlalchemy.schema.Table`
        :param record_id: Id of record to manipulate
        :param attributes: Attributes to rcv from db. None for *
        :type attributes: list or None
        :rtype: :class:`sqlalchemy.engine.ResultProxy`
        """
        if attributes is not None:
            raise NotImplementedError('Read attributes not implemented')
        session = self._get_session(model_obj)
        return session.query(model_obj).get(record_id)

    def search(self, model_obj, filters=None, ):
        """ Search table by filters and return records
        :param model_obj: Table class to search
        :type model_obj: :class:`sqlalchemy.schema.Table`
        :param filters: Filters to apply to search
        :type filters: dict or None
        :rtype: :class:`sqlalchemy.engine.ResultProxy`
        """
        if filters is None:
            filters = {}
        session = self._get_session(model_obj)
        return session.query(model_obj).filter_by(**filters)

    def create(self, model_obj, vals, ):
        """ Wrapper to create a record in Carepoint
        :param model_obj: Table class to create with
        :type model_obj: :class:`sqlalchemy.schema.Table`
        :param vals: Data to create record with
        :type vals: dict
        :rtype: :class:`sqlalchemy.ext.declarative.Declarative`
        """
        session = self._get_session(model_obj)
        record_id = model_obj(**vals)
        session.add(record_id)
        session.commit()
        return record_id

    def update(self, model_obj, record_id, vals, ):
        """ Wrapper to update a record in Carepoint
        :param model_obj: Table class to update
        :type model_obj: :class:`sqlalchemy.schema.Table`
        :param record_id: Id of record to manipulate
        :type record_id: int
        :param vals: Data to create record with
        :type vals: dict
        :rtype: :class:`sqlalchemy.ext.declarative.Declarative`
        """
        session = self._get_session(model_obj)
        self.read(model_obj, record_id).update(vals)
        session.commit()
        return session

    def delete(self, model_obj, record_id, ):
        """ Wrapper to delete a record in Carepoint
        :param model_obj: Table class to update
        :type model_obj: :class:`sqlalchemy.schema.Table`
        :param record_id: Id of record to manipulate
        :type record_id: int
        :return: Whether the record was found, and deleted
        :rtype: bool
        """
        session = self._get_session(model_obj)
        result_obj = self.read(model_obj, record_id)
        result_cnt = result_obj.count()
        if result_obj.count() == 0:
            return False
        assert result_cnt == 1
        session.delete(result_obj)
        session.commit()
        return True

    def get_pks(self, model_obj):
        """ Return the Primary keys in the model
        :param model_obj: Table class to update
        :type model_obj: :class:`sqlalchemy.schema.Table`
        :return: Tuple of primary key name strings
        :rtype: tuple
        """
        return tuple(k.name for k in inspect(model_obj).primary_key)

    def __getattr__(self, key, ):
        """ Re-implement __getattr__ to use __getitem__ if attr not found """
        try:
            return super(Carepoint, self).__getattr__(key)
        except AttributeError:
            try:
                self.__getitem__(key)
            except KeyError:
                raise AttributeError()

    def __getitem__(self, key, retry=True, default=False):
        """ Re-implement __getitem__ to scan for models if key missing  """
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

    def set_iter_refresh(self, refresh=True, ):
        """ Toggle flag to search for new models before iteration
        :param refresh: Whether to refresh before iteration
        :type refresh: bool
        """
        self.iter_refresh = refresh

    def __refresh_models__(self, ):
        if self.iter_refresh:
            self.find_models()

    def __iter__(self, ):
        """ Reimplement __iter__ to allow for optional model refresh """
        self.__refresh_models__()
        return super(Carepoint, self).__iter__()

    def values(self, ):
        """ Reimplement values to allow for optional model refresh """
        self.__refresh_models__()
        return super(Carepoint, self).values()

    def keys(self, ):
        """ Reimplement keys to allow for optional model refresh """
        self.__refresh_models__()
        return super(Carepoint, self).keys()

    def items(self, ):
        """ Reimplement items to allow for optional model refresh """
        self.__refresh_models__()
        return super(Carepoint, self).items()

    def itervalues(self, ):
        """ Reimplement itervalues to allow for optional model refresh """
        self.__refresh_models__()
        return super(Carepoint, self).itervalues()

    def iterkeys(self, ):
        """ Reimplement iterkeys to allow for optional model refresh """
        self.__refresh_models__()
        return super(Carepoint, self).iterkeys()

    def iteritems(self, ):
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
                        #pdb.set_trace()
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
