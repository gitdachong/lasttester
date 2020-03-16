#coding:utf-8
import importlib

class Configurer(object):

    def __init__(self,config):
        self._config = config
        self._key = 'instances'
        self._results = {}
        self._instance = None

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
        self._instance = redis.ConnectionPool(**_config)
        self._results[self._config.get('name')] = self._instance
        return [(self._key,self._results)]

    def close(self):
        if self._instance:
            self._instance.disconnect()


