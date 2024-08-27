# encypt and decrypt
import base64

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC



def encyption(message, salt):
    salt = bytes(salt, 'utf8')

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
    )

    message = bytes(message, "utf8")
    password = b"Abcd123"

    key = base64.urlsafe_b64encode(kdf.derive(password))
    f = Fernet(key)

    encMessage = f.encrypt(message)

    return encMessage



def decryption(message, salt):
    salt = bytes(salt, 'utf8')

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
    )

    message = bytes(message, "utf8")
    password = b"Abcd123"

    key = base64.urlsafe_b64encode(kdf.derive(password))
    f = Fernet(key)

    decMessage = f.decrypt(message)

    return decMessage



# Main loop
while True:
    operation = input("Encrypt or Decrypt? (e/d): ")

    if operation == "e":
        enc_message = input("Enter your message: ")
        enc_password = input("Enter your password: ")

        print(encyption(enc_message, enc_password))

    
    elif operation == "d":
        dec_message = input("Enter the encrypted message: ")
        dec_password = input("Enter the password: ")

        print(decryption(dec_message, dec_password))

    else:
        print("Invalid Operation")
        