import numpy as np

class Simulator:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.state = np.ones(2**num_qubits) / np.sqrt(2**num_qubits)

    def apply_gate(self, gate):
        matrix = gate.matrix(self.num_qubits)
        self.state = np.dot(matrix, self.state)

    def measure(self):
        outcome = np.random.choice(2, p=np.abs(self.state)**2)
        self.state = self.collapse_state(outcome)
        return outcome

    def collapse_state(self, outcome):
        new_state = np.zeros(2**self.num_qubits, dtype=np.complex128)
        new_state[outcome] = 1
        return new_state
