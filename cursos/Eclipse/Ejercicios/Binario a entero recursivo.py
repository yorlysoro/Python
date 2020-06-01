import math 

def binario_a_entero(binario,i):
	acarreo = 0
	if len(binario) == 1:
		if binario == "1":
			acarreo = int(math.pow(2,i))
		return acarreo
	else:
		if binario[len(binario)-1] == "1":
			acarreo = int(math.pow(2,i))
		return acarreo + binario_a_entero(binario[0:len(binario)-1], i+1)
		
entrada = input("Ingrese un binario: ")
print(binario_a_entero(entrada, 0))
