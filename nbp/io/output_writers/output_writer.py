from abc import abstractmethod, ABCMeta

class OutputWriter(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def tick(self, body_state, args):
        raise Exception('Method tick should be implemented.')

    @staticmethod
    def get_validation_schema():
        raise Exception('Method get_validation_schema should be implemented.')
