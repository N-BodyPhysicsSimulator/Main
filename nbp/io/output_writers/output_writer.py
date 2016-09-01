from abc import abstractmethod, ABCMeta, ABC


class OutputWriter(ABC):
    __metaclass__ = ABCMeta

    def __init__(self, pipe, args):
        try:
            self.handle(self.generator(pipe.recv), args)
        except EOFError:
            print("EOFError: quitting Output Writer")

    def generator(self, receive):
        while True:
            message = receive()

            if message.get('type') == 'data':
                yield message.get('data')
            elif message.get('type') == 'end':
                self.exit()
                exit(0)

    def exit(self): pass

    @abstractmethod
    def handle(self, generator, args):
        raise NotImplementedError()

    @staticmethod
    def get_cli_arguments() -> list:
        raise NotImplementedError()
