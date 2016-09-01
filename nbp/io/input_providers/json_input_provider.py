import json
from types import GeneratorType

from nbp.bodies import Body
from nbp.bodies import BodyState
from nbp.decorators import entity
from nbp.helpers.validation import str_is_existing_file
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
                    'type': str_is_existing_file,
                    'help': 'Path to JSON file.',
                    'dest': 'json_input_path',
                    'required': True
                }
            )
        ]

    def get_body_states(self) -> GeneratorType:
        path = self.args.get('json_input_path')

        with open(path) as f:
            for line in f.readlines():
                yield BodyState.from_dict(
                    json.loads(line)
                )
