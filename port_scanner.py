#Name: Enoch Adeleke
import pyfiglet
import sys
import socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

# Check if the target argument is provided
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])  # Convert hostname to IPv4
else:
    print("Usage: python3 port_scanner.py <target>")
    sys.exit()

# Print scanning details
print("-" * 50)
print(f"Scanning Target: {target}")
print("Scanning started at: " + str(datetime.now()))
print("-" * 50)

try:
    # Scan ports 1 to 1024 (common ports)
    for port in range(1, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()

except KeyboardInterrupt:
    print("\n Exiting Program!")
    sys.exit()

except socket.gaierror:
    print("\n Hostname Could Not Be Resolved!")
    sys.exit()

except socket.error:
    print("\n Server not responding!")
    sys.exit()
