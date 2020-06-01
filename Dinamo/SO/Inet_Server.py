import socket
server_port = 9999
sock_fd = None
message = ""
recv = None
conn_fd = None
client_addr = None
try:
	sock_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)
except:
	print("Error Create Socket")

server_address = socket.gethostbyname("debian")
socket.inet_aton(server_address)

try:
	sock_fd.bind((server_address, server_port))
except:
	print("Error Bind")
	sock_fd.close()

try:
	sock_fd.listen(1)
	conn_fd, client_addr = sock_fd.accept()
	print("Connected by:", client_addr)
	while True:
		recv = conn_fd.recv(1024)
		if not recv:
			print("Connection Closed")
			break
		print("Received:", repr(recv))
		if repr(recv) == "exit":
			break
		conn_fd.sendall(recv)
except:
	print("Error to listen")
	sock_fd.close()
finally:
	sock_fd.close()
	conn_fd.close()
