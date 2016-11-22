
class OutputWriterController():
    def __init__(self, output_writer, pipe):
        try:
            self.__output_writer = output_writer
            output_writer.handle(self.generator(pipe.recv))
        except EOFError:
            print("EOFError: quitting Output Writer")

    def generator(self, receive):
        while True:
            message = receive()

            if message.get('type') == 'data':
                yield message.get('data')
            elif message.get('type') == 'end':
                #self.__output_writer.exit()
                exit(0)
