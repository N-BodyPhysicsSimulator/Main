from abc import ABC, abstractmethod, ABCMeta
from types import GeneratorType
from typing import Iterator

from nbp.bodies import BodyState


class InputProvider(ABC):
    """InputProvider ABC. All InputProviders will extend this class
    >>> class ExampleInputProvider(InputProvider): pass
    >>> a = ExampleInputProvider({})
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: Can't instantiate abstract class ExampleInputProvider with abstract methods get_generator
    >>> class ExampleInputProvider(InputProvider):
    ...     def get_generator(): yield []
    >>> a = ExampleInputProvider({})
    """

    __metaclass__ = ABCMeta

    def __init__(self, args):
        self.args = args
    
    @abstractmethod
    def get_generator(self) -> Iterator[BodyState]:
        """ Method to receive bodies. Returns a generator. """
        raise NotImplementedError()

    @staticmethod
    def get_cli_arguments() -> list:
        raise NotImplementedError()
