#coding:utf-8
import sys,traceback


def try_except(f):
    def handle_problems(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception:
            exc_type, exc_instance, exc_traceback = sys.exc_info()
            formatted_traceback = ''.join(traceback.format_tb(exc_traceback))
            message = '\n{0}\n{1}:\n{2}'.format(
                formatted_traceback,
                exc_type.__name__,
                exc_instance
            )
#             raise exc_type(message)
            print(exc_type(message))
            # 其他你喜欢的操作
        finally:
            pass
    return handle_problems
