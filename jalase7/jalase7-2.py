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


    if type(message) == type(b's'):
        message = message
    else:
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

    if type(message) == type(b's'):
        message = message
    else:
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

        absolute_path = os.getcwd() + "/"

        if os.path.exists(absolute_path + file_name):
            pass
        else:
            print("File does not exist.")
            continue

        with open(absolute_path + file_name, "rb") as file_object:
            data = file_object.read()
        
        enc_message = data
        enc_password = input("Enter your password: ")

        with open(absolute_path + "encrypted.txt", "w") as enc_object:
            enc_content = str(encyption(enc_message, enc_password))
            enc_filtered = enc_content.split("'")
            enc_data = enc_object.write(enc_filtered[1])

    
    elif operation == "d":
        file_name = input("Enter your file name: ")

        absolute_path = os.getcwd() + "/"

        if os.path.exists(absolute_path + file_name):
            pass
        else:
            print("File does not exist.")
            continue

        with open(absolute_path + file_name, "r") as file_object:
            data = file_object.read()
        
        enc_message = data
        enc_password = input("Enter your password: ")

        with open(absolute_path + "raw.txt", "wb") as enc_object:
            enc_content = decryption(enc_message, enc_password)

            if type(enc_content) == type(b"a"):
                enc_data = enc_object.write(enc_content)
            else:
                enc_filtered = enc_content.split("'")
                
                enc_filtered_2 = enc_filtered[1].split("\\n")
                
                for i in enc_filtered_2:
                    enc_data = enc_object.write(i + "\n")


    else:
        print("Invalid Operation")
        