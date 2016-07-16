from nbp.io.input_providers import FileInputProvider
from nbp.modifiers import CalculationModifier
from nbp.bodies import BodyState
from nbp.bodies import Body

class DummyFileInputProvider(FileInputProvider):
    def get_body_states(self) -> BodyState:
        sun = Body.from_tuple_parameters('Sun', 1989000000000000000000000000000, 100, (0, 0, 0), (0, 0, 0))
        earth = Body.from_tuple_parameters('earth', 5972000000000000000000000, 100, (0, 152100000000, 1000), (29290, 0, 32))
        moon = Body.from_tuple_parameters('moon', 73460000000000000000000, 100, (405500000, 152100000000, 175000), (29290, 964, 0))
        jupiter = Body.from_tuple_parameters('jupiter', 1900000000000000000000000000, 100, (816620000000, 0, -1000), (40, 12440, 1))
        saturn = Body.from_tuple_parameters('saturn', 568000000000000000000000000, 100, (0, 1352550000000, 0), (0, 10180, 0))
        neptune = Body.from_tuple_parameters('neptune', 102413000000000000000000000, 100, (0, -4444450000000, 500000), (-5370, 0, 0))
        bodies = [sun, earth, moon, jupiter, saturn, neptune]

        state = BodyState(bodies, 0, 0, (24 * 60 * 60 * ((365.25) / 8) ))

        while True:
            state = CalculationModifier.modificate(state)

            yield state
              
