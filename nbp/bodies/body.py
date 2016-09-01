import numpy

from nbp.helpers.numpy import tuple_to_numpy, numpy_to_dict, dict_to_numpy


class Body:
    pass  # Ughh, type hinting


class Body(object):
    def __init__(self, name: str, mass: float, radius: float, position: numpy.ndarray, velocity: numpy.ndarray):
        self.name, self.mass, self.radius = name, mass, radius
        self.position, self.velocity = position, velocity

    @classmethod
    def from_tuple_parameters(cls, name: str, mass: float, radius: float, position: tuple, velocity: tuple) -> Body:
        """Build Body from position and velocity as tuple
        
        >>> planet1 = Body.from_tuple_parameters("Planet1", 100.0, 20.0, (1.0, 2.0, 3.0), (4.0, 5.0, 6.0))
        >>> planet1.position
        array([[ 1.],
               [ 2.],
               [ 3.]])
        >>> planet1.velocity
        array([[ 4.],
               [ 5.],
               [ 6.]])
        >>> planet1.name
        'Planet1'
        >>> planet1.mass
        100.0
        >>> planet1.radius
        20.0
        >>> planet2 = Body("Planet2", 100.0, 20.0, numpy.array([[1.0], [2.0], [3.0]]),
        ... numpy.array([[4.0], [5.0], [6.0]]))
        >>> planet1.name == planet2.name
        False
        >>> planet1.mass == planet2.mass
        True
        >>> planet1.radius == planet2.radius
        True
        >>> planet1.position == planet2.position
        array([[ True],
               [ True],
               [ True]], dtype=bool)
        >>> planet1.velocity == planet2.velocity
        array([[ True],
               [ True],
               [ True]], dtype=bool)
        """
        return Body(
            name,
            mass,
            radius,
            tuple_to_numpy(position),
            tuple_to_numpy(velocity)
        )

    def to_dict(self) -> dict:
        return {
            'name': self.name,
            'mass': self.mass,
            'radius': self.radius,
            'position': numpy_to_dict(self.position),
            'velocity': numpy_to_dict(self.velocity)
        }

    @staticmethod
    def from_dict(dictionary):
        return Body(
            dictionary['name'],
            dictionary['mass'],
            dictionary['radius'],
            dict_to_numpy(dictionary['position']),
            dict_to_numpy(dictionary['velocity'])
        )
