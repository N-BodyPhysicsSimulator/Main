from nbp.decorators import entity
from nbp.helpers.validation import str_is_existing_file
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
                    'type': str_is_existing_file,
                    'help': 'Path to JSON file.',
                    'dest': 'json_output_path',
                    'required': True
                }
            )
        ]

    def tick(self, get_state, args):
        path = args.get('json_output_path')

        with open(path, "a") as f:
            while True:
                f.write(
                    get_state().to_json() + "\n"
                )
