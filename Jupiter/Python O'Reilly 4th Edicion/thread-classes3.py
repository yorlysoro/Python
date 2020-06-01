import threading, _thread
class Power:
	def __init__(self, i):
		self.i = i
	def action(self):
		print(self.i ** 32)


obj = Power(2)
threading.Thread(target=obj.action).start()

def action(i):
	def power():
		print(i ** 32)
		
	return power
	
threading.Thread(target=action(2)).start()

_thread.start_new_thread(obj.action, ())
_thread.start_new_thread(action(2), ())
