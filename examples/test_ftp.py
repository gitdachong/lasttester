from lasttester.components.configs.ftp import Configurer


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
config.upload('/2/tg_image_1338043360.jpeg','/Users/scott/Downloads/tg_image_1338043360.jpeg')
config.close()
