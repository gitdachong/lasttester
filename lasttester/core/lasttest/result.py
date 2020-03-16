#coding:utf-8
import time
from functools import wraps
from ...utils import util
__unittest = True

def failfast(method):
    @wraps(method)
    def inner(self, *args, **kw):
        if getattr(self, 'failfast', False):
            self.stop()
        return method(self, *args, **kw)
    return inner

STDOUT_LINE = '\nStdout:\n%s'
STDERR_LINE = '\nStderr:\n%s'


class TestResult(object):

    def __init__(self):
        self.shouldStop = False
        self._result = {"result":True,"total":0,"success":0,"failure":0,"skip":0,"error":0,"start_time":0,"end_time":0,"duration":0,"executor":"","tests":[]}

    @property
    def result(self):
        return self._result

    def add_test_result(self,test,flag,err):
        _testresult = test.result
        _testresult['run_success'] = flag
        _testresult['run_error_text'] = err
        self._result['total'] += 1

        if _testresult['result']:
            self._result['success'] +=1
        else:
            self._result['result'] = False
            if flag:
                self._result['failure'] += 1
            else:
                self._result['error'] += 1

        self._result['tests'].append(_testresult)

    def startTest(self, test):
        "Called when the given test is about to be run"
        pass


    def startTestRun(self):
        self._result['start_time'] = util.get_current_timestamp_13()

    def stopTest(self, test):
        """Called when the given test has been run"""
        pass



    def stopTestRun(self):

        self._result['end_time'] = util.get_current_timestamp_13()


    def wasSuccessful(self):
        """Tells whether or not this result was a success."""
        # The hasattr check is for test_result's OldResult test.  That
        # way this method works on objects that lack the attribute.
        # (where would such result intances come from? old stored pickles?)
        return self._result['result']

    def stop(self):
        """Indicates that the tests should be aborted."""
        self.shouldStop = True


    def __repr__(self):
        return ("<%s run=%i errors=%i failures=%i>" %
               ("%s.%s" % (self.__class__.__module__, self.__class__.__qualname__), self._result['total'], self._result['error'],
                self._result['failure']))
