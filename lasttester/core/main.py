#coding:utf-8

from .context import Context
from . import lasttest

class LastTester:
    def __init__(self):
        self._context = Context()
        self._configurers = []
        kwargs = {
            "failfast": False,
        }
        self._runner = lasttest.TestRunner(**kwargs)
        self._result = {}

    @property
    def result(self):
        return self._result

    def run(self,test_driver_data):
        self.run_from_data(test_driver_data)
        return self._result


    def run_from_data(self,test_driver_data):
        self.__init_data(test_driver_data)
        test_cases =test_driver_data.get('testcases',[])
        test_suite = self.__load_tests(test_cases)
        run_result = self._runner.run(test_suite)
        print(run_result)
        self._result =run_result.result


    def __init_data(self,test_driver_data = {}):
        test_driver_data.setdefault('testcases',[])
        configs = test_driver_data.pop('configs',[])
        self._context.load_configs(configs)


    def __run_setUp(self,test_driver_data):
        pass


    def __run_tearDown(self):
        for _configurer in self._configurers:
            _configurer.close()


    def __load_tests(self, testcases):
        test_suite = lasttest.TestSuite()
        for case_index, testcase in enumerate(testcases):
            self._context.load_configs(testcase.pop('configs',[]))
            tests = testcase.get("teststeps", [])
            for index, test_dict in enumerate(tests):
                loaded_testcase = lasttest.TestCase(self._context, test_dict)
                test_suite.addTest(loaded_testcase)

        return test_suite

    def __register(self):
        pass

