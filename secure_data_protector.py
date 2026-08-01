from cryptography.fernet import Fernet
import hashlib
import base64
from getpass import getpass

# Convert user secret key into a valid encryption key
def generate_key(secret):
    sha = hashlib.sha256(secret.encode()).digest()
    return base64.urlsafe_b64encode(sha)


# Encrypt Message
def encrypt_message():

    print("\n========== ENCRYPT MESSAGE ==========")

    message = input("Enter Message: ")

    secret = getpass("Create Secret Key: ")

    key = generate_key(secret)

    fernet = Fernet(key)

    encrypted = fernet.encrypt(message.encode())

    print("\n========== ENCRYPTED MESSAGE ==========")
    print(encrypted.decode())


# Decrypt Message
def decrypt_message():

    print("\n========== DECRYPT MESSAGE ==========")

    encrypted = input("Enter Encrypted Message: ")

    secret = getpass("Enter Secret Key: ")

    key = generate_key(secret)

    fernet = Fernet(key)

    try:
        decrypted = fernet.decrypt(encrypted.encode())

        print("\n========== DECRYPTED MESSAGE ==========")
        print(decrypted.decode())

    except:
        print("\n❌ Wrong Secret Key or Invalid Encrypted Message")


# Main Program
while True:

    print("\n========================================")
    print("      SECURE DATA PROTECTOR")
    print("========================================")
    print("1. Encrypt Message")
    print("2. Decrypt Message")
    print("3. Exit")

    choice = input("\nEnter Your Choice: ")

    if choice == "1":
        encrypt_message()

    elif choice == "2":
        decrypt_message()

    elif choice == "3":
        print("\nThank You!")
        break

    else:
        print("\nInvalid Choice! Please Try Again.")