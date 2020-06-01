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


class Pila:
	def __init__(self,size):
		self.lista = []
		self.tope = 0
		self.size = size
	def empty(self):
		if self.tope == 0:
			return True
		else:
			return False
	def push(self,dato):
		if self.tope < self.size:
			self.lista += [dato]
			self.tope += 1
		else:
			print("La pila esta llena")
	def pop(self):
		if self.empty():
			print ("La pila esta vacia")
		else:
			self.tope -= 1
			self.lista = [self.lista[x] for x in range(self.tope)]
			
	def show(self):
		i = self.tope - 1
		while i > -1:
			print ( "[%d] => %d" %(i,self.lista[i]))
			i -= 1

	def size(self):
		return self.tope

	def top(self):
		return self.lista[-1]
