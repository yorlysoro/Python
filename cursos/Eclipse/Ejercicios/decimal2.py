bits = input('Dame un numero binario: ')

valor = 0
for bit in bits:
	valor += valor + int(bit)
	
print("Su valor decimal es ", valor)
