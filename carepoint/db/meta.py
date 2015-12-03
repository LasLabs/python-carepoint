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
from .db import Struct, Base


class Meta(type):
    ''' Metaclass to autodetect models '''

    # Default path to search for models - change with register_model_dir
    model_path = os.path.join(__file__, 'models') 

    def __init__(self, name, bases, attrs):
        ''' Initializing mount, or registering a model?    '''
        if not hasattr(self, 'models'):
            self.models = Struct(Base)
        else:
            self.register_model(self)
    
    def register_model(self, model):
        ''' Registration logic + append to models struct '''
        self.models[model.__class__.__name__] = models
    
    @staticmethod
    def register_model_dir(model_path):
        ''' This function sets the model path to be searched   '''
        if os.path.isdir(model_path):
            Base.model_path = model_path
        else:
            raise EnvironmentError('%s is not a directory' % model_path)
        
    @staticmethod
    def find_models():
        ''' Traverse registered model directory and import non-loaded modules  '''
        
        model_path = Base.model_path
        if not os.path.isdir(model_path):
            raise EnvironmentError('%s is not a directory' % model_path)
        
        for dir_name, subdirs, files in os.walk(model_path):
            for file_name in files:
                if file_name.endswith('.py') and file_name != '__init__.py':
                    module = file_[:-3] #< Strip extension
                    mod_obj = globals().get(module)
                    if mod_obj is None:
                        f, filename, desc = imp.find_module(
                            module, [model_path]
                        )
                        globals()[module] = mod_obj = imp.load_module(
                            module, f, filename, desc
                        )
