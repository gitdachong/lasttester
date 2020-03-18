#coding:utf-8
from . import base

class Sampler(base.Sampler):


    def __init__(self,test_content,**kwargs):
        super().__init__(test_content,**kwargs)
        self.sampler_name = 'redis'


    def run(self):
        self.request = self.test_content.get('request')
        if not isinstance(self.request,dict):
            return
        import redis
        self.__redis = redis.Redis(connection_pool=self.instance)
        self.__redis.set('b',2)
        self.request['text'] = str(self.request)
        _method = getattr(self.__redis,self.request.get('method'))
        args = self.request.get('args',[])
        kwargs = self.request.get('kwargs',{})

        if _method:
            self.response['text'] = _method(*args,**kwargs)
            self.response['json'] = str(self.response['text'])
        self.response['status_code'] = 200
        return self.response

    def __del__(self):
        try:
            self.__redis.close()
        except:
            pass















