import bottle
from gevent import monkey

from nbp.decorators import entity
from nbp.helpers.validation import int_is_valid_port
from .output_writer import OutputWriter


@entity("http")
class HTTPOutputWriter(OutputWriter):
    @staticmethod
    def get_cli_arguments() -> list:
        return [
            (
                '--http-port',
                {
                    'metavar': 'port',
                    'type': int_is_valid_port,
                    'help': 'Port to run on, required when using the HTTP Output Provider.',
                    'dest': 'http_port',
                    'required': True
                }
            )
        ]

    def tick(self, get_state, args):
        monkey.patch_all()

        @bottle.route('/')
        def default():
            bottle.response.content_type = "text/plain"

            while True:
                yield get_state().to_json()
                yield "\n"

        bottle.run(port=args.get("http_port"), server="gevent")
