#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Arbol_Binario.py
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

from Nodo_Arbol_Binario import Nodo

class Arbol_Binario_Busqueda:
	def __init__(self):
		self.root = None

	def empty(self):
		if self.root == None:
			return True
		else:
			return False

	def add(self,value):
		if self.empty():
			self.root = Nodo(value=value,is_root = True)
		else:
			nodo = self.__get_place(value)
			if value < nodo.value:
				nodo.left = Nodo(value=value,parent=nodo, is_left=True)
			else:
				nodo.right = Nodo(value=value, parent=nodo, is_right = True)
	
	def __get_place(self,value):
		aux = self.root
		while aux is not None:
			temp = aux
			if value <= aux.value:
				aux = aux.left
			else:
				aux = aux.right
		return temp
	def show_in_order(self,nodo):
		if nodo:
			self.show_in_order(nodo.left)
			print(nodo.value)
			self.show_in_order(nodo.right)

	def show_pre_order(self,nodo):
		if nodo:
			print(nodo.value)
			self.show_pre_order(nodo.left)
			self.show_pre_order(nodo.right)
	def show_pos_order(self,nodo):
		if nodo:
			self.show_pos_order(nodo.left)
			self.show_pos_order(nodo.right)
			print(nodo.value)
	def search(self,nodo,value):
		if nodo == None:
			return None
		else:
			if nodo.value == value:
				return nodo
			elif value <= nodo.value:
				return self.search(nodo.left,value)
			else:
				return self.search(nodo.right,value)
