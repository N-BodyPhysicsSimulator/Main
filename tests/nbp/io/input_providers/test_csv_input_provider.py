from __future__ import print_function

import pytest
import tempfile

from nbp.io.input_providers import CSVInputProvider
from nbp.bodies import BodyState, Body
from nbp.helpers.validation import str_is_existing_file


def test_csv_input_provider():
    csv_content = """name,mass,radius,pos.x,pos.y,pos.z,vel.x,vel.y,vel.z
earth,123,100,0,1521,10,292,0,320.5
moon,999,100,2929000,1521,132,2929,-57381,3200
sun,1234.56,200,58580,15209,16400,29290,-11476,320
star,98765,17574,15209,29200,2929,-34428,3200,123"""

    f = tempfile.NamedTemporaryFile(delete=False)
    filepath = f.name
    f.write(csv_content.encode())
    f.close()

    f = open(filepath, 'r')

    assert str_is_existing_file(f.name) == f.name
    assert csv_content == f.read()
    
    args = {
        "csv_input_path": f.name,
        "separator": ',',
        "delta_time": 10.0
    }

    expected_state = {
        'bodies': [
            {
                'name': 'earth',
                'mass': 123.0,
                'radius': 100.0,
                'position': { 'x': 0.0, 'y': 1521.0, 'z': 10.0 },
                'velocity': { 'x': 292.0, 'y': 0.0, 'z': 320.5 }
            },
            {
                'name': 'moon',
                'mass': 999.0,
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
                'mass': 98765.0,
                'radius': 17574.0,
                'position': { 'x': 15209.0, 'y': 29200.0, 'z': 2929.0 },
                'velocity': { 'x': -34428.0, 'y': 3200.0, 'z': 123.0 },
            }
        ],
        'ticks': 0,
        'time': 0.0,
        'delta_time': args.get('delta_time')
    }

    csv_gen = CSVInputProvider(args).get_generator()
    assert (next(csv_gen)) == BodyState.from_dict(expected_state)

    f.close()
