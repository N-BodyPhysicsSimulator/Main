import numpy

class Body():
    pass # Will make Type Hinting work.

class Body(object):
    def __init__(self, name: str, mass: float, radius: float, position: tuple, velocity: tuple):
        self.name, self.mass, self.radius = name, mass, radius

        # Vector
        self.position = numpy.array([[position[0]],
                                     [position[1]],
                                     [position[2]]]).astype('float64')

        # Vector
        self.velocity = numpy.array([[velocity[0]],
                                     [velocity[1]],
                                     [velocity[2]]]).astype('float64')

    def distance_to(self, other: Body) -> numpy.ndarray:
        """Takes two instances of a bodies and calculates the distance.

        Returns a Vector. Use numpy.linalg.norm(<Vector>) to get real distance in a float.

        >>> earth = Body("Earth", 5.972*(10**24), 100, (1.506*(10**11), 0, 100), (0, 29290, 0))
        >>> moon = Body("Moon", 0.0735*(10**24), 100, (1.496*(10**11), 384.4*(10**6), -500), (1050, 29290, 0))
        >>> moon.distance_to(earth)
        array([[  1.00000000e+09],
               [ -3.84400000e+08],
               [  6.00000000e+02]])
        >>> moon = Body("Moon", 0.0735*(10**24), 100, (1.496*(10**11), 384.4*(10**6), -500), (1050, 29290, 0))
        >>> moon.distance_to(moon)
        array([[ 0.],
               [ 0.],
               [ 0.]])
        """

        return other.position - self.position

    def absolute_distance_to_one(self, other: Body) -> numpy.ndarray:
        """Takes two instances of a bodies and calculates the absolute distance.

        >>> earth = Body("Earth", 5.972*(10**24), 100.0, (1.496*(10**11), 0, 0), (0, 29290, 0))
        >>> moon = Body("Moon", 0.0735*(10**24), 100.0, (1.496*(10**11), 384.4*(10**6), 0), (1050, 29290, 0))
        >>> moon.absolute_distance_to_one(earth)
        384400000.0
        """
        return numpy.linalg.norm(self.distance_to(other))

    def acceleration_to_one(self, other: Body) -> numpy.ndarray:
        """Return acceleration in x, y, z directions.
        >>> earth = Body("Earth", (5.972*(10**24)), 100.0, (0, 0, 0), (0, 0, 0))
        >>> kg = Body("kg", 1.0, 100.0, (0, 6371000, 0), (0, 0, 0))
        >>> kg.acceleration_to_one(earth)
        array([[ 0.        ],
               [-9.81964974],
               [ 0.        ]])
        """
        if self == other:
            return numpy.array([[0],
                                [0],
                                [0]])

        distance_vector = self.distance_to(other)
        distance = self.absolute_distance_to_one(other)

        force = (6.67408 * (10 ** -11)) * ((self.mass * other.mass) / (distance ** 2))
        forceratio = force / distance

        return (distance_vector * forceratio) / self.mass

    def acceleration_to_all(self, bodies: [Body]) -> numpy.ndarray:
        """ Return the acceleration in vectors to alll other bodies
        >>> kg = Body("kg", 1.0, 100.0, (0, 0, 0), (0, 0, 0))
        >>> earth1 = Body("Earth1", (5.972*(10**24)), 100.0, (0, 6371000, 6280), (0, 0, 0))
        >>> earth2 = Body("Earth4", (5.972*(10**24)), 100.0, (-6371000, 0, 0), (0, 0, 0))
        >>> moon = Body("Moon", 0.0735*(10**24), 100.0, (0, 384.4*(10**6), -1000), (0, 0, 0))
        >>> bodies = [kg, earth1, earth2, moon]
        >>> moon.acceleration_to_all(bodies)
        array([[ -4.46878801e-05],
               [ -5.48536334e-03],
               [  6.07257588e-08]])

        """
        total_acceleration = numpy.array([[0],
                                          [0],
                                          [0]]).astype("float64")

        for body in bodies:
            total_acceleration = total_acceleration + self.acceleration_to_one(body)

        return total_acceleration

    def calculate_position(self, delta_time: float) -> None:
        """ Calculates a new position for a new tick
        >>> test_body = Body("Test_body", 1.0, 1.0, (60, -20, 15), (4, 10.2, -6))
        >>> test_body.calculate_position(3.0)
        >>> test_body.position
        array([[ 72. ],
               [ 10.6],
               [ -3. ]])
        """
        self.position = self.position + (delta_time * self.velocity)

    def calculate_velocity(self, bodies, delta_time: float) -> None:
        """ Calculates new velocity for a new tick.
        >>> kg = Body("kg", 1.0, 100.0, (0, 0, 0), (0, 0, 0))
        >>> earth1 = Body("Earth1", (5.972*(10**24)), 100.0, (0, 6371000, 0), (0, 0, 0))
        >>> earth2 = Body("Earth2", (5.972*(10**24)), 100.0, (0, -6371000, 0), (0, 0, 0))
        >>> earth3 = Body("Earth3", (5.972*(10**24)), 100.0, (6371000, 0, 0), (0, 0, 0))
        >>> earth4 = Body("Earth4", (5.972*(10**24)), 100.0, (-6371000, 0, 0), (0, 0, 0))
        >>> earth5 = Body("Earth5", (5.972*(10**24)), 100.0, (6371000, 9000, -532), (0, 0, 0))
        >>> earth6 = Body("Earth6", (5.972*(10**24)), 100.0, (-6371000, -9000, 532), (0, 0, 0))
        >>> bodies = [kg, earth1, earth2, earth3, earth4, earth5, earth6]
        >>> kg.calculate_velocity(bodies, 314.0)
        >>> kg.velocity
        array([[ 0.],
               [ 0.],
               [ 0.]])

        >>> kg = Body("kg", 1.0, 100.0, (0, 0, 0), (0, 0, 0))
        >>> earth1 = Body("Earth1", (5.972*(10**24)), 100.0, (0, 6371000, 6280), (0, 0, 0))
        >>> moon = Body("Moon", 0.0735*(10**24), 100.0, (0, 384.4*(10**6), -1000), (0, 0, 0))
        >>> bodies = [kg, earth1, moon]
        >>> kg.calculate_velocity(bodies, 16.0)
        >>> kg.velocity
        array([[  0.00000000e+00],
               [  1.57114698e+02],
               [  1.54870030e-01]])

        >>> kg = Body("kg", 1.0, 100.0, (0, 0, 0), (0, 0, 0))
        >>> earth1 = Body("Earth1", (5.972*(10**24)), 100.0, (0, 6371000, 6280), (0, 0, 0))
        >>> moon = Body("Moon", 0.0735*(10**24), 100.0, (0, 384.4*(10**6), -1000), (0, 0, 0))
        >>> bodies = [kg, earth1, moon]
        >>> kg.calculate_velocity(bodies, 16.0)
        >>> kg.calculate_position(16.0) # This is basicly a test of a tick
        >>> kg.position
        array([[  0.00000000e+00],
               [  2.51383517e+03],
               [  2.47792047e+00]])
        """
        self.velocity = self.velocity + (delta_time * self.acceleration_to_all(bodies))

    def merge(self, other):
        """ merges one body with a second body. Important note: This function doesn't delete the other body!
        It assumed that the density will stay the same after collision
        >>> earth = Body("Earth", 5.972*(10**24), 6371000, (1.506*(10**11), 500, 100), (-100, 29290, -2))
        >>> moon = Body("Moon", 0.0735*(10**24), 1738000, (1.496*(10**11), 384.4*(10**6), -500), (1050, -29290, 100))
        >>> earth.merge(moon)
        >>> earth.position
        array([[  1.50587842e+11],
               [  4.67395352e+06],
               [  9.27053180e+01]])
        >>> earth.velocity
        array([[ -8.60185262e+01],
               [  2.85777959e+04],
               [ -7.59904061e-01]])
        >>> earth.radius
        6413824.949215559
        >>> earth.mass # Notice the strage 1 at the end.
        6.045500000000001e+24
        >>> huge = Body("huge", 5.972*(10**24), 173843647354234567632353, (1.506*(10**11), 500, 100), (-100, 29290, -2))
        >>> huge.merge(earth)
        >>> huge.radius
        1.7384364735423404e+23
        >>> large = Body("huge", 5.972*(10**24), 17380000000, (1.506*(10**11), 500, 100), (-100, 29290, -2)) # Notice that if the radius of large is 1738000000000 that the radius will get smaller with 2,7 milimeters
        >>> earth.merge(large)
        >>> earth.radius
        17380000000.291138
        """
        total_mass = self.mass + other.mass
        self.position = (self.position * self.mass + other.position * other.mass) / total_mass
        self.velocity = (self.velocity * self.mass + other.velocity * other.mass) / total_mass
        self.radius = ((self.radius ** 3) + (other.radius ** 3)) ** (1/3)
        self.mass = total_mass
