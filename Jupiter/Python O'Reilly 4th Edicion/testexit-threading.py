import threading, sys, time

def action():
	sys.exit()
	print('not reached')

threading.Thread(target=action).start()
time.sleep(2)
print('Main exit')
