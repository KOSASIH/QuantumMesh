import unittest
from circuit import Circuit, Qubit, HGate, CNOTGate

class TestCircuit(unittest.TestCase):
    def test_circuit_initialization(self):
        circuit = Circuit(2)
        self.assertEqual(circuit.num_qubits, 2)
        self.assertEqual(len(circuit.qubits), 2)

    def test_circuit_add_gate(self):
        circuit = Circuit(2)
        gate = HGate(0)
        circuit.add_gate(gate)
        self.assertEqual(len(circuit.gates), 1)

    def test_circuit_apply_gates(self):
        circuit = Circuit(2)
        gate1 = HGate(0)
        gate2 = CNOTGate(0, 1)
        circuit.add_gate(gate1)
        circuit.add_gate(gate2)
        circuit.apply_gates()
        self.assertEqual(circuit.qubits[0].state, np.array([1/np.sqrt(2), 1/np.sqrt(2)]))
        self.assertEqual(circuit.qubits[1].state, np.array([1/np.sqrt(2), 0, 0, 1/np.sqrt(2)]))

if __name__ == '__main__':
    unittest.main()
