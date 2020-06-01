#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Lista_Circular.py
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

from Nodo_Circular import Nodo

class ListaCircular():

	def __init__(self):
		self.primero = None
		self.ultimo = None

	def vacia(self):
		return self.primero == None
	def agregar_inicio(self,dato):
		if self.vacia():
			self.primero = self.ultimo = Nodo(dato)
			self.ultimo.siguiente = self.primero
		else:
			aux = Nodo(dato)
			aux.siguiente = self.primero
			self.primero = aux
			self.ultimo.siguiente = self.primero
			
	def agregar_final(self,dato):
		if self.vacia():
			self.primero = self.ultimo = Nodo(dato)
			self.ultimo.siguiente = self.primero
		else:
			aux = self.ultimo
			self.ultimo = aux.siguiente = Nodo(dato)
			self.ultimo.siguiente = self.primero
			
	def recorrer(self):
		aux = self.primero
		while aux:
			print(aux.dato)
			aux = aux.siguiente
			if aux == self.primero:
				break
	def remover_inicio(self):
		if self.vacia():
			print ("Lista vacia")
		elif self.primero == self.ultimo:
			self.primero = self.ultimo == None
		else:
			self.primero = self.primero.siguiente
			self.ultimo.siguiente = self.primero
			
	def remover_final(self):
		if self.vacia():
			print ("Lista vacia")
		elif self.primero == self.ultimo:
			self.primero = self.ultimo = None
		else:
			aux = self.primero
			while aux.siguiente != self.ultimo:
				aux = aux.siguiente
			aux.siguiente = self.primero
			self.ultimo = aux
