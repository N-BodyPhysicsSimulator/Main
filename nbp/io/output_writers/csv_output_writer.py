import os

from nbp.decorators import entity
from nbp.helpers.numpy import numpy_to_list
from nbp.helpers.validation import str_is_existing_dir
from .output_writer import OutputWriter


@entity("csv")
class CSVOutputWriter(OutputWriter):
    @staticmethod
    def get_cli_arguments() -> list:
        return [
            (
                '--path',
                {
                    'metavar': 'path',
                    'type': str_is_existing_dir,
                    'help': 'Path for output, required when using the CSV Output Provider.',
                    'dest': 'path',
                    'required': True
                }
            )
        ]

    def handle(self, generator, args):
        path = args.get('path')

        for state in generator:
            for body in state.bodies:
                filepath = os.path.join(path, (body.name + '.csv'))

                if not os.path.exists(filepath):
                    f = open(filepath, 'a+')
                    f.write('name,mass,radius,pos.x,pos.y,pos.z,vel.x,vel.y,vel.z,ticks,time,delta_time')
                    f.close()

                data = [body.name, body.mass, body.radius]
                data += numpy_to_list(body.position)
                data += numpy_to_list(body.velocity)
                data += [state.ticks, state.time, state.delta_time]

                f = open(filepath, 'a+')
                f.write("\n")
                f.write(','.join([str(item) for item in data]))
                f.close()
