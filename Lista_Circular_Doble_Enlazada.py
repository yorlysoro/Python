#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Lista_Circular_Doble_Enlazada.py
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
from Nodo_Circular2 import Nodo

class ListaCircularDobleEnlazada():
	def __init__(self):
		self.primero = None
		self.ultimo = None
	def vacia(self):
		if self.primero == None:
			return True
		else:
			return False
	def agregar_inicio(self,dato):
		if self.vacia():
			self.primero = self.ultimo = Nodo(dato)
		else:
			aux = Nodo(dato)
			aux.siguiente = self.primero
			self.primero.anterior = aux
			self.primero = aux
		self.__unir_nodos()
			
	def agregar_final(self,dato):
		if self.vacia():
			self.primero = self.ultimo = Nodo(dato)
		else:
			aux = self.ultimo
			self.ultimo = aux.siguiente = Nodo(dato)
			self.ultimo.anterior = aux
		self.__unir_nodos()
			
	def __unir_nodos(self):
		if self.primero != None:
			self.primero.anterior = self.ultimo
			self.ultimo.siguiente = self.primero
		
	def recorrer_inicio_a_fin(self):
		aux = self.primero
		while aux:
			print(aux.dato)
			aux = aux.siguiente
			if aux == self.primero:
				break

	def recorrer_fin_a_inicio(self):
		aux = self.ultimo
		while aux:
			print(aux.dato)
			aux = aux.anterior
			if aux == self.ultimo:
				break
	def eliminar_inicio(self):
		if self.vacia():
			print ("La lista esta vacia")
		elif self.primero == self.ultimo:
			self.primero = self.ultimo = None
		else:
			self.primero = self.primero.siguiente
		self.__unir_nodos()
		
	def eliminar_ultimo(self):
		if self.vacia():
			print ("La lista esta vacia")
		elif self.primero == self.ultimo:
			self.primero = self.ultimo = None
		else:
			self.ultimo = self.ultimo.anterior
		self.__unir_nodos()

	def buscar(self,dato):
		aux = self.primero
		while aux:
			if aux.dato == dato:
				return True
			else:
				aux = aux.siguiente
				if aux == self.primero:
					return False
