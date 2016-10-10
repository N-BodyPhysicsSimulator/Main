from __future__ import print_function

import pytest
import tempfile

from nbp.io.input_providers import JSONInputProvider
from nbp.io.output_writers import JSONOutputWriter
from nbp.bodies import BodyState, Body
from nbp.helpers.validation import dirname_is_existing_dir
from nbp.helpers.validation import str_is_existing_file


def test_json_input_provider_output_writer():
    f = tempfile.NamedTemporaryFile(delete=False)
    filepath = f.name
    f.write(b"")
    f.close()

    assert dirname_is_existing_dir(f.name) == f.name
    assert str_is_existing_file(f.name) == f.name
    
    args = {
        "json_output_path": filepath,
        "json_input_path": filepath
    }

    get_simple_generator = lambda: (BodyState.from_dict({
        'bodies': [
            {
                'name': 'earth',
                'mass': (i + 1) * 123.0,
                'radius': i + 100.0,
                'position': { 'x': 0.0, 'y': 1521.0, 'z': 10.0 },
                'velocity': { 'x': 292.0, 'y': 0.0, 'z': 320.5 }
            },
            {
                'name': 'moon',
                'mass': 999.0 / (i + 3),
                'radius': 100.0,
                'position': { 'x': 2929000.0, 'y': 1521.0, 'z': 132.0 },
                'velocity': { 'x': 2929.0, 'y': -57381.0, 'z': 3200.0 }
            },
            {
                'name': 'sun',
                'mass': 1234.56,
                'radius': 200.0,
                'position': { 'x': 58580.0, 'y': 15209.0, 'z': 16400.0 },
                'velocity': { 'x': 29290.0, 'y': -11476.0, 'z': 320.0 }
            },
            {
                'name': 'star',
                'mass': 98765.0 / (i + 36),
                'radius': 17574.0,
                'position': { 'x': 15209.0, 'y': 29200.0, 'z': 2929.0 },
                'velocity': { 'x': -34428.0, 'y': 3200.0, 'z': 123.0 },
            }
        ],
        'ticks': 0,
        'time': 0.0,
        'delta_time': 10.0
    }) for i in range(0, 3))

    output_generator = get_simple_generator()
    JSONOutputWriter(args).handle(output_generator)

    json_gen_in = JSONInputProvider(args).get_generator()
    json_gen_out = get_simple_generator()


    for i in range(0, 3):
        assert next(json_gen_in) == next(json_gen_out)

    f.close()
