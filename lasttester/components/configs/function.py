#coding:utf-8

class Configurer(object):

    def __init__(self,config):
        self._config = config
        self._key = 'functions'
        self._results = {}

    def parse(self):
        config_body = self._config.get('config_body')
        self._results = self._parse(config_body)
        return [(self._key,self._results)]


    def _parse(self,body):
        _result = {}
        if isinstance(body, dict):
            _result = body
        elif isinstance(body, list):
            for _item in body:
                _result.update(self._parse(_item))
        return _result

    def close(self):
        pass




