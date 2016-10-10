from __future__ import print_function

import pytest

from nbp.io.input_providers import InputProvider

def test_should_abstract_methods():
    class KokopelliInputProvider(InputProvider):
        pass

    class JogahInputProvider(InputProvider):
        def get_generator(self):
            return []

    class OkiInputProvider(InputProvider):
        @staticmethod
        def get_cli_arguments():
            return []

    class GaolInputProvider(InputProvider):
        def get_generator(self):
            return []

        @staticmethod
        def get_cli_arguments():
            return []

        def generator(self, receive):
            return []

    with pytest.raises(TypeError):
        KokopelliInputProvider({})

    with pytest.raises(TypeError):
        JogahInputProvider({})

    with pytest.raises(TypeError):
        OkiInputProvider({})

    assert GaolInputProvider({}).get_generator() == []
    assert GaolInputProvider({}).get_cli_arguments() == []
