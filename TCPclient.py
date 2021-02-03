import socket
s_ip="127.0.0.1"
s_port=12345

c_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c_sock.connect((s_ip,s_port))

print("Receve data from server:",c_sock.recv(1024))
message="Hello, TCP Server"
c_sock.sendall(message.encode('utf-8'))

c_sock.close()
