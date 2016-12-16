
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
    """
    the settings are in this format : ([time1, time2], [distance1, distance2])
    >>> from nbp.helpers.numpy import tuple_to_numpy
    >>> from nbp.bodies import Body
    >>> from nbp.bodies import BodyState
    >>> import numpy as np
    >>> settings = ([1, 2, 3, 4], [100, 200, 300, 400])
    >>> velocity = tuple_to_numpy((0, 0, 0))
    >>> one = Body('body1', 1, 100, np.array([[0.], [0.], [0.]]), velocity)
    >>> two = Body('body2', 1, 100, np.array([[0.], [99.], [0.]]), velocity)

    >>> dtm = DeltaTimeModifier({ 'change_dt_settings': settings })
    >>> bs = BodyState([one, two], 0, 0, 10)
    >>> bs.delta_time
    10.0
    >>> new = dtm.modify(bs)
    >>> new.delta_time
    1
    """
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

    def modify(self, state: BodyState) -> BodyState:
        """Calculates one tick of the simulator"""
        state.delta_time = get_delta_time(state.bodies, self.args.get('change_dt_settings'))

        return state
