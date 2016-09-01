from abc import abstractmethod, ABCMeta, ABC


class OutputWriter(ABC):
    __metaclass__ = ABCMeta

    def __init__(self, pipe, args):
        try:
            self.tick(pipe.recv, args)
        except EOFError:
            print("EOFError: quitting Output Writer")

    @abstractmethod
    def tick(self, body_state, args):
        raise NotImplementedError()

    @staticmethod
    def get_cli_arguments() -> list:
        raise NotImplementedError()
