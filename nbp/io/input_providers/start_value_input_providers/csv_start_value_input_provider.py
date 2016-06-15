from nbp.io.input_providers.file_input_provider import FileInputProvider
from nbp.bodies.body import Body

def combine_lists(keys, values):
    """
    >>> d = combine_lists(['hallo', 'test'], ['a', 'b'])
    >>> d == {'hallo': 'a', 'test': 'b'}
    True
    >>> d = combine_lists(['name', 'mass', 'radius'], ['Earth', 12345.123, 123E123])
    >>> d == {'mass': 12345.123, 'radius': 1.23e+125, 'name': 'Earth'}
    True
    >>> d = combine_lists(['name', 'mass', 'radius'], [3.1415, 'Test', 'value'])
    >>> d == {'mass': 'Test', 'radius': 'value', 'name': 3.1415}
    True
    """
    return dict(zip(keys, values))

def parse_string_value(string_value):
    """
    >>> parse_string_value("Hallo!")
    'Hallo!'
    >>> parse_string_value("1.234")
    1.234
    >>> parse_string_value("1e10")
    10000000000.0
    >>> parse_string_value("123E123")
    1.23e+125
    >>> parse_string_value("11.123e12")
    11123000000000.0
    >>> parse_string_value("11.123e124")
    1.1123e+125
    >>> parse_string_value("999123123.23123123")
    999123123.2312312
    >>> parse_string_value("50003e2")
    5000300.0
    >>> parse_string_value("50003e-123")
    5.0003e-119
    >>> parse_string_value("50003E-133")
    5.0003e-129
    """
    try:
        return float(string_value)
    except ValueError: # if not number
        return string_value

def dict_to_body(body_dict) -> Body:
    """
    >>> a = Body('Earth', 123, 456, (7, 8, 9), (10, 11, 12))
    >>> b = dict_to_body({
    ...     'name': 'Earth',
    ...     'mass': 123,
    ...     'radius': 456,
    ...     'position.x': 7,
    ...     'position.y': 8,
    ...     'position.z': 9,
    ...     'velocity.x': 10,
    ...     'velocity.y': 11,
    ...     'velocity.z': 12
    ... })
    >>> a.name == b.name
    True
    >>> a.mass == b.mass
    True
    >>> a.radius == b.radius
    True
    >>> a.position == b.position
    array([[ True],
           [ True],
           [ True]], dtype=bool)
    >>> a.velocity == b.velocity
    array([[ True],
           [ True],
           [ True]], dtype=bool)
    """
    return Body(
        body_dict['name'],
        body_dict['mass'],
        body_dict['radius'],
        (body_dict['position.x'], body_dict['position.y'], body_dict['position.z']),
        (body_dict['velocity.x'], body_dict['velocity.y'], body_dict['velocity.z'])
    )

class CSVStartValueInputProvider(FileInputProvider):
    def get_bodies(self) -> [Body]:
        """ Function get_bodies. Returns a generator.

        To use: use list to convert the generator to a list.

        @TODO: Write doctest """
        columns = None

        for line in open(self.get_filepath()):
            line = [parse_string_value(v.strip()) for v in line.split(',')]

            if columns is None:
                columns = line
            else:
                yield dict_to_body(combine_lists(columns, line))
