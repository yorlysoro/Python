#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  burbuja2.py
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
lista = [2, 26, 4, 3, 1]

for i in range(1, len(lista)):
	print 'Pasada ', i
	for j in range(0, len(lista)-i):
		print ' Comparacion de los elementos en posicion %d y %d' %(j, j+1)
		if lista[j] > lista[j+1]:
			elemento = lista[j]
			lista[j] = lista[j+1]
			lista[j+1] = elemento
			print ' Se intercambian '
		print ' Estado actual de la lista ', lista

print lista
