from types import GeneratorType

from nbp.bodies import Body
from nbp.bodies import BodyState
from nbp.decorators import entity
from nbp.io.input_providers import InputProvider


@entity("dummy")
class DummyInputProvider(InputProvider):
    @staticmethod
    def get_cli_arguments() -> list:
        return []

    def get_body_states(self) -> GeneratorType:
        """
        :rtype: GeneratorType
        """
        sun = Body.from_tuple_parameters('Sun', 1989000000000000000000000000000, 100, (0, 0, 0), (0, 0, 0))
        earth = Body.from_tuple_parameters('earth', 5972000000000000000000000, 100, (0, 152100000000, 1000),
                                           (29290, 0, 32))
        moon = Body.from_tuple_parameters('moon', 73460000000000000000000, 100, (405500000, 152100000000, 175000),
                                          (29290, 964, 0))
        jupiter = Body.from_tuple_parameters('jupiter', 1900000000000000000000000000, 100, (816620000000, 0, -1000),
                                             (40, 12440, 1))
        saturn = Body.from_tuple_parameters('saturn', 568000000000000000000000000, 100, (0, 1352550000000, 0),
                                            (0, 10180, 0))
        neptune = Body.from_tuple_parameters('neptune', 102413000000000000000000000, 100, (0, -4444450000000, 500000),
                                             (-5370, 0, 0))
        bodies = [sun, earth, moon, jupiter, saturn, neptune]

        yield BodyState(bodies, 0, 0, self.args.get('delta_time'))
