from nbp.bodies import Body

import json


class BodyState(object):
    pass  # Typehinting


class BodyState(object):
    def __init__(self, bodies: [Body], ticks: int, time: float, delta_time: float):
        self.bodies, self.ticks = bodies, int(ticks)
        self.time, self.delta_time = float(time), float(delta_time)
        self.time_settings = {'time': [],'radius': []}#All the radi must be ALWAYS be positive and all the time must be either all negative or all positive.

    def to_dict(self) -> dict:
        """
        >>> state = BodyState([], 10, 100, 2).to_dict()
        >>> state.get('ticks')
        10
        >>> state.get('time')
        100.0
        >>> state.get('delta_time')
        2.0
        >>> state.get('bodies')
        []

        :return: dict
        """
        return {
            'ticks': self.ticks,
            'time': self.time,
            'delta_time': self.delta_time,
            'bodies': [body.to_dict() for body in self.bodies]
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @staticmethod
    def from_dict(dictionary: dict) -> BodyState:
        """
        >>> state = BodyState.from_dict({
        ...   'ticks': 10,
        ...   'time': 100,
        ...   'delta_time': 2.0,
        ...   'bodies': []
        ... })
        >>> state.ticks
        10
        >>> state.time
        100.0
        >>> state.delta_time
        2.0
        >>> state.bodies
        []

        :return: dict
        """
        return BodyState(
            [Body.from_dict(body) for body in dictionary['bodies']],
            dictionary['ticks'],
            dictionary['time'],
            dictionary['delta_time']
        )
