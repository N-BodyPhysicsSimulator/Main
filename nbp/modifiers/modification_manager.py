from nbp.bodies import BodyState

class ModificationManager(object):
    def __init__(self, generator, modifier):
        self.__generator = generator
        self.__modifier = modifier

    def get_generator(self):
        try:
            while True:
                state = next(self.__generator)
                yield state
        except StopIteration:
            pass
        finally:
            while True:
                state = self.__modifier.modificate(state)
                yield state
