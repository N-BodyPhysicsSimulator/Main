import numpy as np
import os

from .output_writer import OutputWriter

from nbp import validate_is_dir

class CSVOutputWriter(OutputWriter):
    @staticmethod
    def get_validation_schema():
        return {
            'path': {
                'required': True,
                'type': 'string',
                'empty': False,
                'validator': validate_is_dir
            }
        }

    def tick(self, get_state, args):
        path = args.get('path')

        while True:
            state = get_state()

            for body in state.bodies:
                filepath = os.path.join(path, (body.name + '.csv') )

                if not os.path.exists(filepath):
                    f = open(filepath, 'a+')
                    f.write('name,mass,radius,pos.x,pos.y,pos.z,vel.x,vel.y,vel.z,ticks,time,delta_time')
                    f.close()

                data  = [body.name, body.mass, body.radius]
                data += self.__to_list(body.position)
                data += self.__to_list(body.velocity)
                data += [state.ticks, state.time, state.delta_time]

                f = open(filepath, 'a+')
                f.write("\n")
                f.write(','.join([str(item) for item in data]))
                f.close()

    def __to_list(self, item):
        return [item[0][0], item[1][0], item[2][0]]

