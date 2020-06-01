#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Fila.py
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
from Nodos_Fila import Fila

class Fila_Implementacion:
	
	def __init__(self):
		self.filatamano = 5
		self.fila = Fila(0)

	def Elementos(self):
		return self.fila.final + 1

	def Vacia(self):
		if self.fila.final == -1:
			return True
		else:
			return False
	def Llena(self):
		if self.fila.final+1 == self.filatamano:
			return True
		else:
			return False
	def Frente(self):
		if self.Vacia():
			return -1
		else:
			return self.fila.arrayFila[self.fila.frente]

	def Final(self):
		if self.Vacia():
			return -1
		else:
			return self.fila.arrayFila[self.fila.final]
	def Insertar(self,dato):
		if self.Llena():
			print ("La fila esta llena no se puede insertar el dato ", dato)
		else:
			if self.fila.final == -1:
				self.fila.frente = 0
			self.fila.final += 1
			self.fila.arrayFila.insert(self.fila.final,dato)
	def Eliminar(self):
		if self.Vacia():
			print ("La fila esta vacia no hay mas elementos")
		else:
			print ("Se ha eleminado el elemento ", self.fila.arrayFila[self.fila.frente], " de la fila")
			self.fila.arrayFila.pop(self.fila.frente)
			self.fila.final -= 1
			if self.fila.final == -1:
				self.fila.frente = -1
	
			
