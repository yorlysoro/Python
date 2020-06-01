#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Burbuja.py
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

lista = [10,2,0.5,3.7,4]

print (lista)
for x in range(len(lista)):
	y = 1
	for y in (range(len(lista))):
		if lista[y] > lista[x]:
			aux = lista[y]
			lista[y] = lista[x]
			lista[x] = aux
print (lista)
	
