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
import imp
import inspect
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..conf.settings import Settings
from .db import Db


Base = declarative_base()


class Carepoint(dict):
    ''' Base CarePoint db connector object '''
    
    BASE = Base
    DEFAULT_DB = 'cph'
    
    # Default path to search for models - change with register_model_dir
    model_path = os.path.join(__file__, '..', 'models')
    
    def __init__(self, server, user, passwd, ):
        
        super(Carepoint, self).__init__()
        self.settings = Settings()
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

    def __get_session(self, model_obj, ):
        return self.env[record_id.__dbname__]()

    def read(self, model_obj, record_id, attributes=None, ):
        """
        Get record by id and return the object
        :param model_obj: Table class to search
        :type model_obj: :class:`sqlalchemy.schema.Table`
        :param record_id: Id of record to manipulate
        :param attributes: Attributes to rcv from db. None for *
        :type attributes: list or None
        :rtype: :class:`sqlalchemy.engine.ResultProxy`
        """
        if attributes is not None:
            raise NotImplementedError('Read attributes not implemented')
        return self.carepoint.query(model_obj).get(record_id)

    def search(self, model_obj, filters=None, ):
        """
        Search table by filters and return records
        :param model_obj: Table class to search
        :type model_obj: :class:`sqlalchemy.schema.Table`
        :param filters: Filters to apply to search
        :type filters: dict or None
        :rtype: :class:`sqlalchemy.engine.ResultProxy`
        """
        if filters is None:
            filters = {}
        return self.carepoint.query(model_obj).filter_by(**filters)
    
    def create(self, model_obj, vals, ):
        """
        Wrapper to create a record in Carepoint
        :param model_obj: Table class to create with
        :type model_obj: :class:`sqlalchemy.schema.Table`
        :param vals: Data to create record with
        :type vals: dict
        :rtype: :class:`sqlalchemy.ext.declarative.Declarative`
        """
        session = self.__get_session(model_obj)
        record = model_obj(**vals)
        session.add(record_id)
        session.commit()
        return record

    def update(self, model_obj, record_id, vals, ):
        """
        Wrapper to update a record in Carepoint
        :param model_obj: Table class to update
        :type model_obj: :class:`sqlalchemy.schema.Table`
        :param record_id: Id of record to manipulate
        :type record_id: int
        :param vals: Data to create record with
        :type vals: dict
        :rtype: :class:`sqlalchemy.ext.declarative.Declarative`
        """
        session = self.__get_session(model_obj)
        session.query(model_obj).get(record_id).update(vals)
        session.commit()
        return session
    
    def delete(self, model_obj, record_id, ):
        """
        Wrapper to delete a record in Carepoint
        :param model_obj: Table class to update
        :type model_obj: :class:`sqlalchemy.schema.Table`
        :param record_id: Id of record to manipulate
        :type record_id: int
        :rtype: bool
        """
        session = self.__get_session(model_obj)
        result_obj = session.query(model_obj).get(record_id)
        assert result_obj.count() == 1
        session.delete(result_obj)
        session.commit()
        return True

    def __getattr__(self, key, ):
        ''' Re-implement __getattr__ to use __getitem__ if attr not found '''
        try:
            return super(Carepoint, self).__getattr__(key)
        except AttributeError:
            try:
                self.__getitem__(key)
            except KeyError:
                raise AttributeError()

    def __getitem__(self, key, retry=True, default=False):
        ''' Re-implement __getitem__ to scan for models if key missing  '''
        try:
            return super(Carepoint, self).__getitem__(key)
        except KeyError:
            if default != False:
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
        '''
        Toggle flag to search for new models before iteration
        @param  bool    refresh     Whether to refresh before iteration
        '''
        self.iter_refresh = refresh
        
    def __refresh_models__(self, ):
        if self.iter_refresh:
            self.find_models()

    def __iter__(self, ):
        ''' Reimplement __iter__ to allow for optional model refresh   '''
        self.__refresh_models__()
        return super(Carepoint, self).__iter__()

    def values(self, ):
        ''' Reimplement values to allow for optional model refresh   '''
        self.__refresh_models__()
        return super(Carepoint, self).values()

    def keys(self, ):
        ''' Reimplement keys to allow for optional model refresh   '''
        self.__refresh_models__()
        return super(Carepoint, self).keys()

    def items(self, ):
        ''' Reimplement items to allow for optional model refresh   '''
        self.__refresh_models__()
        return super(Carepoint, self).items()

    def itervalues(self, ):
        ''' Reimplement itervalues to allow for optional model refresh   '''
        self.__refresh_models__()
        return super(Carepoint, self).itervalues()

    def iterkeys(self, ):
        ''' Reimplement iterkeys to allow for optional model refresh   '''
        self.__refresh_models__()
        return super(Carepoint, self).iterkeys()

    def iteritems(self, ):
        ''' Reimplement iteritems to allow for optional model refresh   '''
        self.__refresh_models__()
        return super(Carepoint, self).iteritems()
    
    def register_model(self, model):
        ''' Registration logic + append to models struct '''
        self[model.__name__] = model
    
    def register_model_dir(self, model_path):
        ''' This function sets the model path to be searched   '''
        if os.path.isdir(model_path):
            self.model_path = model_path
        else:
            raise EnvironmentError('%s is not a directory' % model_path)

    def find_models(self, ):
        ''' Traverse registered model directory and import non-loaded modules  '''
        
        model_path = self.model_path
        if model_path is not None and not os.path.isdir(model_path):
            raise EnvironmentError('%s is not a directory' % model_path)
        
        for dir_name, subdirs, files in os.walk(model_path):
            
            parent_module = dir_name.replace(model_path, '')
            parent_module = parent_module.replace(os.path.sep, '.')
            
            for file_ in files:
                if file_.endswith('.py') and file_ != '__init__.py':
                    module = file_[:-3] #< Strip extension
                    mod_obj = globals().get(module)
                    if mod_obj is None:
                        f, filename, desc = imp.find_module(
                            module, [model_path]
                        )
                        mod_obj = imp.load_module(
                            module, f, filename, desc
                        )
                        cls = [m for m in dir(mod_obj) if not m.startswith('__')]
                        for model_cls in cls:
                            model_obj = getattr(mod_obj, model_cls)
                            if hasattr(model_obj, '__tablename__'):
                                if not hasattr(model_obj, '__dbname__'):
                                    model_obj.__dbname__ = self.DEFAULT_DB
                                self.register_model(model_obj)
