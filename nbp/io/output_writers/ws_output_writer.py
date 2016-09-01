import asyncio

import websockets

from nbp.decorators import entity
from nbp.helpers.validation import int_is_valid_port
from .output_writer import OutputWriter


@entity("ws")
class WSOutputWriter(OutputWriter):
    @staticmethod
    def get_cli_arguments() -> list:
        return [
            (
                '--ws-port',
                {
                    'metavar': 'port',
                    'type': int_is_valid_port,
                    'help': 'Port to run on, required when using the WebSocket Output Provider.',
                    'dest': 'ws_port',
                    'required': True
                }
            )
        ]
    
    def tick(self, get_state, args):
        async def server(client, _):
            while True:
                await client.send(get_state().to_json())

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        asyncio.get_event_loop().run_until_complete(
            websockets.serve(server, 'localhost', args.get('ws_port'))
        )
        asyncio.get_event_loop().run_forever()
