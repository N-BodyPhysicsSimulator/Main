import json

from nbp.decorators import entity
from nbp.helpers.validation import dirname_is_existing_dir
from nbp.io.output_writers.output_writer import OutputWriter


@entity("json")
class JSONOutputWriter(OutputWriter):
    @staticmethod
    def get_cli_arguments() -> list:
        return [
            (
                '--json-output-file',
                {
                    'metavar': 'path',
                    'type': dirname_is_existing_dir,
                    'help': 'Path to JSON file.',
                    'dest': 'json_output_path',
                    'required': True
                }
            )
        ]

    def handle(self, generator):
        path = self.args.get('json_output_path')

        with open(path, "a") as f:
            for state in generator:
                f.write(
                    json.dumps(state.to_dict()) + "\n"
                )
