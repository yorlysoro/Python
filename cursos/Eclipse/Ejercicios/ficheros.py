f = open("Fraction Class.py", "r")

lineas = f.readlines()

print (lineas[0])
print (lineas[:])

f.close()

for line in open("Fraction Class.py", "r"):
	print (line)

fwrite = open("Copy Fraction Class.py", "w")
for line in open("Fraction Class.py", "r"):
	fwrite.write(line)
	
fwrite.close()
