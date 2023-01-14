import socket

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    result = sock.connect_ex((ip, port))
    if result == 0:
        print(f'Port {port} is open')

def main():
    ip_address = 'example.com'
    start_port = 1
    end_port = 1024
    for port in range(start_port, end_port):
        scan_port(ip_address, port)

if __name__ == "__main__":
    main()
