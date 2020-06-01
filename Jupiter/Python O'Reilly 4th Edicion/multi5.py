import os
from multiprocessing import Process

def runprogram(arg):
	os.execlp('python', 'python', 'child.py', str(arg))
	
for i in range(5):
	Process(target=runprogram, args=(i,)).start()
print('parent exit')
