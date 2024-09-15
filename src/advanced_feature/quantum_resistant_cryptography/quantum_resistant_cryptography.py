import numpy as np
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import x25519
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

# Lattice-based cryptography using NTRU
class NTRUCryptography:
    def __init__(self, n, p, q):
        self.n = n
        self.p = p
        self.q = q

    def keygen(self):
        # Generate public and private keys
        public_key = np.random.randint(0, self.q, size=self.n)
        private_key = np.random.randint(0, self.p, size=self.n)
        return public_key, private_key

    def encrypt(self, message, public_key):
        # Encrypt message using public key
        ciphertext = np.mod(message + public_key, self.q)
        return ciphertext

    def decrypt(self, ciphertext, private_key):
        # Decrypt ciphertext using private key
        message = np.mod(ciphertext - private_key, self.p)
        return message

# Code-based cryptography using McEliece
class McElieceCryptography:
    def __init__(self, n, k, t):
        self.n = n
        self.k = k
        self.t = t

    def keygen(self):
        # Generate public and private keys
        public_key = np.random.randint(0, 2, size=(self.n, self.k))
        private_key = np.random.randint(0, 2, size=(self.k, self.n))
        return public_key, private_key

    def encrypt(self, message, public_key):
        # Encrypt message using public key
        ciphertext = np.mod(message @ public_key, 2)
        return ciphertext

    def decrypt(self, ciphertext, private_key):
        # Decrypt ciphertext using private key
        message = np.mod(ciphertext @ private_key, 2)
        return message

# Example usage
if __name__ == '__main__':
    # Lattice-based cryptography using NTRU
    ntru = NTRUCryptography(n=256, p=3, q=257)
    public_key, private_key = ntru.keygen()
    message = np.random.randint(0, 256, size=256)
    ciphertext = ntru.encrypt(message, public_key)
    decrypted_message = ntru.decrypt(ciphertext, private_key)
    print(decrypted_message)

    # Code-based cryptography using McEliece
    mceliece = McElieceCryptography(n=256, k=128, t=32)
    public_key, private_key = mceliece.keygen()
    message = np.random.randint(0, 2, size=128)
    ciphertext = mceliece.encrypt(message, public_key)
    decrypted_message = mceliece.decrypt(ciphertext, private_key)
    print(decrypted_message)
