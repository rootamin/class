# encypt and decrypt
import base64, os

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
        file_name = input("Enter your file name: ")

        with open(file_name, "r") as file_object:
            data = file_object.read()
        
        enc_message = data
        enc_password = input("Enter your password: ")

        with open("encrypted.txt", "w") as enc_object:
            enc_content = str(encyption(enc_message, enc_password))
            enc_data = file_object.write(enc_content)

    
    elif operation == "d":
        dec_message = "s"
        dec_password = input("Enter the password: ")

        print(decryption(dec_message, dec_password))

    else:
        print("Invalid Operation")
        