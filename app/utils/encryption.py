import hashlib


def encrypt(password):
    encrypt = hashlib.sha256()
    encrypt.update(password.encode())
    return encrypt.hexdigest()
