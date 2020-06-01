#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pilas.py
#  
#  Copyright 2016 Yorlys Oropeza <yorlys@debian>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
class Pila:
	def __init__(self,cantidad):
		self.tope = -1
		self.datos = []
		self.cantidad = cantidad
	
	def Pila_Vacia(self):
		if self.tope == -1:
			return True
		else:
			return False
	def Pila_Llena(self):
		if self.tope == self.cantidad:
			return True
		else:
			return False
	def Elementos_Pila(self):
		if self.Pila_Vacia == True:
			return self.tope + 1
		else:
			return self.tope + 1
	def Elemento_Cima(self):
		if self.Pila_Vacia() == True:
			print "La pila esta vacia no hay elemento en la cima"
		else:
			print "El elemento en la cima es ", self.datos[self.tope]
	def Pila_Push(self,dato):
		if self.Pila_Llena() == True:
			self.dato = dato
			print "La pila esta llena no se puede agregar el elmento ", self.dato
		else:
			self.tope += 1
			self.datos.append(dato)
	def Pila_Pop(self):
		if self.Pila_Vacia() == True:
			print "La pila esta vacia no hay elementos que sacar"
		else:
			print "Se a sacado el dato ", self.datos[self.tope]
			self.datos.remove(self.datos[self.tope])
			self.tope -= 1
	def Visualizar(self):
		if self.Pila_Vacia() == True:
			print "La pila esta vacia no se pueden mostrar elementos"
		else:
			n = self.tope
			while n != -1:
				print self.datos[n], " "
				n -= 1
pilas = Pila(5)
print "Hay ",pilas.Elementos_Pila()," elementos en la pila"
pilas.Elemento_Cima()
pilas.Visualizar()

pilas.Pila_Push(5)
print "Hay ",pilas.Elementos_Pila()," elementos en la pila"
pilas.Elemento_Cima()
pilas.Visualizar()

pilas.Pila_Push(10)
print "Hay ",pilas.Elementos_Pila()," elementos en la pila"
pilas.Elemento_Cima()
pilas.Visualizar()

pilas.Pila_Push(25)
print "Hay ",pilas.Elementos_Pila()," elementos en la pila"
pilas.Elemento_Cima()
pilas.Visualizar()

pilas.Pila_Push(40)
print "Hay ",pilas.Elementos_Pila()," elementos en la pila"
pilas.Elemento_Cima()
pilas.Visualizar()

pilas.Pila_Push(48)
print "Hay ",pilas.Elementos_Pila()," elementos en la pila"
pilas.Elemento_Cima()
pilas.Visualizar()

pilas.Pila_Push(8)
print "Hay ",pilas.Elementos_Pila()," elementos en la pila"
pilas.Elemento_Cima()
pilas.Visualizar()

pilas.Pila_Push(4)
print "Hay ",pilas.Elementos_Pila()," elementos en la pila"
pilas.Elemento_Cima()
pilas.Visualizar()

pilas.Pila_Pop()
print "Hay ",pilas.Elementos_Pila()," elementos en la pila"
pilas.Elemento_Cima()
pilas.Visualizar()

pilas.Pila_Pop()
print "Hay ",pilas.Elementos_Pila()," elementos en la pila"
pilas.Elemento_Cima()
pilas.Visualizar()

pilas.Pila_Pop()
print "Hay ",pilas.Elementos_Pila()," elementos en la pila"
pilas.Elemento_Cima()
pilas.Visualizar()

pilas.Pila_Pop()
print "Hay ",pilas.Elementos_Pila()," elementos en la pila"
pilas.Elemento_Cima()
pilas.Visualizar()

pilas.Pila_Pop()
print "Hay ",pilas.Elementos_Pila()," elementos en la pila"
pilas.Elemento_Cima()
pilas.Visualizar()

pilas.Pila_Pop()
print "Hay ",pilas.Elementos_Pila()," elementos en la pila"
pilas.Elemento_Cima()
pilas.Visualizar()

