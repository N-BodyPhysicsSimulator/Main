from nbp.bodies import Body

import json

class BodyState(object):
    def __init__(self, bodies: [Body], ticks: int, time: float, delta_time: float):
        self.bodies, self.ticks, self.time, self.delta_time = bodies, ticks, time, delta_time

    def to_dict(self):
        return {
            'ticks': self.ticks,
            'time': self.time,
            'delta_time': self.delta_time,
            'bodies': [body.to_dict() for body in self.bodies]
        }

    def to_json(self):
        return json.dumps(self.to_dict())
