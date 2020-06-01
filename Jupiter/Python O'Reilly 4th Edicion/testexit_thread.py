import _thread as thread
existat = 0

def child():
	global existat
	existat += 1
	threadid = thread.get_ident()
	print('Hello form child', threadid, existat)
	thread.exit()
	print('never reached')
	
	
def parent():
	while True:
		thread.start_new_thread(child, ())
		if input() == 'q': break
		
parent()
