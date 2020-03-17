#coding:utf-8
from lasttester.contrib.db import DbClass

class Configurer(object):

    def __init__(self,config):
        self._config = config
        self._key = 'instances'
        self._results = {}
        self._instance = None

    def parse(self):
        driver_type = self._config.get('driver_type','mysql')
        self._instance = DbClass(self._config.get('config_body'), driver_type)
        self._results[self._config.get('name')] = self._instance
        return [(self._key,self._results)]

    def close(self):
        if self._instance:
            self._instance.close()


