#coding:utf-8

class Cache():

    def __init__(self,type='file',**kwargs):
        self.cacheInstance = None
        if type =='file':
            from .lib.FileCache import FileCache
            self.cacheInstance = FileCache(kwargs.get('file'))

    def set(self,key,value):
        return self.cacheInstance.set(key,value)

    def get(self,key):
        return self.cacheInstance.get(key)

    def delete(self,key):
        return self.cacheInstance.delete(key)

    def call_mothod(self,method,*args,**kwargs):
        if hasattr(self.cacheInstance,method):
            return self.cacheInstance.method(*args,**kwargs)
        return False
