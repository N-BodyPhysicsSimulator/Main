from abc import abstractmethod, ABCMeta


class OutputWriter(metaclass=ABCMeta):
    def __init__(self, args):
        self.args = args
        
    def exit(self):
        pass

    @abstractmethod
    def handle(self, generator, args):
        pass

    @staticmethod
    @abstractmethod
    def get_cli_arguments() -> list:
        pass
