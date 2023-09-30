class Logger(object):
    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls):
        if cls._instance is None:
            print('Creating new instance')
            cls._instance = cls.__new__(cls)
        return cls._instance
    
log = Logger.instance()
print("first log " + str(log))

log2 = Logger.instance()
print("second log" + str(log2))

print(log is log2)