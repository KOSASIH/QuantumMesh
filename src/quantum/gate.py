class Gate:
    def apply(self, state):
        raise NotImplementedError

class HadamardGate(Gate):
    def apply(self, state):
        return np.array([1/np.sqrt(2), 1/np.sqrt(2), 1/np.sqrt(2), -1/np.sqrt(2)]).dot(state)

class CNOTGate(Gate):
    def apply(self, state):
        control_index, target_index = self.control, self.target
        control_state = state[control_index]
        target_state = state[target_index]
        if control_state == 1:
            target_state = 1 - target_state
        return state.dot([1, 0, 0, 0, 0, 1, 1, 0])
