#coding:utf-8
import builtins
import types
from . import functions

built_in_functions = {}

for name, _build_in in builtins.__dict__.items():
    if isinstance(_build_in, (types.BuiltinFunctionType, types.BuiltinMethodType)):
        built_in_functions[name] = _build_in

for name,_build_in in functions.__dict__.items():
            if isinstance(_build_in,types.FunctionType):
                built_in_functions[name] = _build_in

