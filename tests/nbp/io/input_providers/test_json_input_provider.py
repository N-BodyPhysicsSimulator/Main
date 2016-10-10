from __future__ import print_function

import pytest
import tempfile

from nbp.io.input_providers import JSONInputProvider
from nbp.bodies import BodyState, Body
from nbp.helpers.validation import str_is_existing_file


def test_json_input_provider():
    json_content = """{"bodies": [{"mass": 123.0, "radius": 100.0, "position": {"y": 1521.0, "z": 10.0, "x": 0.0}, "name": "earth", "velocity": {"y": 0.0, "z": 320.5, "x": 292.0}}, {"mass": 999.0, "radius": 100.0, "position": {"y": 1521.0, "z": 132.0, "x": 2929000.0}, "name": "moon", "velocity": {"y": -57381.0, "z": 3200.0, "x": 2929.0}}, {"mass": 1234.56, "radius": 200.0, "position": {"y": 15209.0, "z": 16400.0, "x": 58580.0}, "name": "sun", "velocity": {"y": -11476.0, "z": 320.0, "x": 29290.0}}, {"mass": 98765.0, "radius": 17574.0, "position": {"y": 29200.0, "z": 2929.0, "x": 15209.0}, "name": "star", "velocity": {"y": 3200.0, "z": 123.0, "x": -34428.0}}], "ticks": 0, "delta_time": 10.0, "time": 0.0}"""
    json_content += "\n" + json_content
    json_content += "\n" + json_content

    f = tempfile.NamedTemporaryFile(delete=False)
    filepath = f.name
    f.write(json_content.encode())
    f.close()

    f = open(filepath, 'r')

    assert str_is_existing_file(f.name) == f.name
    assert json_content == f.read()
    
    args = { "json_input_path": f.name }

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
        'delta_time': 10.0
    }

    json_gen = JSONInputProvider(args).get_generator()
    assert (next(json_gen)) == BodyState.from_dict(expected_state)
    assert (next(json_gen)) == BodyState.from_dict(expected_state)
    assert (next(json_gen)) == BodyState.from_dict(expected_state)

    f.close()
