#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Quicksort.py
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

lista = [4,3,1,5,2,6,8]

print (lista)
j = len(lista)-1
i = 0
def quicksort(lista,i,j):
	fin = j
	inicio = i
	pivote = lista[i]
	while i <= j:
		while lista[i] < pivote:
			i = i+1
		while lista[j] > pivote:
			j = j-1
		if i <= j:
			aux = lista[i]
			lista[i] = lista[j]
			lista[j] = aux
			i = i+1
			j = j-1
	if inicio < j:
		quicksort(lista,inicio,j)
	if i < fin:
		quicksort(lista,i,fin)

quicksort(lista,i,j)
print (lista)
			
