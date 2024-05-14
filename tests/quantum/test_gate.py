import unittest
from gates import Gate, HadamardGate, CNOTGate

class TestGate(unittest.TestCase):
    def test_hadamard_gate(self):
        gate = HadamardGate()
        matrix = gate.matrix(1)
        self.assertTrue(np.allclose(matrix, np.array([[1/np.sqrt(2), 1/np.sqrt(2)],
                                                     [1/np.sqrt(2), -1/np.sqrt(2)]])))

    def test_cnot_gate(self):
        gate = CNOTGate()
        matrix = gate.matrix(2)
        self.assertTrue(np.allclose(matrix, np.array([[1, 0, 0, 0],
                                                     [0, 1, 0, 0],
                                                     [0, 0, 0, 1],
                                                     [0, 0, 1, 0]])))

if __name__ == '__main__':
    unittest.main()
