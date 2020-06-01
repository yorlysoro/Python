import os
from multiprocessing import Process, Pipe

def sender(pipe):
	"""
	send object to parent on anonymous pipe
	"""
	pipe.send(['spam'] + [42, 'eggs'])
	pipe.close()

def talker(pipe):
	"""
	send and receive objects on a pipe
	"""
	pipe.send(dict(name='Bob', spam=42))
	reply = pipe.recv()
	print('talker got:', reply)
	
(parentEnd, childEnd) = Pipe()
Process(target=sender, args=(childEnd,)).start()
print('parent got:', parentEnd.recv())
parentEnd.close()

(parentEnd, childEnd) = Pipe()
child = Process(target=talker, args=(childEnd,))
child.start()
print('parent got:', parentEnd.recv())
parentEnd.send({x * 2 for x in 'spam'})
child.join()
print('parent exit')
