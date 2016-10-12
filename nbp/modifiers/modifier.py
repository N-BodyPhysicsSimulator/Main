from abc import ABCMeta, abstractmethod
from typing import Iterator

from nbp.bodies import BodyState


class Modifier(metaclass=ABCMeta):
    def __init__(self, args):
        self.args = args

    @abstractmethod
    def modify(self, state):
        pass

    @staticmethod
    @abstractmethod
    def get_cli_arguments() -> list:
        pass
