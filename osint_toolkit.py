import socket

print("=" * 50)
print("      CYBER SECURITY TOOLKIT")
print("          OSINT TOOLKIT")
print("=" * 50)

domain = input("Enter Domain Name (Example: google.com): ")

try:
    # Domain to IP
    ip = socket.gethostbyname(domain)

    print("\n========== RESULTS ==========")
    print("Domain Name      :", domain)
    print("IP Address       :", ip)

    # Website Reachability
    print("Website Status   : Reachable")

    # Hostname
    hostname = socket.getfqdn(domain)
    print("Host Name        :", hostname)

    # Reverse DNS Lookup
    try:
        reverse = socket.gethostbyaddr(ip)
        print("Reverse DNS      :", reverse[0])
    except:
        print("Reverse DNS      : Not Available")

    print("\nOSINT Scan Completed Successfully.")

except socket.gaierror:
    print("\nInvalid Domain Name or Website Not Reachable.")