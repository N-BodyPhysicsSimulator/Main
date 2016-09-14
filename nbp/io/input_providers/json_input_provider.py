import json
from types import GeneratorType
from typing import Iterator

from nbp.bodies import Body
from nbp.bodies import BodyState
from nbp.decorators import entity
from nbp.helpers.validation import dirname_is_existing_dir
from nbp.io.input_providers import InputProvider


@entity("json")
class JSONInputProvider(InputProvider):
    @staticmethod
    def get_cli_arguments() -> list:
        return [
            (
                '--json-input-file',
                {
                    'metavar': 'path',
                    'type': dirname_is_existing_dir,
                    'help': 'Path to JSON file.',
                    'dest': 'json_input_path',
                    'required': True
                }
            )
        ]

    def get_generator(self) -> Iterator[BodyState]:
        path = self.args.get('json_input_path')

        with open(path) as f:
            for line in f.readlines():
                yield BodyState.from_dict(
                    json.loads(line)
                )
