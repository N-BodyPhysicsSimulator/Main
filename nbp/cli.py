import argparse
import queue

from threading import Thread
from multiprocessing import Pipe

from nbp.io.input_providers import DummyFileInputProvider
from nbp.io.output_writers import CSVOutputWriter
from nbp.io.output_writers import WSOutputWriter

from nbp.modifiers import CalculationModifier

class cli:
    input_providers = {
        'dummy': DummyFileInputProvider
    }

    output_writers = {
        'csv': CSVOutputWriter,
        'ws': WSOutputWriter,
    }

    modifiers = {
        'calculation': CalculationModifier
    }
    
    @staticmethod
    def start(args):
        print(args)
        input_provider_class = cli.input_providers[args.inputprovider]

        input_provider = input_provider_class('')
        generator = input_provider.get_body_states()

        pipes = []

        for modifier_name in args.modifier:
            modifier_class = cli.modifiers[modifier_name]
            generator = modifier_class(generator).get_generator()

        for ow_name in args.outputwriter:
            parent, child = Pipe()
            ow_class = cli.output_writers[ow_name]
            Thread(target=ow_class, args=(child, vars(args))).start()

            pipes.append(parent)

        for state in generator:
            for parent in pipes:
                parent.send(state)

    @staticmethod
    def get_parser():
        parser = argparse.ArgumentParser(description='N-Body Physics Simulator')

        parser.add_argument('--inputprovider', metavar='i',
                            type=str, help='Selection of Input Provider',
                            dest='inputprovider')

        parser.add_argument('--outputwriter', metavar='o', 
                            type=str, help='Selection of Output Writers',
                            dest='outputwriter', nargs='*')

        parser.add_argument('--modifier', metavar='m', 
                            type=str, help='Selection of modifier(s).',
                            dest='modifier', nargs='*')

        parser.add_argument('--port', metavar='p', 
                            type=str, help='Port to run on.',
                            dest='port')

        parser.add_argument('--path', metavar='P', 
                            type=str, help='Path of output, might be required.',
                            dest='path')

        parser.add_argument('--max-ticks', metavar='M', 
                            type=str, help='Max ticks to calculate, might be required.',
                            dest='max_ticks')

        return parser
