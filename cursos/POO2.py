#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  POO2.py
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
class animal:
	def __init__(self, nombre = None, patas=4):
		self.nombre = nombre
		self.patas = patas
		self.tipo = "Can"
		
x = animal("Tobias", 2)
y = animal("Humberto")

print x.nombre,x.patas,x.tipo
print y.nombre,y.patas,y.tipo
