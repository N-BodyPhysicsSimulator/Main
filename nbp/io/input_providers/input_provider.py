from abc import ABC, abstractmethod

class InputProvider(ABC):
    """InputProvider ABC. All InputProviders will extend this class
    >>> class ExampleInputProvider(InputProvider): pass
    >>> a = ExampleInputProvider()
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: Can't instantiate abstract class ExampleInputProvider with abstract methods get_bodies
    >>> class ExampleInputProvider(InputProvider):
    ...     def get_bodies(): return []
    >>> a = ExampleInputProvider()
    """
    @abstractmethod
    def get_bodies(self):
        """ Method to receive bodies. Returns a generator. """
        raise NotImplementedError()
