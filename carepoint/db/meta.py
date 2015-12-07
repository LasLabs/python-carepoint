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
from .struct import Struct


class Meta(type):
    ''' Metaclass to autodetect models '''

    # Default path to search for models - change with register_model_dir
    model_path = None #os.path.join(__file__, '..', 'models') 

    def __init__(cls, name, bases, attrs):
        ''' Initializing mount, or registering a model?    '''
        if not hasattr(cls, 'models'):
            cls.models = Struct(Meta)
        else:
            cls.register_model(cls)
    
    def register_model(cls, model):
        ''' Registration logic + append to models struct '''
        cls.models[model.__name__] = model
    
    @staticmethod
    def register_model_dir(model_path):
        ''' This function sets the model path to be searched   '''
        if os.path.isdir(model_path):
            Meta.model_path = model_path
        else:
            raise EnvironmentError('%s is not a directory' % model_path)
        
    @staticmethod
    def find_models():
        ''' Traverse registered model directory and import non-loaded modules  '''
        
        model_path = Meta.model_path
        if model_path is not None and not os.path.isdir(model_path):
            raise EnvironmentError('%s is not a directory' % model_path)
        
        # for dir_name, subdirs, files in os.walk(model_path):
        #     
        #     parent_module = dir_name.replace(model_path, '')
        #     parent_module = parent_module.replace(os.path.sep, '.')
        #     
        for file_ in os.listdir(model_path):
            if file_.endswith('.py') and file_ != '__init__.py':
                module = file_[:-3] #< Strip extension
                mod_obj = globals().get(module)
                if mod_obj is None:
                    f, filename, desc = imp.find_module(
                        module, [model_path]
                    )
                    globals()[module] = mod_obj = imp.load_module(
                        module, f, filename, desc
                    )

            
            # for file_name in files:
            #     if file_name.endswith('.py') and file_name != '__init__.py':
            #         module = file_[:-3] #< Strip extension
            #         mod_obj = globals().get(module)
            #         if mod_obj is None:
            #             f, filename, desc = imp.find_module(
            #                 module, [model_path]
            #             )
            #             globals()[module] = mod_obj = imp.load_module(
            #                 module, f, filename, desc
            #             )
