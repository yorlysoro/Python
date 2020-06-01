#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Ejercicio_Pila.py
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

from Nodo_Pila_Ejercicio import Pila

class Pila_Constructor:
	def __init__(self):
		self.pila = Pila()
	def Vacia(self):
		if self.pila.pilatope == -1:
			return True
		else:
			return False

	def Elementos(self):
		return self.pila.pilatope + 1
	def Push(self,dato):
		self.pila.pilatope += 1
		self.pila.arrayPila.insert(self.pila.pilatope,dato)
	def Pop(self):
		self.pila.pilatope -= 1
		return self.pila.arrayPila.pop()
	
