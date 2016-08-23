import asyncio
import websockets

class WSOutputWriter(object):
    def __init__(self, body_states, **kwargs):
        port = kwargs.get('port')
        max_ticks = kwargs.get('max_ticks')

        #if max_ticks:
        #    max = range(0, int(max_ticks))
        #else:
        #    max = iter(int, 1) #inf

        #for body_state in max:
        #    self.__tick(port, next(body_states))

        async def hello(websocket, path):
            for bs in body_states:
                await websocket.send(bs.to_json())

        start_server = websockets.serve(hello, 'localhost', 8080)

        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()

        
