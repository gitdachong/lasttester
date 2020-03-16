#coding:utf-8
import contextlib
import sys
import traceback
class Capturer(object):
    def __init__(self):
        self.success = True
        self.errors = []

    @contextlib.contextmanager
    def catch(self):
        try:
            yield
        except KeyboardInterrupt:
            raise
        except:
            exc_info = traceback.format_exc()
            self.success = False
            self.errors.append(exc_info)

    def get_parsed_errors(self):
        """Converts a sys.exc_info()-style tuple of values into a string."""
        return ''.join(self.errors)
