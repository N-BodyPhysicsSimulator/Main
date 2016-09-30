
from typing import Iterator

from nbp.bodies import BodyState
from nbp.decorators import entity
from nbp.helpers.physics import calculate_position
from nbp.helpers.physics import calculate_velocity
from nbp.helpers.physics import get_delta_time
from nbp.modifiers import Modifier
from nbp.helpers.validation import change_delta_time_settings_to_tuples


@entity("delta_time")
class DeltaTimeModifier(Modifier):
    @staticmethod
    def get_cli_arguments() -> list:
        return [
            (
                '--change-delta-time-settings',
                {
                    'metavar': 'settings',
                    'type': change_delta_time_settings_to_tuples,
                    'help': 'Settings for Change Delta Time',
                    'dest': 'change_dt_settings',
                    'required': True
                }
            )
        ]

    def modificate(self, state: BodyState) -> BodyState:
        """Calculates one tick of the simulator"""
        state.delta_time = get_delta_time(state.bodies, self.args.get('change_dt_settings'))

        return state
