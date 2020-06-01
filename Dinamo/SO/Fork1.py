import os

print("Hola desde el programa", os.getpid())
print("Haciendo fork")
pid = os.fork()

if pid == 0:
	print("NOOOOOOOOO!")
	os.execl("./test.py", "one", "tow")
else:
	print("Yo soy tu padre!!!")
print("Adios desde el programa", os.getpid())
