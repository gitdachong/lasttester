#coding:utf-8
from lasttester.contrib.db import DbClass
from ...core import constants
from . import base
class Configurer(base.Configurer):

    def __init__(self,config):
        self._config = config
        self._key = constants.KEY_CONFIGURER_INSTANCES
        self._results = {}

    def parse(self):
        driver_type = self._config.get('driver_type','mysql')
        self.instance = DbClass(self._config.get('config_body'), driver_type)
        self._results[self._config.get('name')] = self
        return [(self._key,self._results)]

    def close(self):
        if self.instance:
            self.instance.close()


