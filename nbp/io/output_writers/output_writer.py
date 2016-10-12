import pytest

from abc import abstractmethod, ABCMeta


class OutputWriter(metaclass=ABCMeta):
    def __init__(self, args):
        self.args = args
        
    def exit(self):
        pass

    @abstractmethod
    @pytest.mark.skip(reason="Abstract method")
    def handle(self, generator, args):
        pass

    @staticmethod
    @abstractmethod
    @pytest.mark.skip(reason="Abstract method")
    def get_cli_arguments() -> list:
        pass
