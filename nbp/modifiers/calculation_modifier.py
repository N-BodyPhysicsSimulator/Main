from typing import Iterator

from nbp.bodies import BodyState
from nbp.decorators import entity
from nbp.helpers.physics import calculate_position
from nbp.helpers.physics import calculate_velocity
from nbp.modifiers import Modifier


@entity("calculation")
class CalculationModifier(Modifier):
    def modificate(self, state: BodyState) -> BodyState:
        """Calculates one tick of the simulator"""
        state.ticks += 1
        state.time += state.delta_time

        state = self.__update_position(state)
        state = self.__update_velocity(state)
        # state = self.__merge(state)

        return state

    def get_generator(self) -> Iterator[BodyState]:
        """
        Only modificate if last Body from generator

        :return: Iterator[BodyState]
        """
        try:
            while True:
                state = next(self.generator)
                yield state
        except StopIteration:
            pass
        finally:
            while True:
                state = self.modificate(state)
                yield state

    def __update_position(self, state):
        for i, body in enumerate(state.bodies):
            state.bodies[i].position = calculate_position(body, state.delta_time)

        return state

    def __update_velocity(self, state):
        for i, body in enumerate(state.bodies):
            state.bodies[i].velocity = calculate_velocity(body, state.delta_time, state.bodies)

        return state
