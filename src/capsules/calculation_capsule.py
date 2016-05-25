from ..models import Body

class CalculationCapsule(object):
    def __init__(self, bodies: [Body], change_in_time: float):
        self.bodies = bodies
        self.ticks = 0
        self.change_in_time = change_in_time # Delta Time
        self.time = 0

    def minimal_distance(self) -> float:
        """Return the smallest distance between all bodies."""
        smallest_distance = 0

        for body in self.bodies:
            for other_body in self.bodies:
                if body == other_body: continue
                distance = numpy.linalg.norm(body.distance_to(other_body))
                
                if smallest_distance == None or smallest_distance > distance:
                    smallest_distance = distance
        
        return float(smallest_distance)

    def calculate(self) -> [Body]:
        self.ticks += 1
        self.time += self.change_in_time

        change_change_in_time()

        for body in bodies: body.calculate_position(self.change_in_time)
        for body in bodies: body.calculate_velocity(self.bodies, self.change_in_time)

    def change_change_in_time(self):
        pass