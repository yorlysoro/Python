#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  filas_circulares.py
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

class Fila_Circular:
	def __init__(self,cantidad):
		self.final = -1
		self.frente = -1
		self.datos = []
		self.cantidad = cantidad
	def Fila_Vacia(self):
		if self.final == -1:
			return True
		else:
			return False
	def Fila_Circular_Elementos(self):
		if self.Fila_Vacia() == True:
			return 0
		else:
			return self.final + 1
	def Fila_Circular_Llena(self):
		if self.Fila_Circular_Elementos() == self.cantidad+1:
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
	def Fila_Circular_Insertar(self,dato):
		if self.final == -1 :
			self.final = 0
			self.datos.append(dato)
		elif self.final+1 == self.cantidad+1:
			self.frente -= 1
			self.final += 1
			self.datos.pop(self.frente)
			self.datos.insert(self.frente,dato)
		elif self.frente == self.cantidad:
			self.final += 1
			self.frente += 1
			self.datos.pop(self.final)
			self.datos.insert(self.final,dato)
		else:
			self.final += 1
			self.datos.append(dato)
		def Fila_Circular_Eliminar(self):
			if self.Fila_Vacia() == True:
				print "La fila esta vacia no se pueden sacar mas elementos"
			else:
				print "Se ha eliminado el elemento ",self.datos[self.frente], " de la lista"
				self.datos.pop(self.frente)
				self.datos.insert(self.frente, 0)
				self.frente += 1
				self.final -= 1
	def Fila_Circular_Despliega(self):
		if self.Fila_Vacia() == True:
			print "La lista vacia no se pueden mostrar elementos"
		else:
			print self.datos

fila_circular = Fila_Circular(4)
print "La fila tiene ",fila_circular.Fila_Circular_Elementos(), " elementos"
print "El frente de la fila es ", fila_circular.Fila_Frente()
print "El final de la fila es ", fila_circular.Fila_Final()
print "La fila esta vacia ", fila_circular.Fila_Vacia()
print "La fila esta llena ", fila_circular.Fila_Circular_Llena()
fila_circular.Fila_Circular_Despliega()
 
fila_circular.Fila_Circular_Insertar(10)
print "La fila tiene ",fila_circular.Fila_Circular_Elementos(), " elementos"
print "El frente de la fila es ", fila_circular.Fila_Frente()
print "El final de la fila es ", fila_circular.Fila_Final()
print "La fila esta vacia ", fila_circular.Fila_Vacia()
print "La fila esta llena ", fila_circular.Fila_Circular_Llena()
fila_circular.Fila_Circular_Despliega()			
 
fila_circular.Fila_Circular_Insertar(20)
print "La fila tiene ",fila_circular.Fila_Circular_Elementos(), " elementos"
print "El frente de la fila es ", fila_circular.Fila_Frente()
print "El final de la fila es ", fila_circular.Fila_Final()
print "La fila esta vacia ", fila_circular.Fila_Vacia()
print "La fila esta llena ", fila_circular.Fila_Circular_Llena()
fila_circular.Fila_Circular_Despliega()			
				
fila_circular.Fila_Circular_Insertar(30)
print "La fila tiene ",fila_circular.Fila_Circular_Elementos(), " elementos"
print "El frente de la fila es ", fila_circular.Fila_Frente()
print "El final de la fila es ", fila_circular.Fila_Final()
print "La fila esta vacia ", fila_circular.Fila_Vacia()
print "La fila esta llena ", fila_circular.Fila_Circular_Llena()
fila_circular.Fila_Circular_Despliega()
			
fila_circular.Fila_Circular_Insertar(40)
print "La fila tiene ",fila_circular.Fila_Circular_Elementos(), " elementos"
print "El frente de la fila es ", fila_circular.Fila_Frente()
print "El final de la fila es ", fila_circular.Fila_Final()
print "La fila esta vacia ", fila_circular.Fila_Vacia()
print "La fila esta llena ", fila_circular.Fila_Circular_Llena()
fila_circular.Fila_Circular_Despliega()
			
fila_circular.Fila_Circular_Insertar(50)
print "La fila tiene ",fila_circular.Fila_Circular_Elementos(), " elementos"
print "El frente de la fila es ", fila_circular.Fila_Frente()
print "El final de la fila es ", fila_circular.Fila_Final()
print "La fila esta vacia ", fila_circular.Fila_Vacia()
print "La fila esta llena ", fila_circular.Fila_Circular_Llena()
fila_circular.Fila_Circular_Despliega()			

fila_circular.Fila_Circular_Insertar(60)
print "La fila tiene ",fila_circular.Fila_Circular_Elementos(), " elementos"
print "El frente de la fila es ", fila_circular.Fila_Frente()
print "El final de la fila es ", fila_circular.Fila_Final()
print "La fila esta vacia ", fila_circular.Fila_Vacia()
print "La fila esta llena ", fila_circular.Fila_Circular_Llena()
fila_circular.Fila_Circular_Despliega()	

fila_circular.Fila_Circular_Insertar(70)
print "La fila tiene ",fila_circular.Fila_Circular_Elementos(), " elementos"
print "El frente de la fila es ", fila_circular.Fila_Frente()
print "El final de la fila es ", fila_circular.Fila_Final()
print "La fila esta vacia ", fila_circular.Fila_Vacia()
print "La fila esta llena ", fila_circular.Fila_Circular_Llena()
fila_circular.Fila_Circular_Despliega()


fila_circular.Fila_Circular_Insertar(75)
print "La fila tiene ",fila_circular.Fila_Circular_Elementos(), " elementos"
print "El frente de la fila es ", fila_circular.Fila_Frente()
print "El final de la fila es ", fila_circular.Fila_Final()
print "La fila esta vacia ", fila_circular.Fila_Vacia()
print "La fila esta llena ", fila_circular.Fila_Circular_Llena()
fila_circular.Fila_Circular_Despliega()
