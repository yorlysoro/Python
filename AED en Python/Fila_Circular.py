#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Fila_Circular.py
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
from Nodo_Fila_Circular import Fila_Circular

class Fila_Circular_Implementacion:
	def __init__(self):
		self.fila = Fila_Circular()
		for x in range(self.fila.tamanoFila):
			self.fila.arrayFila.insert(x,-1)

	def Vacia(self):
		if self.fila.Final == -1:
			return True
		else:
			return False
	def Elementos(self):
		if self.Vacia():
			return 0
		elif self.fila.Final >= self.fila.Frente:
			return self.fila.Final - self.fila.Frente + 1
		else:
			return self.fila.tamanoFila - self.fila.Frente + self.fila.Final + 1
	def Llena(self):
		if self.Elementos() == self.fila.tamanoFila:
			return True
		else:
			return False
	def Insertar(self,dato):
		if self.Vacia():
			self.fila.Final += 1
			self.fila.Frente += 1
			self.fila.arrayFila[self.fila.Final] = dato
		else:
			if self.fila.Final + 1 == self.fila.tamanoFila:
				self.fila.Final = 0
				self.fila.arrayFila[self.fila.Final] = dato
			else:
				self.fila.Final += 1
				self.fila.arrayFila[self.fila.Final] = dato
	def Eliminar(self):
		if self.Vacia():
			return -1
		else:
			self.fila.arrayFila[self.fila.Frente] = -1
			if self.fila.Final == self.fila.Frente:
				self.fila.Final = -1
				self.fila.Frente = -1
			else:
				if self.fila.Frente+1 == self.fila.tamanoFila:
					self.fila.Frente = 0
				else:
					self.fila.Frente += 1

	def Mostrar(self):
		for x in self.fila.arrayFila:
			if x != -1:
				print(x)
		
