from abc import ABCMeta, abstractmethod, ABC


class Modifier(ABC):
    __metaclass__ = ABCMeta

    def __init__(self, generator):
        self.__generator = generator

    def get_generator(self):
        """
        Should rewrite!
        :return:
        """
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
