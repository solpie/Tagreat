__author__ = 'SolPie'


def singleton(cls):
    instances = {}

    def getInstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]

    return getInstance


class BaseView(object):
    def __init__(self):
        self.dic_event_func = dict()

    def map(self, event, func):
        self.dic_event_func[event] = func

    def execute(self, event, *args,**kwargs):
        return self.dic_event_func[event](*args)
