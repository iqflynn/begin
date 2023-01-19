import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = input("Target IP: ")
port = int(input("Target Port: "))

def portscanner(port):
    if s.connect_ex((host, port)):
        print("The port is closed")
    else:
        print("The port is open")
        
portscanner(port)
