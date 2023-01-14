import socket
from threading import Thread

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    result = sock.connect_ex((ip, port))
    if result == 0:
        print(f'Port {port} is open')
    else:
        pass

def main():
    ip_address = '192.168.0.169'
    start_port = 1
    end_port = 1024
    for port in range(start_port, end_port):
        t = Thread(target=scan_port, args=(ip_address, port))
        t.start()

if __name__ == "__main__":
    main()
