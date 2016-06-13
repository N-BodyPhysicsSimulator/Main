from nbp.bodies import Body

class CalculationInputProvider(object):
    def __init__(self, bodies: [Body], time_zones):
        self.bodies = bodies
        self.ticks = 0
        self.delta_time = min(time_zones['time']) # Change in time #todo make it take the absolute smallest number so it can also be negitive time.
        self.time_zones = time_zones # A list with the time zones in one list and the time zones radius in antohter can be in a random order {'time': [3, 2, 4, 1], 'radius': [200, 300, 100, 400]}
        self.time = 0

        self.time_zones['time'].sort()
        self.time_zones['radius'].sort()

    def minimal_distance(self) -> float:
        """Return the smallest distance between all bodies.
        >>> sun = Body('Sun', 1989000000000000000000000000000, 100, (0, 0, 0), (0, 0, 0))
        >>> earth = Body('earth', 5972000000000000000000000, 100, (0, 152100000000, 1000), (29290, 0, 32))
        >>> moon = Body('moon', 73460000000000000000000, 100, (405500000, 152100000000, 175000), (29290, 964, 0))
        >>> jupiter = Body('jupiter', 1900000000000000000000000000, 100, (816620000000, 0, -1000), (40, 12440, 1))
        >>> saturn = Body('saturn', 568000000000000000000000000, 100, (0, 1352550000000, 0), (0, 10180, 0))
        >>> neptune = Body('neptune', 102413000000000000000000000, 100, (0, -4444450000000, 500000), (-5370, 0, 0))
        >>> bodies = [sun, earth, moon, jupiter, saturn, neptune]
        >>> calculator = CalculationInputProvider(bodies, {'time': [60, 3600], 'radius': [395500000, 152100000000]})
        >>> calculator.minimal_distance()
        405500037.33168757
        >>> sun = Body('Sun', 1989000000000000000000000000000, 100, (0, 0, 0), (0, 0, 0))
        >>> earth = Body('earth', 5972000000000000000000000, 100, (0, 152100000000, 1000), (29290, 0, 32))
        >>> moon = Body('moon', 73460000000000000000000, 100, (-405500000, 152100000000, -174000), (29290, 964, 0))
        >>> jupiter = Body('jupiter', 1900000000000000000000000000, 100, (816620000000, 0, -1000), (40, 12440, 1))
        >>> saturn = Body('saturn', 568000000000000000000000000, 100, (0, 1352550000000, 0), (0, 10180, 0))
        >>> neptune = Body('neptune', 102413000000000000000000000, 100, (0, -4444450000000, 500000), (-5370, 0, 0))
        >>> bodies = [sun, earth, moon, jupiter, saturn, neptune]
        >>> calculator = CalculationInputProvider(bodies, {'time': [60, 3600], 'radius': [395500000, 152100000000]})
        >>> calculator.minimal_distance()
        405500037.7620204
        >>> sun = Body('Sun', 1989000000000000000000000000000, 100, (0, 0, 0), (0, 0, 0))
        >>> earth = Body('earth', 5972000000000000000000000, 100, (107550941418, 107550941418, 100000), (29290, 0, 32))
        >>> jupiter = Body('jupiter', 1900000000000000000000000000, 100, (816620000000, 0, -1000), (40, 12440, 1))
        >>> saturn = Body('saturn', 568000000000000000000000000, 100, (0, 1352550000000, 0), (0, 10180, 0))
        >>> neptune = Body('neptune', 102413000000000000000000000, 100, (0, -4444450000000, 500000), (-5370, 0, 0))
        >>> bodies = [sun, earth, jupiter, saturn, neptune]
        >>> calculator = CalculationInputProvider(bodies, {'time': [60, 3600], 'radius': [395500000, 152100000000]})
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

    def change_delta_time(self):
        """ Changes delta time based on the distance between bodies. 
        >>> body1 = Body('body1', 1, 100, (0, 0, 0), (0, 0, 0))
        >>> body2 = Body('body2', 1, 100, (0, 99, 0), (0, 0, 0))
        >>> bodies = [body1, body2]
        >>> calculator = CalculationInputProvider(bodies, {'time': [3, 2, 4, 1], 'radius': [200, 300, 100, 400]}) #{"amount_time_zones": 4,"delta_time1": 1, "delta_time_radius1": 100, "delta_time2": 2, "delta_time_radius2": 200, "delta_time3": 3, "delta_time_radius3": 300, "delta_time4": 4, "delta_time_radius4": 400})
        >>> calculator.change_delta_time()
        >>> calculator.delta_time
        1
        >>> body1 = Body('body1', 1, 100, (0, 0, 0), (0, 0, 0))
        >>> body2 = Body('body2', 1, 100, (0, 146.32, 0), (0, 0, 0))
        >>> bodies = [body1, body2]
        >>> calculator.bodies = bodies
        >>> calculator.change_delta_time()
        >>> calculator.delta_time
        2
        >>> body1 = Body('body1', 1, 100, (0, 0, 0), (0, 0, 0))
        >>> body2 = Body('body2', 1, 100, (0, 200, 0), (0, 0, 0))
        >>> bodies = [body1, body2]
        >>> calculator.bodies = bodies
        >>> calculator.change_delta_time()
        >>> calculator.delta_time
        2
        >>> body1 = Body('body1', 1, 100, (0, 0, 0), (0, 0, 0))
        >>> body2 = Body('body2', 1, 100, (0, 201, 0), (0, 0, 0))
        >>> bodies = [body1, body2]
        >>> calculator.bodies = bodies
        >>> calculator.change_delta_time()
        >>> calculator.delta_time
        3
        >>> body1 = Body('body1', 1, 100, (0, 0, 0), (0, 0, 0))
        >>> body2 = Body('body2', 1, 100, (0, 314, 0), (0, 0, 0))
        >>> bodies = [body1, body2]
        >>> calculator.bodies = bodies
        >>> calculator.change_delta_time()
        >>> calculator.delta_time
        4
        >>> body1 = Body('body1', 1, 100, (0, 0, 0), (0, 0, 0))
        >>> body2 = Body('body2', 1, 100, (0, 403, 0), (0, 0, 0))
        >>> bodies = [body1, body2]
        >>> calculator.bodies = bodies
        >>> calculator.change_delta_time()
        >>> calculator.delta_time
        4
        >>> body1 = Body('body1', 1, 100, (0, 0, 0), (0, 0, 0))
        >>> body2 = Body('body2', 1, 100, (0, -152100000000, 0), (0, 0, 0))
        >>> bodies = [body1, body2]
        >>> calculator.bodies = bodies
        >>> calculator.change_delta_time()
        >>> calculator.delta_time
        4
        >>> body1 = Body('body1', 1, 100, (0, 0, 0), (0, 0, 0))
        >>> body2 = Body('body2', 1, 100, (0, -154, 0), (0, 0, 0))
        >>> bodies = [body1, body2]
        >>> calculator.bodies = bodies
        >>> calculator.change_delta_time()
        >>> calculator.delta_time
        2
        """
        minimal_distance = self.minimal_distance()
        
        for zone_i, _ in enumerate(self.time_zones['time']):
            zones = {
                'upper': {
                    'index': zone_i
                },
                'lower': {
                    'index': zone_i - 1
                }
            }

            for zone_type in ['upper', 'lower']:
                i = zones[zone_type]['index']

                for zone_input in ['radius', 'time']:
                    zones[zone_type][zone_input] = self.time_zones[zone_input][i]

            if ((zones['upper']['index'] == 0 and minimal_distance < zones['upper']['radius'])
                    or (zones['lower']['radius'] < minimal_distance and zones['upper']['radius'] >= minimal_distance)
                    or (zones['upper']['radius'] < minimal_distance)): # We could combine these 3 if-statements
                self.delta_time = zones['upper']['time']
            # else: self.delta_time = self.delta_time

    def calculate_one_tick(self) -> [Body]:
        """ Calculates one tick of the simulator
        >>> sun = Body('Sun', 1989000000000000000000000000000, 100, (0, 0, 0), (0, 0, 0))
        >>> earth = Body('earth', 5972000000000000000000000, 100, (0, 152100000000, 1000), (29290, 0, 32))
        >>> moon = Body('moon', 73460000000000000000000, 100, (405500000, 152100000000, 175000), (29290, 964, 0))
        >>> jupiter = Body('jupiter', 1900000000000000000000000000, 100, (816620000000, 0, -1000), (40, 12440, 1))
        >>> saturn = Body('saturn', 568000000000000000000000000, 100, (0, 1352550000000, 0), (0, 10180, 0))
        >>> neptune = Body('neptune', 102413000000000000000000000, 100, (0, -4444450000000, 500000), (-5370, 0, 0))
        >>> bodies = [sun, earth, moon, jupiter, saturn, neptune]
        >>> calculator = CalculationInputProvider(bodies, {'time': [60, 3600], 'radius': [395500000, 152100000000]})
        >>> while calculator.time < (0.24 * 24 * 3600): calculator.calculate_one_tick()
        >>> calculator.bodies[1].position
        array([[634425450.6842861],
               [152098877195.82477],
               [694116.6414370898]], dtype=object)
        >>> calculator.bodies[5].position
        array([[-116314199.7670317],
               [-4444449998683.439],
               [499999.9998518952]], dtype=object)
        >>> calculator.bodies[5].velocity
        array([[-5369.999973472422],
               [0.14571932401226062],
               [-1.6392377850297617e-08]], dtype=object)
        """
        self.ticks += 1
        self.time += self.delta_time

        for body in self.bodies:
            body.calculate_position(self.delta_time)

        for body in self.bodies:
            body.calculate_velocity(self.bodies, self.delta_time)

        self.change_delta_time()