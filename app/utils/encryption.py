from cryptography.fernet import Fernet

# Generate a key (run once, save to file)
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as f:
        f.write(key)
    return key

# Load key from file
def load_key():
    with open("secret.key", "rb") as f:
        key = f.read()
    return key

# Encrypt message
def encrypt_message(message: str) -> bytes:
    cipher = Fernet(load_key())
    return cipher.encrypt(message.encode())

# Decrypt message
def decrypt_message(token: bytes) -> str:
    cipher = Fernet(load_key())
    return cipher.decrypt(token).decode()
