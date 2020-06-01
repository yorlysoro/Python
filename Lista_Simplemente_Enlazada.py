#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Lista_Simplemente_Enlazada.py
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


from Nodo import Nodo

class ListaSimpleEnlazada():
	
	def __init__(self):
		self.primero = None
		self.ultimo = None
	def Vacia(self):
		return self.primero == None
	def agregar_ultimo(self,dato):
		if self.Vacia():
			self.primero = self.ultimo = Nodo(dato)
		else:
			aux = self.ultimo
			self.ultimo = aux.siguiente = Nodo(dato)
	def recorrido(self):
		aux =  self.primero
		while aux != None:
			print(aux.dato)
			aux = aux.siguiente
	def eliminar_ultimo(self):
		aux = self.primero
		while aux.siguiente != self.ultimo:
			aux = aux.siguiente
		aux.siguiente = None
		self.ultimo = aux

	def agregar_inicio(self,dato):
		if self.Vacia():
			self.primero = self.ultimo = Nodo(dato)
		else:
			aux = Nodo(dato)
			aux.siguiente = self.primero
			self.primero = aux
	def eliminar_inicio(self):
		self.primero = self.primero.siguiente
			
