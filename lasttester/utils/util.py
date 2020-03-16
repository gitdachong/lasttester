#coding:utf-8
import time
import uuid

def get_current_timestamp_13():
    return int(round(time.time() * 1000))

def get_uuid_str():
    return str(uuid.uuid1())

