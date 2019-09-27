import socket
import sys

# creating a server socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       # to communicate using IPv4 address
host = input(str("Enter the hostname of the server to connect to:"))
port = 33333
s.connect((host, port))

filename = input("Enter the RFC to download:")
s.send(bytes(filename, 'utf-8'))
RFC_file_size = s.recv(1024)
x = RFC_file_size.decode('utf-8')
if x != '':
    file = open(filename, 'wb')
    received_data = s.recv(1024)
    received_size = len(received_data)
    file.write(received_data)
    while received_size < int(x):
        received_data = s.recv(1024)
        received_size += len(received_data)
        file.write(received_data)
    file.close()
    print("File has been received successfully")
else:
    print("Requested RFC was not found!!!")
