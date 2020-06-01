import socket
import os
sock_fd = None
conn_fd = None
sock_addr = None
sock = open("MySocket", '+b')
try:
	sock_fd = socket.fromfd(sock,socket.AF_UNIX, socket.SOCK_STREM,0)
except:
	print("Error to create socket")
sock_addr = "MySocket"


#os.unlink(sock_addr)
try:
	sock_fd.bind((sock_addr))
except:
	print("Error Bind")
try:
	sock_fd.listen(5)
	conn_fd = sock_fd.accept()
	while True:
		recv = conn_fd.recv()
		print("Received:", repr(recv))
		if repr(recv) == "exit":
			break
		conn_fd.sendall(recv)
except:
	print("Conection Closed")
	sock_fd.close()
finally:
	sock_fd.close()
	conn_fd.close()
