from abc import ABCMeta, abstractmethod, ABC
from typing import Iterator

from nbp.bodies import BodyState


class Modifier(ABC):
    __metaclass__ = ABCMeta

    def __init__(self, generator):
        self.generator = generator

    def get_generator(self) -> Iterator[BodyState]:
        yield self.modificate(
            next(self.generator)
        )

    @abstractmethod
    def modificate(self, state):
        raise Exception('Method modificate should be implemented.')
