import socket

# Common ports
ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS"
}

print("=" * 45)
print("        NETWORK PORT SCANNER")
print("=" * 45)

host = input("Enter IP Address or Hostname: ")

print("\nScanning...\n")

for port, service in ports.items():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    result = s.connect_ex((host, port))

    if result == 0:
        print(f"Port {port} ({service}) : OPEN")
    else:
        print(f"Port {port} ({service}) : CLOSED")

    s.close()

print("\nScan Completed.")