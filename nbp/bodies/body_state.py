from nbp.bodies import Body


class BodyState(object):
    pass  # Typehinting


class BodyState(object):
    def __init__(self, bodies: [Body], ticks: int, time: float, delta_time: float):
        self.bodies, self.ticks = bodies, int(ticks)
        self.time, self.delta_time = float(time), float(delta_time)
        
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

    def __eq__(self, other):
        """
        >>> import numpy as np
        >>> from nbp.bodies import Body

        >>> one = Body.from_tuple_parameters("Earth", 100.0, 20.0, (1.0, 2.0, 3.0), (4.0, 5.0, 6.0))
        >>> two = Body('Earth', 100.0, 20.0, np.array([[1.], [2.], [3.]]), np.array([[4.], [5.], [6.]]))
        
        >>> state1 = BodyState.from_dict({
        ...   'ticks': 10,
        ...   'time': 100,
        ...   'delta_time': 2.0,
        ...   'bodies': []
        ... })

        >>> state2 = BodyState.from_dict({
        ...   'ticks': 10,
        ...   'time': 100,
        ...   'delta_time': 2.0,
        ...   'bodies': []
        ... })
        
        >>> state1.bodies = [one, two]
        >>> state2.bodies = [one, two]

        >>> state1 == state2
        True
        """
        return isinstance(other, self.__class__) and self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """
        >>> import numpy as np
        >>> from nbp.bodies import Body

        >>> one = Body.from_tuple_parameters("Moon", 10.0, 2.0, (11.0, 2.20, 3.40), (14.0, 55.0, 67.0))
        >>> two = Body('Earth', 100.0, 20.0, np.array([[1.], [2.], [3.]]), np.array([[4.], [5.], [6.]]))
        
        >>> state1 = BodyState.from_dict({
        ...   'ticks': 10,
        ...   'time': 100,
        ...   'delta_time': 2.0,
        ...   'bodies': []
        ... })
        >>> state1.bodies = [one]

        >>> state2 = BodyState.from_dict({
        ...   'ticks': 1,
        ...   'time': 1020,
        ...   'delta_time': 23.0,
        ...   'bodies': []
        ... })
        >>> state1.bodies = [two]

        >>> state1 != state2
        True
        """
        return isinstance(other, self.__class__) and not self.__eq__(other)
