import socket
import time
import datetime
import threading
import os
import random
from Response import *

def download_RFC(RFC_name,conn):
    RFC_name = conn.recv(1024)
    nameoffile = str(RFC_name.decode('utf-8'))
    if os.path.isfile(nameoffile):
        x = (os.path.getsize(nameoffile))
        y = str(x)
        conn.send(bytes(y,"utf-8"))
        with open(RFC_name, 'rb') as file:
            RFC_data = file.read(1024)
            conn.send(RFC_data)
            while RFC_data != '':
                RFC_data = file.read(1024)
                conn.send(RFC_data)
        print("RFC file transmission completed!!!")
        s.close()
    else:
        #conn.send(bytes("RFC file requested is not present!!!","utf-8"))
        s.close()


port = input(str("Enter the port number to use for TCP connection:"))  # port number at which connection will be established
hostname = socket.gethostname()
num_connection = 6  # number of supported connections

# Creating a server socket

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # to communicate using IPv4 address
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # to reuse the address once connection is closed
    s.bind((hostname, int(port)))  # to bind to a specific port number
    s.listen(num_connection)  # to indicate server is waiting for client connection
    print(hostname)
    print("Waiting for incoming connection:")
    while True:
        conn,addr = s.accept()
        print("Connected to peer with address: " + str(addr))
        thread = threading.Thread(target=download_RFC, args=("file_thread",conn))
        thread.start()

except socket.error:
    print("The requested file is not present with me!!!")
    s.close()


peer_list = {}  # dictionary to maintain the list of peers
list_of_rfcs = []  # dictionary to maintain the list of RFCs
#peer_no
peers_rfcs = []  # dictionary of dictionary to map peers to RFCs


# Function to add peer information to peer list

def add_peer_details(socketconn, address, port_num):
    peer_list.update({address: port_num})
    print(peer_list)


def cookie_generator():  # function to generate a new cookie
    flag = 1
    while True:
        random_cookie = random.randrange(start=1000, stop=999999, step=1)
        for host in peer_no:
            if random_cookie == int(host.cookie):
                flag = 0
        if flag:
            break
    return random_cookie

def peerlistupdate():
    f = open("Peer_List.txt","w+")
    f.write = ("\n Hostname \t Cookie \t Active_State \t TTL \t Port No. \t Active times \t Most Recent registration time \n")
    f.close()


# Function to create a list of peers and map it with IP address and used port number
# def create_peer_list(mapped_peer_list, address, port_no):
#    peer_list = [address, str(port_no)]
#    mapper = ['hostname', 'Port No.']

#    dictionary = dict(zip(address, port_no))
#    mapped_peer_list.insert(0, dictionary)
#    return mapped_peer_list, mapper


# Function to create the list of RFCs


# Function to create mapping of RFCs to peers


# Function to create a separate thread for each connecting peer. This is to implement simultaneous access.
# def threaded_peer():



