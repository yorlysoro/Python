from builtins import int
cadena = input("Dame una cadena: ")
i = int(input("Dame un numero: "))
j = int(input("Dame otro numero: "))

subcadena = ''
for k in range(i,j):
	subcadena += cadena[k]
	
	
print("La subcadena entre %d y %d es %s" % (i,j,subcadena))