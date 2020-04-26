from lasttester.contrib.cache import Cache

ca = Cache()
# ca.set('a',1)
temp = ca.get('a')
print(type(temp),temp)
