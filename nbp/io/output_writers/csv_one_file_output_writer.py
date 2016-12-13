import os

from nbp.decorators import entity
from nbp.helpers.numpy import numpy_to_list
from nbp.helpers.validation import dirname_is_existing_dir
from .output_writer import OutputWriter


@entity("csv_one_file")
class CSVOneFileOutputWriter(OutputWriter):
    @staticmethod
    def get_cli_arguments() -> list:
        return [
            (
                '--csv-1f-output-file',
                {
                    'metavar': 'path',
                    'type': dirname_is_existing_dir,
                    'help': 'Path for output, required when using the CSV One File Output Provider.',
                    'dest': 'path',
                    'required': True
                }
            )
        ]

    def handle(self, generator):
        path = self.args.get('path')

        for state in generator:
            for body in state.bodies:
                if not os.path.exists(path):
                    f = open(path, 'a+')
                    f.write('name,mass,radius,pos.x,pos.y,pos.z,vel.x,vel.y,vel.z,ticks,time,delta_time')
                    f.close()

                data = [body.name, body.mass, body.radius]
                data += numpy_to_list(body.position)
                data += numpy_to_list(body.velocity)
                data += [state.ticks, state.time, state.delta_time]

                f = open(path, 'a+')
                f.write("\n")
                f.write(','.join([str(item) for item in data]))
                f.close()
