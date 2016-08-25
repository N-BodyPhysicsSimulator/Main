from .output_writer import OutputWriter

import asyncio
import websockets

class WSOutputWriter(object):
    @staticmethod
    def get_validation_schema():
        return {}
    
    def tick(self, state, args):
        print(state.to_json())
    #def __init__(self, pipe, kwargs):
        #port = kwargs.get('port')

        #def hello(websocket, path):
        #    while True:
        #        state = pipe.recv()
        #        websocket.send(state.to_json())

        #start_server = websockets.serve(hello, 'localhost', 8080)

        #asyncio.get_event_loop().run_until_complete(start_server)
        #asyncio.get_event_loop().run_forever()

        
