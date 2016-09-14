from nbp.modifiers import Modifier

class ModifierBundle(object):
    def __init__(self, modifiers=[]: [Modifier]):
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
