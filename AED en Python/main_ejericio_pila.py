from Ejercicio_Pila import Pila_Constructor
import re
def Palindromo(cadena):
	pila = Pila_Constructor()
	palindromo = []
	for x in range(len(cadena)):
		pila.Push(cadena[x])

	for n in range(len(cadena)):
		palindromo.insert(n,pila.Pop())

	if list(palindromo) == list(cadena):
		return "La palabra es palindromo"
	else:
		return "La palabra no es palindromo"

def Inverso(cadena):
	pila = Pila_Constructor()
	reverso = []
	for x in range(len(cadena)):
		pila.Push(cadena[x])
	for x in range(len(cadena)):
		reverso.insert(x,pila.Pop())
	return reverso

def EvaluarExpresiones(expresion):
	operandos = Pila_Constructor()
	operadores = Pila_Constructor()
	Result = '0'
	for x in range(len(expresion)):
		if expresion[x] != ' ':
			if expresion[x] == '+' or expresion[x] == '-' or expresion[x] == '*' or expresion[x] == '/':
				if operadores.Vacia():
					if operandos.Elementos() > 0:
						operadores.Push(expresion[x])
					else:
						print ("Error. Operador sin operando previo: ", expresion[x])
						return '-1'
				else:
					print ("Error.Exceso de operadores: ", expresion[x])
					return '-1'
			elif expresion[x] >= '0' or expresion[x] <= '9':
				if operadores.Vacia():
					if operandos.Vacia():
						operandos.Push(expresion[x])
					else:
						print ("Error. Exceso de operandos: ", expresion[x])
						return '-1'
				else:
					coperador = operadores.Pop()
					coperandos = operandos.Pop()
					if coperador == '+':
						Result = str(int(coperandos) + int(expresion[x]))
					elif coperador == '-':
						Result = str(int(coperandos) - int(expresion[x]))
					elif coperador == '*':
						Result =  str(int(coperandos) * int(expresion[x]))
					else:
						Result = str(int(coperandos) // int(expresion[x]))
					operandos.Push(Result)
					Result = '0'
			else:
				print ("Error.Caracter invalido [", expresion[x],"]")
				return '-1'
				break
		elif Result == '-1':
			break
	if Result != '-1':
		if operandos.Elementos() == 1 and operadores.Vacia():
			Result = operandos.Pop()
		else:
			print("Error. Expresion con operandos/operadores de mas")
	return Result
	
print (Palindromo('amoraroma'))
print (''.join(Inverso('Carro')))

resultado = EvaluarExpresiones('2+4*6/2-2')
print (resultado)
