from abc import ABC
from nbp.io.input_providers.input_provider import InputProvider

class FileInputProvider(InputProvider, ABC):
    """ Abstract class FileInputProvider """

    def __init__(self, filepath):
        """ User will give filepath """
        self.__filepath = filepath

    def get_filepath(self):
        """ Getter of filepath """
        return self.__filepath
