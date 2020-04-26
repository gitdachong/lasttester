#coding:utf-8
import os

def init_path(filename):
    if not filename:
        return False
    if os.path.exists(filename):
        return True
    path = os.path.split(filename)[0]
    if os.path.exists(path):
        return True
    os.makedirs(path)
    if os.path.exists(path):
        return True
    return False