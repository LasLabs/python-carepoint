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

class Struct(dict):
    '''
    Subclass dict, re-implement __getitem__ to scan for models
    if a requested key is missing
    '''
    def __init__(self, cls, *args, **kwargs):
        '''
        Init, set mount to PlugPyMount master instance
        @param  PlugPyMount cls
        '''
        self.mount = cls
        super(Struct, self).__init__(*args,**kwargs)

    def __getitem__(self, key, retry=True, default=False):
        ''' Re-implement __getitem__ to scan for models if key missing  '''
        try:
            return super(Struct, self).__getitem__(key)
        except KeyError:
            if default != False:
                return default
            elif retry:
                self.mount.find_models()
                return self.__getitem__(key, False)
            else:
                raise KeyError(
                    'Plugin "%s" not found in model_dir "%s"' % (
                        key, self.mount.model_path
                    )
                )

    def set_iter_refresh(self, refresh=True):
        '''
        Toggle flag to search for new models before iteration
        @param  bool    refresh     Whether to refresh before iteration
        '''
        self.iter_refresh = refresh
        
    def __refresh_models__(self, ):
        if self.iter_refresh:
            self.mount.find_models()

    def __iter__(self):
        ''' Reimplement __iter__ to allow for optional model refresh   '''
        self.__refresh_models__()
        return super(Struct, self).__iter__()

    def values(self):
        ''' Reimplement values to allow for optional model refresh   '''
        self.__refresh_models__()
        return super(Struct, self).values()

    def keys(self):
        ''' Reimplement keys to allow for optional model refresh   '''
        self.__refresh_models__()
        return super(Struct, self).keys()

    def items(self):
        ''' Reimplement items to allow for optional model refresh   '''
        self.__refresh_models__()
        return super(Struct, self).items()

    def itervalues(self):
        ''' Reimplement itervalues to allow for optional model refresh   '''
        self.__refresh_models__()
        return super(Struct, self).itervalues()

    def iterkeys(self):
        ''' Reimplement iterkeys to allow for optional model refresh   '''
        self.__refresh_models__()
        return super(Struct, self).iterkeys()

    def iteritems(self):
        ''' Reimplement iteritems to allow for optional model refresh   '''
        self.__refresh_models__()
        return super(Struct, self).iteritems()
