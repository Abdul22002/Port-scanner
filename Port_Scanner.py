import socket
from concurrent.futures import ThreadPoolExecutor

# Function to scan a single port
def scan_port(host, port):
    try:
        # Create a socket object and set a timeout
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((host, port))
            if result == 0:
                print(f"Port {port} is open")
            else:
                print(f"Port {port} is closed")
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

# Main function to scan a range of ports
def scan_ports(host, start_port, end_port, max_threads=50):
    with ThreadPoolExecutor(max_threads) as executor:
        for port in range(start_port, end_port + 1):
            executor.submit(scan_port, host, port)

# Get user input for target host and port range
if __name__ == "__main__":
    target_host = input("Enter the target host (e.g., 192.168.1.1): ")
    start_port = int(input("Enter the starting port number: "))
    end_port = int(input("Enter the ending port number: "))
    
    print(f"Scanning ports {start_port} to {end_port} on {target_host}...")
    scan_ports(target_host, start_port, end_port)
