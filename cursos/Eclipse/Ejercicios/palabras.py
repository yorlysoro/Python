cadena = input('Escribe una frase: ')
while cadena != '':
	blancos = 0
	for caracter in cadena:
		if caracter == ' ':
			blancos += 1
	palabras = blancos + 1 
	print("Palabras: ", palabras)
	
	cadena = input("Escribe una frase: ")