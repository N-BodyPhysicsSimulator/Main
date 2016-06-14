from abc import ABC, abstractmethod
from nbp.io.input_providers.input_provider import InputProvider

class FileInputProvider(InputProvider, ABC):
    """ Abstract class FileInputProvider """

    def __init__(self, filepath):
        """ User will give filepath """
        self.__filepath = filepath

    def get_filepath(self):
        """ Getter of filepath """
        return self.__filepath

    @abstractmethod
    def get_bodies(self):
        """ Method to receive bodies. Returns a generator. """
        raise NotImplementedError()
