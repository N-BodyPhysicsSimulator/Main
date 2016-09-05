import json
from typing import Iterator

from nbp.bodies import BodyState
from nbp.decorators import entity
from nbp.helpers.validation import str_is_existing_file
from nbp.io.input_providers import InputProvider


@entity("csv")
class CSVInputProvider(InputProvider):
    @staticmethod
    def get_cli_arguments() -> list:
        return [
            (
                '--csv-input-file',
                {
                    'metavar': 'path',
                    'type': str_is_existing_file,
                    'help': 'Path to CSV file.',
                    'dest': 'csv_input_path',
                    'required': True
                }
            ),
            (
                '--separator',
                {
                    'metavar': ',.;',
                    'type': str,
                    'help': 'Separator in CSV-file.',
                    'dest': 'separator',
                    'default': ','
                }
            )
        ]

    def get_generator(self) -> Iterator[BodyState]:
        path = self.args.get('csv_input_path')
        separator = self.args.get('separator')

        bodies = self.__get_bodies_from_path(path, separator)

        yield BodyState.from_dict({
            'bodies': bodies,
            'ticks': 0,
            'time': 0,
            'delta_time': self.args.get('delta_time')
        })

    def __get_bodies_from_path(self, path, separator):
        bodies = []

        with open(path) as f:
            for index, line in enumerate(f.readlines()):
                if index is 0:
                    column_names = line.split(separator)
                else:
                    body = dict(zip(column_names, line.split(separator)))

                    bodies.append({
                        'name': str(body['name']),
                        'radius': float(body['radius']),
                        'mass': float(body['mass']),
                        'position': {
                            'x': float(body['pos.x']),
                            'y': float(body['pos.x']),
                            'z': float(body['pos.x'])
                        },
                        'velocity': {
                            'x': float(body['vel.x']),
                            'y': float(body['vel.x']),
                            'z': float(body['vel.x'])
                        }
                    })

        return bodies
