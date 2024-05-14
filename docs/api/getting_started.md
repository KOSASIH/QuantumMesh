# Getting Started with Quantum Computing Library

Welcome to the Quantum Computing Library! This library provides a simple and intuitive interface for creating and simulating quantum circuits.

# Installation

To install the library, simply run:

```
1. pip install qc-library
```

# Getting Started

To get started, let's create a simple quantum circuit with one qubit and one Hadamard gate:

```python

1. from circuit import Circuit, HGate
2. 
3. # Create a new circuit with one qubit
4. circuit = Circuit(1)
5. 
6. # Add a Hadamard gate to the circuit
7. circuit.add_gate(HGate(0))
8. 
9. # Apply the gates to the circuit
10. circuit.apply_gates()
11. 
12. # Print the final state of the qubit
13. print(circuit.qubits[0].state)

```

This will output:

```csharp

[0.70710678+0.j 0.70710678+0.j]
```

This means that the final state of the qubit is in a superposition of both 0 and 1 with equal probability.

# Simulating a Quantum Circuit

To simulate a quantum circuit, we can use the Simulator class:

```python

from simulator import Simulator
```

# Create a new simulator with one qubit

sim = Simulator(1)

# Add a Hadamard gate to the simulator

sim.apply_gate(HGate(0))

# Measure the qubit

outcome = sim.measure()

# Print the outcome

print(outcome)

This will output either 0 or 1, depending on the random measurement outcome.

# Testing Your Quantum Circuit

To test your quantum circuit, you can use the unittest module in Python:

```python

1. import unittest
2. from circuit import Circuit, HGate
3. 
4. class TestCircuit(unittest.TestCase):
5.    def test_apply_gate(self):
6.        circuit = Circuit(1)
7.        gate = HGate(0)
8.        circuit.add_gate(gate)
9.        circuit.apply_gates()
10.        self.assertTrue(np.allclose(circuit.qubits[0].state, np.array([0.70710678+0.j, 0.70710678+0.j])))
11. 
12. if __name__ == '__main__':
13.    unittest.main()
14. 
```
This will test that the Hadamard gate is applied correctly to the state vector.

# Conclusion

That's it! With these basic building blocks, you can start creating and simulating more complex quantum circuits. Happy coding!
