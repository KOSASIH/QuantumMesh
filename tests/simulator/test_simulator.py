import unittest
from simulator import Simulator

class TestSimulator(unittest.TestCase):
    def test_initialization(self):
        sim = Simulator(2)
        self.assertEqual(sim.num_qubits, 2)
        self.assertEqual(len(sim.state), 4)

    def test_apply_gate(self):
        sim = Simulator(2)
        gate = HGate(0)
        sim.apply_gate(gate)
        self.assertTrue(np.allclose(sim.state, np.array([1/np.sqrt(2), 1/np.sqrt(2), 1/np.sqrt(2), -1/np.sqrt(2)])))

    def test_measure(self):
        sim = Simulator(2)
        outcome = sim.measure()
        self.assertTrue(isinstance(outcome, int))
        self.assertTrue(0 <= outcome < 2**sim.num_qubits)

if __name__ == '__main__':
    unittest.main()
