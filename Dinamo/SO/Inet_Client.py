import socket

sock_fd = None

messagge = ""
recv = ""
try:
	sock_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)
except:
	print("Error Create Socket")
	
server_port = 9999
server_address = socket.gethostbyname("debian")
socket.inet_aton(server_address)
try:
	sock_fd.connect((server_address, server_port))
	while True:
		message = input("client->")
		print("Sent:", message)
		sock_fd.sendall(message.encode())
		if message == "exit":
			break
		recv = sock_fd.recv(1024)
		print("Received:", repr(recv))
except ConnectionRefusedError as C:
	print(C)
	sock_fd.close()
finally:
	sock_fd.close()



