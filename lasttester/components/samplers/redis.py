#coding:utf-8
from . import base

class Sampler(base.Sampler):


    def __init__(self,test_content,**kwargs):
        super().__init__(test_content)
        self.sampler_name = 'redis'
        if 'instance' in kwargs:
            self.__instance = kwargs.get('instance')
        if not self.__instance:
            raise Exception(r"redis instance {} doesn't exists".format(self.test_content.get('instance')))


    def run(self):
        self.request_parsed = self.test_content.get('request')
        if not isinstance(self.request_parsed,dict):
            return
        import redis
        self.__redis = redis.Redis(connection_pool=self.__instance)
        self.__redis.set('b',2)
        self.request = str(self.request_parsed)
        _method = getattr(self.__redis,self.request_parsed.get('method'))
        args = self.request_parsed.get('args',[])
        kwargs = self.request_parsed.get('kwargs',{})
        if _method:
            self.response_parsed = _method(*args,**kwargs)
        self.response =str(self.response_parsed)
        self.status_code = 200
        return self.response_parsed

    def __del__(self):
        try:
            self.__redis.close()
        except:
            pass















