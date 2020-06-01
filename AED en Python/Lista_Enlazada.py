#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Lista_Enlazada.py
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

from Nodo_Lista_Enlazada import Nodo_Lista_Enlazada

class Lista_Enlazada:
	def __init__(self):
		self.primero = None
		self.ultimo = None

	def Vacia(self):
		if self.primero == None:
			return True
		else:
			return False
	def Insertar(self,dato):
		if self.Vacia():
			self.primero = self.ultimo = Nodo_Lista_Enlazada(dato)
			print("Se ha insertado el dato ", dato, " como el primero de la lista")
		else:
			aux = self.ultimo
			self.ultimo = aux.siguiente = Nodo_Lista_Enlazada(dato)
			print("Se ha insertado el elemento ", dato, " en el frente de la lista")

	def Eliminar(self):
		if self.Vacia():
			print ("La lista esta vacia")
		else:
			aux = self.primero
			if aux.siguiente != None:
				while aux.siguiente != self.ultimo:
					aux = aux.siguiente
			aux.siguiente = None
			self.ultimo = aux
			if aux == aux.siguiente:
				self.primero = None
			print("Se elimino un elemento")
	def Recorrer(self):
		aux = self.primero
		while aux != None:
			print(aux.dato)
			aux = aux.siguiente
