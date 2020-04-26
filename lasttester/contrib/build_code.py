#coding:utf-8
import types
import sys
NO_INCLUDE_ATTRIBUTES = ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__builtins__']
class BuildCode(object):
    module = types.ModuleType("_Mixter_BuildCode_Repeatable")
    def __init__(self,buildCode_code_str,global_variables = {},out = False):
        super().__init__()
        self._global_variables = global_variables
        self.module.__dict__.update(self._global_variables)
        self._error = ''
        self._buffer = ''
        self._functions = {}
        self._modules = {}
        self._variables = {}
        self.current_out = sys.stdout
        self.redirect_out = None
        if out and type(self.current_out).__name__ !='_MixterRedirectOut':
            self.redirect_out =self._MixterRedirectOut(self.current_out)
            sys.stdout = self.redirect_out
        self.reload(buildCode_code_str)

        if out and self.redirect_out:
            self._buffer = self.redirect_out._buff
            self.redirect_out.uninstall()

    def __repr__(self):
        return 'BuildCode({})'.format(self._code_str)

    def _init(self):
        for name,attr in self.module.__dict__.items():
            if name in NO_INCLUDE_ATTRIBUTES:
                continue
            setattr(self.module,name,attr)
            if isinstance(attr,types.FunctionType):
                self._functions[name] = attr
            elif isinstance(attr,types.ModuleType):
                self._modules[name] = attr
            else:
                self._variables[name] = attr

    def reload(self,buildCode_code_str):
        self._code_str = str(buildCode_code_str).strip()
        if not self._code_str:
            return
        try:
            code = compile(self._code_str, 'lasttester.contrib.BuildCode', 'exec')
            try:
                self._buffer = eval(code,self.module.__dict__)
            except Exception as e:
                self._error += e.__str__()
                exec(buildCode_code_str,self.module.__dict__)
        except Exception as e:
            self._error += e.__str__()
        self._init()

    def call(self,name,*args,**kwargs):
        func = self.get_attr(name)
        if not func:
            return
        return func(*args,**kwargs)

    def get_attrs(self,name=None):
        if not name:
            return self.module.__dict__
        if hasattr(self.module,name):
            return getattr(self.module,name)
        return None

    def get_functions(self,name=None):
        if not name:
            return self._functions
        func = self.get_attrs(name)
        if not func or not isinstance(func,types.FunctionType):
            return
        return func

    def get_variables(self,name=None):
        if not name:
            return self._variables
        variable = self.get_attrs(name)
        if not variable or isinstance(variable,types.FunctionType) or isinstance(variable,types.ModuleType):
            return
        return variable

    class _MixterRedirectOut(object):
        def __init__(self,orgin_out):
            """ init """
            self._buff = ""
            self.orgin_out = orgin_out

        def write(self, out_stream):
            """ :param out_stream: :return: """
            class_name = sys._getframe(1).f_code.co_filename
            if class_name =='lasttester.contrib.BuildCode':
                self._buff += out_stream
            else:
                self.orgin_out.write(out_stream)

        def flush(self):
            pass

        def isatty(self):
            return False

        def uninstall(self):
            if self.orgin_out:
                sys.stdout = self.orgin_out

class FakeBuildCode(object):
    def __init__(self,buildCode_code_str,out = False):
        super().__init__()
        self.reload(buildCode_code_str)
        self._error = ''
        self._buffer = 'this class has been mocked,if you want to try,please deploy the real code by yourself'


    def reload(self,buildCode_code_str):
        self._code_str = str(buildCode_code_str).strip()

    def call(self,name,*args,**kwargs):

        return self._buffer

    def get_attr(self,name):

        return self._buffer

    def get_function(self,name):
        return self._buffer

    def get_variable(self,name):
        return self._buffer