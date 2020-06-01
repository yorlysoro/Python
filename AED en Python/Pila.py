#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Pila.py
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
from Nodo_Pila import Pila
class Implementacion_Pila:
	def __init__(self):
		self.tamanopila = 5
		self.pila = Pila(0)
	def Pila_Vacia(self):
		if self.pila.pilatope == -1:
			return True
		else:
			return False
	def Pila_Llena(self):
		if self.pila.pilatope+1 == self.tamanopila:
			return True
		else:
			return False
	def Pila_Elementos(self):
		return self.pila.pilatope + 1
	def Pila_Cima(self):
		if self.Pila_Vacia():
			print ("La pila esta vacia; no hay elementos en la cima")
		else:
			print ("Pila cima: ", self.pila.arrayPila[self.pila.pilatope])
	def Pila_Push(self,dato):
		if self.Pila_Llena():
			print ("La pila esta llena no es posible agregar el elemento %d a la pila" %(dato))
		else:
			self.pila.pilatope += 1
			self.pila.arrayPila.insert(self.pila.pilatope,dato) 
			print ("Se agrego el elemento %d a la pila" %(dato))

	def Pila_Pop(self):
		if self.Pila_Vacia():
			print ("La pila esta vacia no se pueden sacar mas elementos")
		else:
			print ("Se ha sacado el elemento", self.pila.arrayPila[self.pila.pilatope], " de la pila" )
			self.pila.arrayPila.pop()
			self.pila.pilatope -= 1
