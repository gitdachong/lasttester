#coding:utf-8
import os
from imp import find_module,load_module
import sys
config_plugins = []


def load_components_config(pluginPath):
    if not os.path.isdir(pluginPath):
        return False
    items = os.listdir(pluginPath)
    for item in items:
        if os.path.isdir(os.path.join(pluginPath, item)):
            load_components_config(pluginPath)
        else:
            if item.endswith('.py') and item != '__init__.py':
                moduleName = item[:-3]
                print(moduleName)
                if moduleName not in sys.modules:
                    fileHandle, filePath, dect = find_module(moduleName, [pluginPath])
                try:
                    moduleObj = load_module(moduleName, fileHandle, filePath, dect)
                finally:
                    if fileHandle: fileHandle.close()
