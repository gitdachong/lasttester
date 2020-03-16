#coding:utf-8
import uuid
import time

built_in_variables = {
    '__UUID': lambda : str(uuid.uuid1()),
    '__TIMESTAMP': lambda : int(round(time.time()*1000)),
    '__TIMESTAMP_10':lambda : int(round(time.time())),


}
