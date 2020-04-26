#coding:utf-8
class Cache():

    def __init__(self,type='shelve',**kwargs):
        self.cacheInstance = None
        if type =='dbm':
            from .base.cache_dbm import CacheDbm
            self.cacheInstance = CacheDbm(kwargs.get('file'))
        elif type =='shelve':
            from .base.cache_shelve import CacheShelve
            self.cacheInstance = CacheShelve(kwargs.get('file'))


    def set(self,key,value):
        return self.cacheInstance.set(key,value)

    def get(self,key,default = None):
        return self.cacheInstance.get(key,default)

    def delete(self,key):
        return self.cacheInstance.delete(key)

    def call_mothod(self,method,*args,**kwargs):
        if hasattr(self.cacheInstance,method):
            return self.cacheInstance.method(*args,**kwargs)
        return False
