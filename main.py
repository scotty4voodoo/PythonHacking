import socket

s_ip="127.0.0.1"
s_port=12345

s_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s_sock.bind((s_ip,s_port))
s_sock.listen(2)

(client,c_addr)=s_sock.accept()
print(c_addr, "is connected")

message="Thank you for connecting"
client.sendall(message.encode('utf-8'))
print("Received data from client:",client.recv(1024))

client.close()
s_sock.close()
