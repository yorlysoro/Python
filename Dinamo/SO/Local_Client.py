import socket
sock_fd = None
recv = None
sock_addr = None
#sock = open("MySocket", 'wb')
sock = socket.fileno()
try:
	 sock_fd = socket.fromfd(sock,socket.AF_UNIX, socket.SOCK_STREM,0)
except:
	print("Error Create Socket")
	
sock_addr = "MySocket"
try:
	sock_fd.connect((sock_addr))
	while True:
		message = input("Client->")
		print("Sent: ", message)
		sock_fd.sendall(message.encode())
		if message == "exit":
			break
		recv = sock_fd.recv()
		print("Received from server:", repr(recv))
except ConnectionRefusedError as C:
	print(C)
	sock_fd.close()
finally:
	sock_fd.close()

