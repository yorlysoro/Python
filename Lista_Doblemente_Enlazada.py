#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Lista_Doblemente_Enlazada.py
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

from Nodo2 import Nodo

class ListaDoblementeEnlazada():
	def __init__(self):
		self.primero = None
		self.ultimo = None
		self.size = 0
	def vacia(self):
		return self.primero == None
	def agregar_final(self,dato):
		if self.vacia():
			self.primero = self.ultimo = Nodo(dato)
		else:
			aux = self.ultimo
			self.ultimo = aux.siguiente = Nodo(dato)
			self.ultimo.anterior = aux
		self.size += 1

	def agregar_inicio(self,dato):
		if self.vacia():
			self.primero = self.ultimo = Nodo(dato)
		else:
			aux = Nodo(dato)
			aux.siguiente = self.primero
			self.primero.anterior = aux
			self.primero = aux
		self.size += 1
	def recorrer_inicio(self):
		aux = self.primero
		while aux != None:
			print (aux.dato)
			aux = aux.siguiente
	def recorrer_fin(self):
		aux = self.ultimo
		while aux != None:
			print (aux.dato)
			aux = aux.anterior
	def size(self):
		return self.size
	def eliminar_inicio(self):
		if self.vacia():
			print ("Esta vacia")
		elif self.primero.siguiente == None:
			self.primero = self.ultimo == None
			self.size = 0
		else:
			self.primero = self.primero.siguiente
			self.primero.anterior = None
			self.size -= 1
	def eliminar_ultimo(self):
		if self.vacia():
			print("Esta vacia")
		elif self.primero.siguiente == None:
			self.primero = self.ultimo == None
			self.size = 0
		else:
			self.ultimo = self.ultimo.anterior
			self.ultimo.siguiente = None
			self.size -= 1
