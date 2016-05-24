class Body(): pass # Will make Type Hinting work.

class Body(object):
    def __init__(self, name, mass, radius, positionX, positionY, positionZ, velocityX, velocityY, velocityZ):
        self.name = name
        self.mass = mass
        self.r = radius
        self.position = {"x": positionX, "y": positionY, "z": positionZ}
        self.velocity = {"x": velocityX, "y": velocityY, "z": velocityZ}
        
    def distance_in_directions_to(self, other: Body) -> dict:
        """Takes two instances of a bodies and calculates the distance.
        >>> earth = Body("Earth", 5.972*(10**24), 100, 1.496*(10**11), 0, 0, 0, 29290, 0)
        >>> moon = Body("Moon", 0.0735*(10**24), 100, 1.496*(10**11), 384.4*(10**6), 0, 1050, 29290, 0)
        >>> moon.distance_in_directions_to(earth) == {'x': 0.0,  'y': -384400000.0, 'z': 0}
        True
        """
        if self == other:
            return {"x": 0, "y": 0, "z": 0}

        distance = {}

        for direction in ['x', 'y', 'z']:
            distance[direction] = other.position[direction] - self.position[direction]

        return distance
        
    def absolute_distance_to(self, distances_in_directions: dict) -> float:
        """Takes ditance in directions and converts it to absolute distance via pythogoras
        >>> earth = Body("Earth", 5.972*(10**24), 100, 1.496*(10**11), 0, 0, 0, 29290, 0, 5)
        >>> moon = Body("Moon", 0.0735*(10**24), 100, 1.496*(10**11), 384.4*(10**6), 0, 1050, 29290, 0, 5)
        >>> dis = moon.distance_in_directions_to(earth)
        >>> moon.absolute_distance_to(dis)
        384400000.0
        >>> moon.absolute_distance_to(dis) == earth.absolute_distance_to(dis)
        True
        """
        return ((distances_in_directions['x'] ** 2) + (distances_in_directions['y'] ** 2) + (distances_in_directions['z'] ** 2)) ** (1/2)
        
    def acceleration_to_one(self, other: Body) -> dict:
        """Return acceleration in x, y, z directions.
        >>> earth = Body("Earth", 5.972*(10**24), 100, 0, 0, 0, 0, 29290, 0, 5)
        >>> moon = Body("Moon", 1, 100, 0, 6371000, 0, 1050, 29290, 0)
        >>> moon.acceleration_to_one(earth)
        {'z': 0.0, 'y': -9.819649737724951, 'x': 0.0}
        """
        if self == other:
            return {"x": 0, "y": 0, "z": 0}

        force_in_directions = {}
        acceleration = {}

        distance_in_directions = self.distance_in_directions_to(other)
        absolute_distance = self.absolute_distance_to(distance_in_directions)
        force = (6.67408 * (10**-11)) * ((self.mass * other.mass) / (absolute_distance ** 2))
        forceratio = force / absolute_distance

        for direction in ['x', 'y', 'z']:
            force = distance_in_directions[direction] * forceratio
            acceleration[direction] = force / self.mass

        return acceleration
        
    def acceleration_to_all(self, bodies: [Body]) -> dict:
        """Function will be moved"""

        total_acceleration = {"x": 0, "y": 0, "z": 0}

        for body in bodies:
            acceleration = self.acceleration_to_one(body)
            for direction in ['x', 'y', 'z']:
                total_acceleration[direction] += acceleration[direction]

        return total_acceleration
        
    def calculate_position(self, change_in_time: float) -> None:
        """ Calculates a new position for a new tick. Function will be moved."""
        for direction in ["x", "y", "z"]:
            self.position[direction] += change_in_time * self.velocity[direction]
    
    def calculate_velocity(self, bodies, change_in_time: float) -> None:
        """ Calculates new velocity for a new tick. Function will be moved."""
        acceleration = self.acceleration_to_all(bodies)

        for direction in ["x", "y", "z"]:
            self.velocity[direction] += change_in_time * acceleration[direction]