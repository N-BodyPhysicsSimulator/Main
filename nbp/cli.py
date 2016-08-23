import argparse

from nbp.io.input_providers import DummyFileInputProvider
from nbp.io.output_writers import CSVOutputWriter
from nbp.io.output_writers import WSOutputWriter

class cli:
    input_providers = {
        'dummy': DummyFileInputProvider
    }

    output_writers = {
        'csv': CSVOutputWriter,
        'ws': WSOutputWriter,
    }
    
    @staticmethod
    def start(args):
        print(args)
        input_provider_class = cli.input_providers[args.inputprovider]
        output_writer_class = cli.output_writers[args.outputwriter]

        input_provider = input_provider_class('')
        output_writer = output_writer_class(input_provider.get_body_states(), **vars(args))

    @staticmethod
    def get_parser():
        parser = argparse.ArgumentParser(description='N-Body Physics Simulator')
        parser.add_argument('--inputprovider', metavar='i',
                            type=str, help='Selection of Input Provider',
                            dest='inputprovider')

        parser.add_argument('--outputwriter', metavar='o', 
                            type=str, help='Selection of Output Writers',
                            dest='outputwriter')

        parser.add_argument('--path', metavar='p', 
                            type=str, help='Path of output, might be required.',
                            dest='path')

        parser.add_argument('--max-ticks', metavar='p', 
                            type=str, help='Max ticks to calculate, might be required.',
                            dest='max_ticks')

        return parser
