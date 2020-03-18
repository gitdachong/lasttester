#coding:utf-8
from ..configs.base import Configurer

class Sampler(object):

    def __init__(self,test_data,**kwargs):
        self.test_content = test_data
        self.request = {}
        self.response = {'status_code':0}
        self.sampler_name = 'base'
        self.instance = None
        if 'instance' in kwargs:
            _instance = kwargs.get('instance')
            if not _instance or not isinstance(_instance,Configurer):
                raise Exception(r"instance {} doesn't exists".format(self.test_content.get('instance')))
            self.instance = _instance.instance

    def run_test(self):
        pass