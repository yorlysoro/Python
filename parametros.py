#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  parametros.py
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
def modifica(a,b):
	for elemento in b:
		a.append(elemento)
	b = b + [4]
	a[-1] = 100
	del b[0]
	return b[:]
	
lista1 = [1,2,3]
lista2 = [4,5,6]

lista3 = modifica(lista1, lista2)

print lista1
print lista2
print lista3
