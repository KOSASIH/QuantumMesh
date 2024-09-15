import numpy as np
import random

# BB84 protocol for quantum key distribution
class BB84:
    def __init__(self, num_bits):
        self.num_bits = num_bits

    def generate_key(self):
        # Generate random key
        key = np.random.randint(0, 2, size=self.num_bits)
        return key

    def encode_key(self, key):
        # Encode key using BB84 protocol
        encoded_key = np.zeros((self.num_bits, 2), dtype=int)
        for i in range(self.num_bits):
            if key[i] == 0:
                encoded_key[i] = [0, random.randint(0, 1)]
            else:
                encoded_key[i] = [1, random.randint(0, 1)]
        return encoded_key

    def decode_key(self, encoded_key):
        # Decode key using BB84 protocol
        key = np.zeros(self.num_bits, dtype=int)
        for i in range(self.num_bits):
            if encoded_key[i, 0] == 0:
                key[i] = 0
            else:
                key[i] = 1
        return key

    def measure_key(self, encoded_key):
        # Measure key using BB84 protocol
        measured_key = np.zeros(self.num_bits, dtype=int)
        for i in range(self.num_bits):
            if encoded_key[i, 1] == 0:
                measured_key[i] = 0
            else:
                measured_key[i] = 1
        return measured_key

# Example usage
if __name__ == '__main__':
    bb84 = BB84(num_bits=1024)
    key = bb84.generate_key()
    encoded_key = bb84.encode_key(key)
    measured_key = bb84.measure_key(encoded_key)
    decoded_key = bb84.decode_key(encoded_key)
    print(key)
    print(measured_key)
    print(decoded_key)
