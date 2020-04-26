#coding:utf-8
import dbm
import os
from ..utils import util_path
class CacheDbm():

    def __init__(self,filename = ''):
        self.file_name = 'lasttester_temp_dbm_cache'
        if not filename:
            import tempfile
            filename = os.path.join(tempfile.gettempdir(),self.file_name)
        if util_path.init_path(filename):
            self._db = dbm.open(filename, 'c')
        else:
            self._db = dbm.open(self.file_name, 'c')



    def set(self, key, value):
        self._db[key] = str(value)
        return self

    def delete(self, key):
        if key in self._db.keys():
            del self._db[key]
        return True

    def get(self, key):
        value = self._db.get(key)
        return None if not value else value.decode()

    def __del__(self):
        self._db.close()
