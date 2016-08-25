from abc import ABCMeta, abstractmethod

from nbp.bodies import BodyState

class Modifier(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def modificate(self, state):
        raise Exception('Method modificate should be implemented.')
