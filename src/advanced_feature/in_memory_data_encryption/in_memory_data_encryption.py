import numpy as np
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

class InMemoryDataEncryption:
    def __init__(self, key):
        self.key = key
        self.backend = default_backend()

    def encrypt_data(self, data):
        # Encrypt data using AES-256-CBC
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(np.random.bytes(16)), backend=self.backend)
        encryptor = cipher.encryptor()
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(data) + padder.finalize()
        encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        # Decrypt data using AES-256-CBC
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(encrypted_data[:16]), backend=self.backend)
        decryptor = cipher.decryptor()
        decrypted_padded_data = decryptor.update(encrypted_data[16:]) + decryptor.finalize()
        unpadder = padding.PKCS7(128).unpadder()
        decrypted_data = unpadder.update(decrypted_padded_data) + unpadder.finalize()
        return decrypted_data

# Example usage
if __name__ == '__main__':
    key = np.random.bytes(32)  # 256-bit key
    in_memory_data_encryption = InMemoryDataEncryption(key)
    data = b'Hello, World!'
    encrypted_data = in_memory_data_encryption.encrypt_data(data)
    decrypted_data = in_memory_data_encryption.decrypt_data(encrypted_data)
    print(decrypted_data.decode())  # Output: Hello, World!
