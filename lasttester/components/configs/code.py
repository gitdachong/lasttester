#coding:utf-8
from lasttester.lib.build_code import BuildCode
class Configurer(object):

    def __init__(self,config):
        self._config = config
        self._key = 'variables'
        self._results = []

    def parse(self):
        config_body = self._config.get('config_body')

        if not config_body:
            return self._results
        elif isinstance(config_body,list):
            for _body in config_body:
                self._results.extend(self._parse(_body))
        elif isinstance(config_body,str):
            self._results.extend(self._parse(config_body))
        return self._results


    def _parse(self,body):
        bc_object = BuildCode(body)
        return [('variables',bc_object.get_variables()),('functions',bc_object.get_functions())]

    def close(self):
        pass




