import numpy

class Body():
    pass # Will make Type Hinting work.

class Body(object):
    def __init__(self, name: str, mass: float, radius: float, position: numpy.ndarray, velocity: numpy.ndarray):
        self.name, self.mass, self.radius = name, mass, radius
        self.position, self.velocity = position, velocity

    @classmethod
    def from_tuple_parameters(self, name: str, mass: float, radius: float, position: tuple, velocity: tuple):
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
        numpy_position = self.__tuple_to_numpy(self, position)
        numpy_velocity = self.__tuple_to_numpy(self, velocity)

        return Body(name, mass, radius, numpy_position, numpy_velocity)
        
    def __tuple_to_numpy(self, t: tuple) -> numpy.ndarray:
        """ How to test this private function!? """
        return numpy.array([[t[0]],
                            [t[1]],
                            [t[2]]]).astype('float64')
