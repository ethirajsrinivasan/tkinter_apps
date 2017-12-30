import abc

class DataManagement(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def getName(self):
        return

    @abc.abstractmethod
    def valid(self):
        return

    @abc.abstractmethod
    def execute(self):
        return
