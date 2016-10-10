import asyncio

import websockets
import json

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
            ),
            (
                '--ws-host',
                {
                    'metavar': '<host>',
                    'type': str,
                    'help': 'Host to run on.',
                    'dest': 'ws_host',
                    'default': 'localhost'
                }
            )
        ]

    def exit(self):
        for client in self.clients:
            client.close()

        loop = asyncio.get_event_loop()

        loop.stop()
        loop.close()
    
    def handle(self, generator):
        self.clients = []

        async def server(client, _):
            self.clients.append(client)

            for state in generator:
                await client.send(json.dumps(state.to_dict()))

        asyncio.set_event_loop(
            asyncio.new_event_loop()
        )

        asyncio.get_event_loop().run_until_complete(
            websockets.serve(server, self.args.get('ws_host'), self.args.get('ws_port'))
        )

        asyncio.get_event_loop().run_forever()
