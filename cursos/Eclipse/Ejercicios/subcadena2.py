from subcadena import subcadena
cadena = input("Dame otra cadena: ")
i = input("Dame un numero: ")
j = input("Dame otro numero: ")

if j > len(cadena):
	final = len(cadena)
else:
	final = j
subcadena = ''
for k in range(i, final):
	subcadena += cadena[k]
	
print("La subcadena entre %d y %d es %s" %(i,j,subcadena))