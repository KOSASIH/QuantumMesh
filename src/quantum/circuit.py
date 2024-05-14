import numpy as np
from gates import Gate

class Circuit:
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.qubits = [Qubit(i) for i in range(num_qubits)]
        self.gates = []

    def add_gate(self, gate):
        self.gates.append(gate)

    def apply_gates(self):
        for gate in self.gates:
            gate.apply(self.qubits)

    def measure(self):
        return [qubit.measure() for qubit in self.qubits]

class Qubit:
    def __init__(self, index):
        self.index = index
        self.state = np.array([1, 0])

    def apply_gate(self, gate):
        self.state = gate.apply(self.state)

    def measure(self):
        probability = np.abs(self.state[0])**2
        outcome = np.random.choice([0, 1], p=[probability, 1-probability])
        if outcome == 0:
            self.state = np.array([1, 0])
        else:
            self.state = np.array([0, 1])
        return outcome
