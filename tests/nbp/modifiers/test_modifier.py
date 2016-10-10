from __future__ import print_function

import pytest

from nbp.modifiers import Modifier

def test_should_implement_abstract_methods():
    class YahwehModifier(Modifier):
        pass

    class AbrahamModifier(Modifier):
        def modify(self, state):
            return state

    class BaalModifier(Modifier):
        @staticmethod
        def get_cli_arguments():
            return []

    class ElohimModifier(Modifier):
        def modify(self, state):
            return state

        @staticmethod
        def get_cli_arguments():
            return []

    with pytest.raises(TypeError):
        BaalModifier({})

    with pytest.raises(TypeError):
        AbrahamModifier({})

    with pytest.raises(TypeError):
        YahwehModifier({})

    assert ElohimModifier({}).modify(True) == True
    assert ElohimModifier({}).get_cli_arguments() == []
