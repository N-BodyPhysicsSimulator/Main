from abc import ABC, abstractmethod

class InputProvider(ABC):
    """InputProvider ABC. All InputProviders will extend this class
    >>> class ExampleInputProvider(InputProvider): pass
    >>> a = ExampleInputProvider()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: Can't instantiate abstract class ExampleInputProvider with abstract methods get_body_states
    >>> class ExampleInputProvider(InputProvider):
    ...     def get_body_states(): yield []
    >>> a = ExampleInputProvider()
    """
    @abstractmethod
    def get_body_states(self):
        """ Method to receive bodies. Returns a generator. """
        raise NotImplementedError()
