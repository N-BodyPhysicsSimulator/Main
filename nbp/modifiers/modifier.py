from abc import ABCMeta, abstractmethod

from nbp.bodies import BodyState

class Modifier(object):
    __metaclass__ = ABCMeta

    def __init__(self, generator):
        self.__generator = generator

    def get_generator(self):
        try:
            while True:
                state = next(self.__generator)
                yield state
        except StopIteration:
            pass
        finally:
            while True:
                state = self.modificate(state)
                yield state

    @abstractmethod
    def modificate(self, state):
        raise Exception('Method modificate should be implemented.')
