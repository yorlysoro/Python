#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Lista_Enlazada.py
#  
#  Copyright 2017 yorlys <yorlys@debian>
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
class Nodo(object):
	def __init__(self, dato = None, prox = None):
		self.dato = dato
		self.prox = prox
	def __str__(self):
		return str(self.dato)
		
		
		
V3 = Nodo("Bananas")
V2 = Nodo("Peras", V3)
V1 = Nodo("Manzanas", V2)

def verLista(nodo):
	"""Recorre todos los nodos a traves de sus enlaces, mostrando sus contenidos"""
	while nodo:
		print(nodo)
		nodo = nodo.prox

verLista(V1)
verLista(V2)
verLista(V3)
