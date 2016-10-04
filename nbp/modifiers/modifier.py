from abc import ABCMeta, abstractmethod, ABC
from typing import Iterator

from nbp.bodies import BodyState


class Modifier(ABC):
    __metaclass__ = ABCMeta

    def __init__(self, args):
        self.args = args

    @abstractmethod
    def modificate(self, state):
        raise Exception('Method modificate should be implemented.')
