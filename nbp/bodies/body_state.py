from nbp.bodies import Body

class BodyState(object):
    def __init__(self, bodies: [Body], ticks: int, time: float, delta_time: float):
        self.bodies, self.ticks, self.time, self.delta_time = bodies, ticks, time, delta_time
