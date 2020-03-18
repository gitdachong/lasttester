from lasttester.components.configs.ftp import Configurer
import os

config = Configurer({
    'name':'ftp',
    'config_body':{
        'host':'47.52.143.180',
        'port':'21',
        'username':'test123',
        'password':'weiwei123456',
    }
})

key,value  = config.parse()[0]
ftp = value.get('ftp')
print(ftp)
# config.upload('/5/','/Users/scott/Downloads/test/1')
config.download('/5/','/Users/scott/Downloads/test/111/')
# config.delete('/')
config.close()
