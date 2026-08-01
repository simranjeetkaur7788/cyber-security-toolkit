print("================================")
print("   Cyber Security Toolkit")
print("================================")

print("1. Password Manager")
print("2. File Integrity Checker")
print("3. Network Scanner")
print("4. OSINT Toolkit")
print("5. Secure Data Protector")

choice = input("Enter your choice: ")

if choice == "1":
    import password_manager

elif choice == "2":
    import file_integrity_checker

elif choice == "3":
    import network_scanner


elif choice == "4":
    import osint_toolkit

elif choice == "5":
    import secure_data_protector

else:
    print("Invalid choice")