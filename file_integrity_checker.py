import hashlib
import os
# Generate SHA-256 Hash
def generate_hash(file_path):

    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:

            while True:
                data = file.read(4096)

                if not data:
                    break

                sha256.update(data)

        return sha256.hexdigest()

    except FileNotFoundError:
        return None

# Save Hash

def save_hash(file_name, file_hash):

    with open("hashes.txt", "a") as file:

        file.write(file_name + "|" + file_hash + "\n")

# Verify File
def verify_file(file_path):

    new_hash = generate_hash(file_path)

    if new_hash is None:
        print("File not found.")
        return

    file_name = os.path.basename(file_path)

    try:

        with open("hashes.txt", "r") as file:

            for line in file:

                saved_name, saved_hash = line.strip().split("|")

                if saved_name == file_name:

                    if saved_hash == new_hash:
                        print("\n✅ File is Safe")
                    else:
                        print("\n⚠ Warning! File has been Modified")

                    return

        print("No saved hash found.")

    except FileNotFoundError:

        print("No hash database found.")

# Main Menu
while True:

    print("\n========== FILE INTEGRITY CHECKER ==========")
    print("1. Generate and Save Hash")
    print("2. Verify File")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        path = input("Enter File Path: ")

        file_hash = generate_hash(path)

        if file_hash:

            print("\nSHA-256 Hash:")
            print(file_hash)

            save_hash(os.path.basename(path), file_hash)

            print("\nHash Saved Successfully.")

        else:

            print("File Not Found.")

    elif choice == "2":

        path = input("Enter File Path: ")

        verify_file(path)

    elif choice == "3":

        print("Thank You!")

        break

    else:

        print("Invalid Choice.")