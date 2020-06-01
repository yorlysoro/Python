#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Nodo_Fila_Prioridad.py
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

class Elemento:
	def __init__(self):
		self.Elemento = []
		self.Prioridad = -1

class Fila_Prioridad:
	def __init__(self):
		self.Frente = -1
		self.Final = -1
		self.filaTamano = 5
		self.arrayFila = Elemento()
