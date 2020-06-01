#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  filas.py
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


class Filas:
	def __init__(self,cantidad):
		self.datos = []
		self.frente = -1
		self.final = -1
		self.cantidad = cantidad
	def Fila_Elementos(self):
		return self.final+1
	def Fila_Vacia(self):
		if self.final == -1:
			return True
		else:
			return False
	def Fila_Llena(self):
		if self.final == self.cantidad:
			return True
		else:
			return False
	def Fila_Frente(self):
		if self.Fila_Vacia() == True:
			return -1
		else:
			return self.datos[self.frente]
	def Fila_Final(self):
		if self.Fila_Vacia() == True:
			return -1
		else:
			return self.datos[self.final]
	def Fila_Insertar(self,dato):
		if self.Fila_Llena() == True:
			self.dato = dato
			print "La fila esta llena no se puede agregar el elemento ", self.dato
		else:
			self.dato = dato
			if self.final == -1:
				self.frente = 0
			self.final += 1
			self.datos.append(dato)
	def Fila_Eliminar(self):
		if self.Fila_Vacia() == True:
			print "La fila esta vacia no hay mas elementos para eleminar"
		else:
			print "Se acaba de eliminar el dato", self.datos[self.frente]
			self.datos.remove(self.datos[self.frente])
			self.final -= 1
			
filas = Filas(5)

print "El frente de la fila es ", filas.Fila_Frente()
print "El final de la fila es ", filas.Fila_Final()
print "Hay ", filas.Fila_Elementos(), " elementos en la fila"

filas.Fila_Insertar(2)

print "El frente de la fila es ", filas.Fila_Frente()
print "El final de la fila es ", filas.Fila_Final()
print "Hay ", filas.Fila_Elementos(), " elementos en la fila"

filas.Fila_Insertar(12)

print "El frente de la fila es ", filas.Fila_Frente()
print "El final de la fila es ", filas.Fila_Final()
print "Hay ", filas.Fila_Elementos(), " elementos en la fila"

filas.Fila_Insertar(14)

print "El frente de la fila es ", filas.Fila_Frente()
print "El final de la fila es ", filas.Fila_Final()
print "Hay ", filas.Fila_Elementos(), " elementos en la fila"


filas.Fila_Insertar(16)

print "El frente de la fila es ", filas.Fila_Frente()
print "El final de la fila es ", filas.Fila_Final()
print "Hay ", filas.Fila_Elementos(), " elementos en la fila"


filas.Fila_Insertar(18)

print "El frente de la fila es ", filas.Fila_Frente()
print "El final de la fila es ", filas.Fila_Final()
print "Hay ", filas.Fila_Elementos(), " elementos en la fila"

filas.Fila_Insertar(20)

print "El frente de la fila es ", filas.Fila_Frente()
print "El final de la fila es ", filas.Fila_Final()
print "Hay ", filas.Fila_Elementos(), " elementos en la fila"

filas.Fila_Insertar(30)

print "El frente de la fila es ", filas.Fila_Frente()
print "El final de la fila es ", filas.Fila_Final()
print "Hay ", filas.Fila_Elementos(), " elementos en la fila"


filas.Fila_Eliminar()
print "El frente de la fila es ", filas.Fila_Frente()
print "El final de la fila es ", filas.Fila_Final()
print "Hay ", filas.Fila_Elementos(), " elementos en la fila"

filas.Fila_Eliminar()
print "El frente de la fila es ", filas.Fila_Frente()
print "El final de la fila es ", filas.Fila_Final()
print "Hay ", filas.Fila_Elementos(), " elementos en la fila"
