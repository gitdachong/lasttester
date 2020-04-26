#coding:utf-8
import shelve
import os
from ..utils import util_path
class CacheShelve():

    def __init__(self,filename = ''):
        self.file_name = 'lasttester_temp_shelve_cache'
        if not filename:
            import tempfile
            filename = os.path.join(tempfile.gettempdir(),self.file_name)
        if util_path.init_path(filename):
            self._db = shelve.open(filename,)
        else:
            self._db = shelve.open(self.file_name)

    def set(self, key, value):
        self._db[key] = value
        return self

    def delete(self, key):
        if key in self._db.keys():
            del self._db[key]
        return True

    def get(self, key):
        return self._db.get(key)

    def __del__(self):
        self._db.close()
