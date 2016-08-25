from cerberus import Validator

class OutputWritingsManager(object):
    def __init__(self, pipe, args, output_writer):
        self.__pipe, self.__args = pipe, args
        self.__output_writer = output_writer

        self.__validate(args, output_writer.get_validation_schema())

        while True:
            output_writer.tick(pipe.recv(), args)

    def __validate(self, args, schema):
        validator = Validator(schema, allow_unknown=True)

        if not validator.validate(args):
            for field, error in validator.errors.items():
                print(field, error)

            raise Exception('Validation errors have occured.')

        
