from typing import Iterator

from nbp.bodies import BodyState
from nbp.decorators import entity
from nbp.helpers.physics import calculate_position
from nbp.helpers.physics import calculate_velocity
from nbp.helpers.physics import get_delta_time
from nbp.modifiers import Modifier


@entity("calculation")
class CalculationModifier(Modifier):
    @staticmethod
    def get_cli_arguments() -> list:
        return []

    def modify(self, state: BodyState) -> BodyState:
        """Calculates one tick of the simulator"""
        state.ticks += 1
        state.time += state.delta_time

        state = self.__update_position(state)
        state = self.__update_velocity(state)

        return state

    def __update_position(self, state):
        for i, body in enumerate(state.bodies):
            state.bodies[i].position = calculate_position(body, state.delta_time)

        return state

    def __update_velocity(self, state):
        for i, body in enumerate(state.bodies):
            state.bodies[i].velocity = calculate_velocity(body, state.delta_time, state.bodies)

        return state
