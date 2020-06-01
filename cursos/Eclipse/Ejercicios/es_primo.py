
num = int(input('Dame un numero: '))

creo_que_es_primo = True
divisor = 2
while divisor < num:
	if num % divisor == 0:
		creo_que_es_primo = False
		break
	divisor += 1
	
if creo_que_es_primo:
	print("El numero", num, "es primo")
else:
	print("EL numero", num, "no es primo")
	
	
