import numpy
import pickle

from base64 import b64encode, b64decode

class Body(): pass # Will make Type Hinting work.

class Body(object):
    def __init__(self, name: str, mass: float, radius: float, position: tuple, velocity: tuple):
        self.name, self.mass, self.radius = name, mass, radius

        # Vector
        self.position = numpy.array([[position[0]],
                                     [position[1]],
                                     [position[2]]])

        # Vector
        self.velocity = numpy.array([[velocity[0]],
                                     [velocity[1]],
                                     [velocity[2]]])

    def distance_to(self, other: Body) -> numpy.ndarray:
        """Takes two instances of a bodies and calculates the distance.

        Returns a Vector. Use numpy.linalg.norm(<Vector>) to get real distance in a float.

        >>> earth = Body("Earth", 5.972*(10**24), 100, (1.506*(10**11), 0, 100), (0, 29290, 0))
        >>> moon = Body("Moon", 0.0735*(10**24), 100, (1.496*(10**11), 384.4*(10**6), -500), (1050, 29290, 0))
        >>> moon.distance_to(earth)
        array([[  -1.00000000e+09],
               [ -3.84400000e+08],
               [  6.00000000e+02]])
        """
        if self == other:
            return numpy.array([[0],
                                [0],
                                [0]])

        return other.position - self.position
        
    def acceleration_to_one(self, other: Body) -> numpy.ndarray:
        """Return acceleration in x, y, z directions.
        >>> earth = Body("Earth", 5.972*(10**24), 100, (0, 0, 0), (0, 29290, 0))
        >>> 1kg = Body("1kg", 1, 100, (0, 6371000, 0), (1050, 29290, 0))
        >>> 1kg.acceleration_to_one(earth)
        array([[ 0.        ],
               [ -9.81964974],
               [ 0.        ]])
        """
        if self == other:
            return numpy.array([[0],
                                [0],
                                [0]])

        distance_vector = other.position - self.position
        distance = numpy.linalg.norm(distance_vector)
        force = (6.67408 * (10**-11)) * ((self.mass * other.mass) / (distance ** 2))
        forceratio = force / distance

        return ( distance_vector * forceratio ) / self.mass
        
    def acceleration_to_all(self, bodies: [Body]) -> numpy.ndarray:
        total_acceleration = 0

        for body in bodies:
            total_acceleration += self.acceleration_to_one(body)

        return total_acceleration
        
    def calculate_position(self, change_in_time: float) -> None:
        """ Calculates a new position for a new tick
        >>> earth = Body("Earth", 5.972*(10**24), 100, (1.506*(10**11), 0, 100), (0, (1*(10**10)), -10))
        >>> earth.calulate_position(10)
        earth.position = array([[ 1.506*(10**11) ],
                                [ 1.0*(10**11) ],
                                [ 0. ]])
        """
        self.position += change_in_time * self.velocity
    
    def calculate_velocity(self, bodies, change_in_time: float) -> None:
        """ Calculates new velocity for a new tick.
        >>> earth = Body("Earth", 5.972*(10**24), 100, (0, 0, 0), (0, 0, 0))
        >>> 1kg = Body("1kg", 1, 100, (0, 6371000, 0), (0, 0, 0))
        >>> 1kg.calculate_velocity(2)
        1kg.velocity = array([[ 0.0 ],
                            [ -19.63929948],
                            [ 0.0 ]])
        """
        self.velocity += change_in_time * self.acceleration_to_all(bodies)
