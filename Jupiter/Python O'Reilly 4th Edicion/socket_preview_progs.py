from socket_preview import server, client
import os, sys
from threading import Thread

mode = int(sys.argv[1])
if mode == 1:
	server()
elif mode == 2:
	client('client:process=%s' % os.getpid())
else:
	for i in range(5):
		Thread(target=client, args=('client:threa=%s' % i,)).start()
		

