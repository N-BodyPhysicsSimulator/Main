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
        array([[1.],
               [2.],
               [3.]])
        >>> planet1.velocity
        array([[4.],
               [5.],
               [6.]])
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
               [ True]])
        >>> planet1.velocity == planet2.velocity
        array([[ True],
               [ True],
               [ True]])
        """
        return Body(
            name,
            mass,
            radius,
            tuple_to_numpy(position),
            tuple_to_numpy(velocity)
        )

    def to_dict(self) -> dict:
        """
        >>> dictionary = Body.from_tuple_parameters(
        ...   'Strawberry',
        ...   123.456,
        ...   789.123,
        ...   (1.1, 2.2, 3.3),
        ...   (9.9, 8.8, 7.7)
        ... ).to_dict()
        >>> dictionary.get('name')
        'Strawberry'
        >>> dictionary.get('mass')
        123.456
        >>> dictionary.get('radius')
        789.123
        >>> float(dictionary.get('position').get('x'))
        1.1
        >>> float(dictionary.get('velocity').get('z'))
        7.7

        :return: dict
        """
        return {
            'name': self.name,
            'mass': self.mass,
            'radius': self.radius,
            'position': numpy_to_dict(self.position),
            'velocity': numpy_to_dict(self.velocity)
        }

    @staticmethod
    def from_dict(dictionary):
        """
        >>> from nbp.helpers.numpy import numpy_to_list

        >>> dictionary = {
        ...   'name': 'Apple',
        ...   'mass': 12.34,
        ...   'radius': 56.78,
        ...   'position': { 'x': 1.9, 'y': 2.8, 'z': 3.7 },
        ...   'velocity': { 'x': 4.6, 'y': 5.5, 'z': 6.4 }
        ... }
        >>> body = Body.from_dict(dictionary)
        >>> body.name
        'Apple'
        >>> body.mass
        12.34
        >>> body.radius
        56.78
        >>> [float(v) for v in numpy_to_list(body.position)]
        [1.9, 2.8, 3.7]
        >>> [float(v) for v in numpy_to_list(body.velocity)]
        [4.6, 5.5, 6.4]

        :param dictionary: dict
        :return: Body
        """
        return Body(
            dictionary['name'],
            dictionary['mass'],
            dictionary['radius'],
            dict_to_numpy(dictionary['position']),
            dict_to_numpy(dictionary['velocity'])
        )

    def __eq__(self, other):
        """
        >>> import numpy as np

        >>> one = Body.from_tuple_parameters("Earth", 100.0, 20.0, (1.0, 2.0, 3.0), (4.0, 5.0, 6.0))
        >>> two = Body('Earth', 100.0, 20.0, np.array([[1.], [2.], [3.]]), np.array([[4.], [5.], [6.]]))
        >>> two == one
        True
        """
        return isinstance(other, self.__class__) and self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """
        >>> import numpy as np

        >>> one = Body.from_tuple_parameters("Moon", 100.0, 20.0, (1.0, 2.0, 3.0), (4.0, 5.0, 6.0))
        >>> two = Body('Earth', 100.0, 20.0, np.array([[1.], [2.], [3.]]), np.array([[4.], [5.], [6.]]))
        >>> two != one
        True
        """
        return isinstance(other, self.__class__) and not self.__eq__(other)
