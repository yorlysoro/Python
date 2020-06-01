#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Nodos.py
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


class Nodo():
	def __init__(self,dato,siguiente = None):
		self.dato = dato
		self.siguiente = siguiente

	def __str__(self):
		return str(self.dato)

def recorrer(nodo):
	while nodo != None:
		print(nodo.dato)
		nodo = nodo.siguiente

nodo4 = Nodo(12)
nodo3 = Nodo(45,nodo4)
nodo2 = Nodo(67,nodo3)
nodo1 = Nodo(89,nodo2)

recorrer(nodo1)
