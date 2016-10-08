from __future__ import print_function

import pytest

from nbp.io.output_writers import OutputWriter

def test_should_abstract_methods():
    class FakeReceiver():
        recv = 123
        
    class DaganOutputWriter(OutputWriter):
        pass

    class HadidOutputWriter(OutputWriter):
        def handle(self, state, args):
            return state

    class MariOutputWriter(OutputWriter):
        @staticmethod
        def get_cli_arguments():
            return []

    class MotOutputWriter(OutputWriter):
        def handle(self, state, args):
            return (state, args)

        @staticmethod
        def get_cli_arguments():
            return []

    with pytest.raises(TypeError):
        DaganOutputWriter({})

    with pytest.raises(TypeError):
        HadidOutputWriter({})

    with pytest.raises(TypeError):
        MariOutputWriter({})

    assert MotOutputWriter(FakeReceiver, {}).handle("String", 123) == ("String", 123)
    assert MotOutputWriter(FakeReceiver, {}).get_cli_arguments() == []
