from ..bodies import Body

class CalculationInputProvider(object):
    def __init__(self, bodies: [Body], time_zones: {}):
        self.bodies = bodies
        self.ticks = 0
        self.delta_time = time_zones["delta_time0"] # Change in time
        self.time_zones = time_zones # A dictionary with the time zones {"amount_time_zones": X, "delta_time0": Y, "delta_time_radius0": Z, etc...}
        self.time = 0

    def minimal_distance(self) -> float:
        """Return the smallest distance between all bodies."""
        smallest_distance = 0.0

        for body in self.bodies:
            for other_body in self.bodies:
                if body == other_body: continue
                distance = body.absolute_distance_to_one(other_body)
                
                if smallest_distance == None or smallest_distance > distance:
                    smallest_distance = distance
        
        return float(smallest_distance)

    def calculate_one_tick(self) -> [Body]:
        self.ticks += 1
        self.time += self.delta_time

        for body in bodies: body.calculate_position(self.delta_time)
        for body in bodies: body.calculate_velocity(self.bodies, self.delta_time)
        
        self.change_delta_time()
    
    def calculate(self):
        pass

    def def change_delta_time(self):
        amount_time_zones = self.time_zones["amount_time_zones"]
        if amount_time_zones > 0:
            minimal_distance = self.minimal_distance()
            for number in range(1, amount_time_zones):
                maxradiusnum = number
                minradiusnum = number - 1
                if self.time_zones["delta_time_radius%s" %maxradiusnum] >= minimal_distance and self.time_zones["delta_time_radius%s" %minradiusnum] < minimal_distance:
                    self.delta_time = self.time_zones["delta_time%s" %maxradiusnum]
                elif self.time_zones["delta_time_radius%s" %maxradiusnum] < minimal_distance:
                    self.delta_time = self.time_zones["delta_time%s" %maxradiusnum]
                elif self.time_zones["delta_time_radius%s" %minradiusnum] > minimal_distance:
                    self.delta_time = self.time_zones["delta_time%s" %minradiusnum]
                else:
                    self.delta_time = self.time_zones["delta_time0"]
                    raise ValueError("Minimal distance is smaller than zero or wrong time zone settings")
    
    