#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pila import Pila

def calculadora_polaca(elementos):
	"""Dada una lista de elementos que representan componentes de una expresion en notacion polaca inversa, evalua dicha expresion. Si la expresion esta mal formada, levanta ValueError"""
	
	p = Pila()
	for elemento in elementos:
		print ("DEBUG:", elemento)
		try: 
			numero = float(elemento)
			p.apilar(numero)
			print("DEBUG: apila ", numero)
		except ValueError:
			if elemento not in "+-*/ %" or len(elemento) != 1:
				raise ValueError("Operador Invalido")
			try:
				a1 = p.desapilar()
				print("DEBUG: desapila ", a1)
				a2 = p.desapilar()
				print("DEBUG: desapila ", a2)
			except ValueError:
				print("DEBUG: error pila faltan openandos")
				raise ValueError("Faltan openrandos")
			if elemento == '+':
				resultado = a2 + a1
			elif elemento == '-':
				resultado = a2 - a1
			elif elemento == '*':
				resultado = a2 * a1
			elif elemento == '/':
				resultado = a2 / a1
			elif elemento == '%':
				resultado = a2 % a1
			print("DEBUG: apila ", resultado)
			p.apilar(resultado)
		res = p.desapilar()
		if p.es_vacia():
			return res
		else:
			print("DEBUG: error pila sobran openrandos")
			raise ValueError("Sobran operandos")
	print(elementos)
def main():
	expresion = input("Ingrese la expresion a evaluar: ")
	elementos = expresion.split()
	print(elementos)
	print (calculadora_polaca(elementos))

if __name__ == '__main__':
	main()
