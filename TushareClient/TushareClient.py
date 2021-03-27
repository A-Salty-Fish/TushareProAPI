import threading

import tushare as ts


def synchronized(func):
    func.__lock__ = threading.Lock()

    def lock_func(*args, **kwargs):
        with func.__lock__:
            return func(*args, **kwargs)

    return lock_func


class Client(object):
    instance = None

    @synchronized
    def __get__(cls, *args, **kwargs):
        if cls.instance is None:
            with open('../TushareClient/token.txt') as tokenFile:
                cls.instance = ts.pro_api(tokenFile.readline())
        return cls.instance
