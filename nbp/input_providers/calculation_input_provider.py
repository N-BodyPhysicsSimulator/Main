from nbp.bodies import Body

class CalculationInputProvider(object):
    def __init__(self, bodies: [Body], time_zones: {}):
        self.bodies = bodies
        self.ticks = 0
        self.delta_time = time_zones["delta_time0"] # Change in time
        self.time_zones = time_zones # A dictionary with the time zones {"amount_time_zones": X, "delta_time0": Y, "delta_time_radius0": Z, etc...}
        self.time = 0

    def minimal_distance(self) -> float:
        """Return the smallest distance between all bodies.
        >>> sun = Body('Sun', 1989000000000000000000000000000, 100, (0, 0, 0), (0, 0, 0))
        >>> earth = Body('earth', 5972000000000000000000000, 100, (0, 152100000000, 1000), (29290, 0, 32))
        >>> moon = Body('moon', 73460000000000000000000, 100, (405500000, 152100000000, 175000), (29290, 964, 0))
        >>> jupiter = Body('jupiter', 1900000000000000000000000000, 100, (816620000000, 0, -1000), (40, 12440, 1))
        >>> saturn = Body('saturn', 568000000000000000000000000, 100, (0, 1352550000000, 0), (0, 10180, 0))
        >>> neptune = Body('neptune', 102413000000000000000000000, 100, (0, -4444450000000, 500000), (-5370, 0, 0))
        >>> bodies = [sun, earth, moon, jupiter, saturn, neptune]
        >>> calculator = CalculationInputProvider(bodies, {"amount_time_zones": 2, "delta_time0": 60, "delta_time_radius0": 395500000, "delta_time1": 3600, "delta_time_radius1": 152100000000})
        >>> calculator.minimal_distance()
        405500037.33168757
        >>> sun = Body('Sun', 1989000000000000000000000000000, 100, (0, 0, 0), (0, 0, 0))
        >>> earth = Body('earth', 5972000000000000000000000, 100, (107550941418, 107550941418, 100000), (29290, 0, 32))
        >>> jupiter = Body('jupiter', 1900000000000000000000000000, 100, (816620000000, 0, -1000), (40, 12440, 1))
        >>> saturn = Body('saturn', 568000000000000000000000000, 100, (0, 1352550000000, 0), (0, 10180, 0))
        >>> neptune = Body('neptune', 102413000000000000000000000, 100, (0, -4444450000000, 500000), (-5370, 0, 0))
        >>> bodies = [sun, earth, jupiter, saturn, neptune]
        >>> calculator = CalculationInputProvider(bodies, {"amount_time_zones": 2, "delta_time0": 60, "delta_time_radius0": 395500000, "delta_time1": 3600, "delta_time_radius1": 152100000000})
        >>> calculator.minimal_distance()
        152099999999.3627
        """
        smallest_distance = 0.0

        for body in self.bodies:
            for other_body in self.bodies:
                if body == other_body:
                    continue

                distance = body.absolute_distance_to_one(other_body)
                if smallest_distance <= 0.0 or smallest_distance > distance:
                    smallest_distance = distance

        return float(smallest_distance)

    def calculate_one_tick(self) -> [Body]:
        """ Calculates one tick of the simulator
        >>> sun = Body('Sun', 1989000000000000000000000000000, 100, (0, 0, 0), (0, 0, 0))
        >>> earth = Body('earth', 5972000000000000000000000, 100, (0, 152100000000, 1000), (29290, 0, 32))
        >>> moon = Body('moon', 73460000000000000000000, 100, (405500000, 152100000000, 175000), (29290, 964, 0))
        >>> jupiter = Body('jupiter', 1900000000000000000000000000, 100, (816620000000, 0, -1000), (40, 12440, 1))
        >>> saturn = Body('saturn', 568000000000000000000000000, 100, (0, 1352550000000, 0), (0, 10180, 0))
        >>> neptune = Body('neptune', 102413000000000000000000000, 100, (0, -4444450000000, 500000), (-5370, 0, 0))
        >>> bodies = [sun, earth, moon, jupiter, saturn, neptune]
        >>> calculator = CalculationInputProvider(bodies, {"amount_time_zones": 2, "delta_time0": 60, "delta_time_radius0": 395500000, "delta_time1": 3600, "delta_time_radius1": 152100000000})
        >>> while calculator.time<(15 * 24 * 3600): calculator.calculate_one_tick()
        >>> calculator.bodies[1].position
        array([[37568574109.24809],
               [147326604988.20786],
               [40489728.17162777]], dtype=object)
        >>> calculator.bodies[5].position
        array([[-6959516107.873012],
               [-4444444355076.259],
               [499999.3655157559]], dtype=object)
        >>> calculator.bodies[5].velocity
        array([[-5369.991721566399],
               [8.718903683962962],
               [-9.795800343391017e-07]], dtype=object)
        """
        self.ticks += 1
        self.time += self.delta_time

        for body in self.bodies:
            body.calculate_position(self.delta_time)

        for body in self.bodies:
            body.calculate_velocity(self.bodies, self.delta_time)

        self.change_delta_time()

    def calculate(self):
        pass

    def change_delta_time(self):
        """ Changes delta time based on the distance between bodies. 
        @TODO: Refactor 
        """
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
