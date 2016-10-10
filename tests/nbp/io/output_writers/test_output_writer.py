from __future__ import print_function

import pytest

from nbp.io.output_writers import OutputWriter

def test_should_abstract_methods():
    class DaganOutputWriter(OutputWriter):
        pass

    class HadidOutputWriter(OutputWriter):
        def handle(self, state):
            return state

    class MariOutputWriter(OutputWriter):
        @staticmethod
        def get_cli_arguments():
            return []

    class MotOutputWriter(OutputWriter):
        def handle(self, state):
            return state

        @staticmethod
        def get_cli_arguments():
            return []

    with pytest.raises(TypeError):
        DaganOutputWriter({})

    with pytest.raises(TypeError):
        HadidOutputWriter({})

    with pytest.raises(TypeError):
        MariOutputWriter({})

    assert MotOutputWriter({}).handle("String") == "String"
    assert MotOutputWriter({}).get_cli_arguments() == []
