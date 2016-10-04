from nbp.modifiers import Modifier

class ModifierBundle(object):
    """
    >>> from nbp.helpers.numpy import tuple_to_numpy
    >>> from nbp.bodies import Body
    >>> from nbp.bodies import BodyState
    >>> from nbp.modifiers import DeltaTimeModifier
    >>> import numpy as np

    >>> settings = ([1, 2, 3, 4], [100, 200, 300, 400])
    >>> velocity = tuple_to_numpy((0, 0, 0))
    >>> one = Body('body1', 1, 100, np.array([[0.], [0.], [0.]]), velocity)
    >>> two = Body('body2', 1, 100, np.array([[0.], [99.], [0.]]), velocity)

    >>> dtm = DeltaTimeModifier({ 'change_dt_settings': settings })
    >>> bs = BodyState([one, two], 0, 0, 10)
    >>> bs.delta_time
    10.0
    >>> bundle = ModifierBundle([ dtm ])
    >>> gen = bundle.get_generator(bs)
    >>> new = next(gen)
    >>> new.delta_time
    1
    """
    def __init__(self, modifiers=[]):
        self.__modifiers = modifiers
    
    def add_modifier(self, modifier: Modifier):
        self.__modifiers.append(modifier)
    
    def __modify(self, state):
        for modifier in self.__modifiers:
            state = modifier.modify(state)
            
        return state
    
    def get_generator(self, begin_state):
        state = begin_state
        
        while True:
            state = self.__modify(state)
            yield state
