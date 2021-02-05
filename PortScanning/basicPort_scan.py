## Port scanning tool for specific IP has open ports

import socket

ip = input("Please input IP address : ")
port_start = int(input("Please input start Port number : "))
port_end = int(input("Please input end port number : "))

for port in range (port_start,port_end):
    sc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sc.settimeout(.5)

    result = sc.connect_ex((ip,port))

    if result == 0:
        print("[*] Open Port : \t",e)
    sc.close()
