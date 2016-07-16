from abc import ABC, abstractmethod
from nbp.io.input_providers.input_provider import InputProvider

from nbp.bodies import BodyState

class FileInputProvider(InputProvider, ABC):
    """ Abstract class FileInputProvider
    >>> class ExampleInputProvider(FileInputProvider): pass
    >>> a = ExampleInputProvider("/home/berniesanders/file")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: Can't instantiate abstract class ExampleInputProvider with abstract methods get_body_states
    >>> class ExampleInputProvider(FileInputProvider):
    ...     def get_body_states(): yield []
    >>> a = ExampleInputProvider("/home/berniesanders/file")
    >>> a.get_filepath()
    '/home/berniesanders/file'
    """

    def __init__(self, filepath):
        """ User will give filepath """
        self.__filepath = filepath

    def get_filepath(self):
        """ Getter of filepath """
        return self.__filepath

    @abstractmethod
    def get_body_states(self):
        """ Method to receive bodies. Returns a generator. """
        raise NotImplementedError()
