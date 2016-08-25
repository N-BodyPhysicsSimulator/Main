import argparse
import queue

from threading import Thread
from multiprocessing import Pipe

from nbp.io.input_providers import DummyFileInputProvider
from nbp.io.output_writers import CSVOutputWriter
from nbp.io.output_writers import WSOutputWriter

from nbp.io.output_writers import OutputWritingsManager

from nbp.modifiers import CalculationModifier

from nbp.modifiers import ModificationManager

class Cli:
    __input_providers = {
        'dummy': DummyFileInputProvider
    }

    __output_writers = {
        'csv': CSVOutputWriter,
        'ws': WSOutputWriter,
    }

    __modifiers = {
        'calculation': CalculationModifier
    }
    
    def __init__(self, args):
        self.__args = args

    def start_application(self):
        input_provider_class = self.__input_providers[self.__args.inputprovider]

        input_provider = input_provider_class('')
        generator = input_provider.get_body_states()

        pipes = []

        if self.__args.modifier:
            for modifier_name in self.__args.modifier:
                modifier = self.__modifiers[modifier_name]()
                generator = ModificationManager(generator, modifier).get_generator()

        for ow_name in self.__args.outputwriter:
            parent, child = Pipe()

            ow = self.__output_writers[ow_name]()
            Thread(target=OutputWritingsManager, args=(child, vars(self.__args), ow)).start()

            pipes.append(parent)

        for state in generator:
            for parent in pipes:
                parent.send(state)

    @staticmethod
    def get_parser():
        parser = argparse.ArgumentParser(description='N-Body Physics Simulator')

        parser.add_argument('--inputprovider', metavar='ip',
                            type=str, help='Selection of Input Provider.',
                            dest='inputprovider', required=True)

        parser.add_argument('--outputwriter', metavar='outputwriters', 
                            type=str, help='Selection of Output Writers.',
                            dest='outputwriter', nargs='+', required=True)

        parser.add_argument('--modifier', metavar='modifiers', 
                            type=str, help='Selection of modifier(s).',
                            dest='modifier', nargs='*')

        parser.add_argument('--port', metavar='port', 
                            type=str, help='Port to run on, might be required.',
                            dest='port')

        parser.add_argument('--path', metavar='path', 
                            type=str, help='Path of output, might be required.',
                            dest='path')

        parser.add_argument('--max-ticks', metavar='ticks', 
                            type=str, help='Max ticks to calculate.',
                            dest='max_ticks')

        parser.add_argument('--max-time', metavar='time', 
                            type=str, help='Max time to calculate.',
                            dest='max_ticks')

        return parser
