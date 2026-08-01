print("Hello, Cyber Security Toolkit!")
import hashlib
import random
import string
import re

# Password Strength Checker
def check_strength(password):
    if len(password) < 8:
        return "Weak"

    if (re.search("[A-Z]", password) and
        re.search("[a-z]", password) and
        re.search("[0-9]", password) and
        re.search("[@#$%^&*!]", password)):
        return "Strong"

    return "Medium"


# Password Generator
def generate_password():
    characters = string.ascii_letters + string.digits + "@#$%^&*!"
    password = "".join(random.choice(characters) for i in range(12))
    return password


# Hash Password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# Verify Password
def verify_password():
    password = input("Enter Password: ")
    saved_hash = input("Enter Saved Hash: ")

    if hash_password(password) == saved_hash:
        print(" Password Verified Successfully")
    else:
        print(" Password Verification Failed")


# Main Program
while True:

    print("\n========== PASSWORD SECURITY ==========")
    print("1. Check Password Strength")
    print("2. Generate Password")
    print("3. Hash Password")
    print("4. Verify Password")
    print("5. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        password = input("Enter Password: ")
        print("Password Strength:", check_strength(password))

    elif choice == "2":
        print("Generated Password:", generate_password())

    elif choice == "3":
        password = input("Enter Password: ")
        print("SHA-256 Hash:")
        print(hash_password(password))

    elif choice == "4":
        verify_password()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")