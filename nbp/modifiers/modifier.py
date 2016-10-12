import pytest

from abc import ABCMeta, abstractmethod
from typing import Iterator

from nbp.bodies import BodyState


class Modifier(metaclass=ABCMeta):
    def __init__(self, args):
        self.args = args

    @abstractmethod
    @pytest.mark.skip(reason="Abstract method")
    def modify(self, state):
        pass

    @staticmethod
    @abstractmethod
    @pytest.mark.skip(reason="Abstract method")
    def get_cli_arguments() -> list:
        pass
