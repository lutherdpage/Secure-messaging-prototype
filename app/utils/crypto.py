from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.fernet import Fernet

def generate_rsa_keys():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key

def encrypt_symmetric_key(symmetric_key: bytes, public_key):
    encrypted_key = public_key.encrypt(
        symmetric_key,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )
    return encrypted_key

def decrypt_symmetric_key(encrypted_key: bytes, private_key):
    return private_key.decrypt(
        encrypted_key,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )

def encrypt_message(message: str, key: bytes):
    f = Fernet(key)
    return f.encrypt(message.encode())

def decrypt_message(token: bytes, key: bytes):
    f = Fernet(key)
    return f.decrypt(token).decode()
