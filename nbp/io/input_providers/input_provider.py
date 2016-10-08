from abc import abstractmethod, ABCMeta
from types import GeneratorType
from typing import Iterator

from nbp.bodies import BodyState


class InputProvider(metaclass=ABCMeta):

    def __init__(self, args):
        self.args = args
    
    @abstractmethod
    def get_generator(self) -> Iterator[BodyState]:
        """ Method to receive bodies. Returns a generator. """
        pass

    @staticmethod
    @abstractmethod
    def get_cli_arguments() -> list:
        pass
