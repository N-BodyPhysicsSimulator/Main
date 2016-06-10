from nbp.io.input_providers.file_input_provider import FileInputProvider
from nbp.bodies.body import Body

class CSVStartValueInputProvider(FileInputProvider):
    def get_bodies(self) -> [Body]:
        """ @TODO: Write doctest """
        bodies = []

        with open(self.get_filepath(), 'r') as opened_file:
            columns = None

            file = filter(
                lambda l: len(l) > 0,
                map(
                    lambda l: l.split(','),
                    opened_file.read().split("\n")
                )
            )

            opened_file.close()

            for _, line in enumerate(file):
                if columns is None:
                    columns = line
                else:
                    line = [self.__parse_string_value(v) for v in line]
                    bodies.append(
                        self.__dict_to_body(
                            self.__combine_lists(columns, line)
                        )
                    )

        return bodies

    def __combine_lists(self, keys, values):
        return dict(zip(keys, values))

    def __parse_string_value(self, string_value):
        try:
            return float(string_value)
        except ValueError: # if not number
            return string_value

    def __dict_to_body(self, body_dict) -> Body:
        return Body(
            body_dict['name'],
            body_dict['mass'],
            body_dict['radius'],
            (body_dict['position.x'], body_dict['position.y'], body_dict['position.z']),
            (body_dict['velocity.x'], body_dict['velocity.y'], body_dict['velocity.z'])
        )
