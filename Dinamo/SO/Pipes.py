import pipes
import os
import time
import random

pipe = pipes.Template()

print("Program Started:", os.getpid())

newpid = os.fork()
f = pipe.open("pipefile", "w")
#f.append('tr a-z A-Z', '--')
if newpid == 0:
	f.close()
	time.sleep(random.randint(0,10))
	print("Read from parent:")
	print(open("pipefile").read())
else:
	f.close()
	message = "Hello world!"
	time.sleep(random.randint(0,10))
	print("Sendint message to shild!")
	f = pipe.open("pipefile", "w")
	f.write(message)
	
print("Program Finished:", os.getpid())
