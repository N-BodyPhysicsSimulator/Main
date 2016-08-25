from .output_writer import OutputWriter

import asyncio
import websockets

class WSOutputWriter(OutputWriter):
    @staticmethod
    def get_validation_schema():
        return {}
    
    def tick(self, get_state, args):
        while True:
            print(get_state().to_json())
