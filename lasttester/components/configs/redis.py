#coding:utf-8
import importlib
from ...core import constants
from . import base
class Configurer(base.Configurer):

    def __init__(self,config):
        self._config = config
        self._key = constants.KEY_CONFIGURER_INSTANCES
        self._results = {}

    def parse(self):
        _config = self._config.get('config_body')
        _config.setdefault('decode_responses',True)
        _config.setdefault('db',0)
        redis = None
        try:
            redis = importlib.import_module('redis')
        except:
            pass
        if not redis:
            raise Exception("redis lib doesn't exists,please user command:[pip install redis] to install it first,please!")

        self.instance = redis.ConnectionPool(**_config)
        self._results[self._config.get('name')] = self
        return [(self._key,self._results)]

    def close(self):
        if self.instance:
            self.instance.disconnect()


