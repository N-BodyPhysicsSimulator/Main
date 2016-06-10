from abc import ABC, abstractmethod

class InputProvider(ABC):
    @abstractmethod
    def get_bodies(self):
        """ Method to receive bodies. Returns a generator. """
        raise NotImplementedError()
