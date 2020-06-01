#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ejercicio2.py
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
#  s
from random import *
def escribirArray(array):
	for i in array:
		print(i)
		
a = list(i for i in range(100))
par = list(i for i in range(100))
impar = list(i for i in range(100))

for i in range(len(a)):
	a[i] = randint(0,100) % 100 + 1
print("Primer Array")
escribirArray(a)
tam = len(a)
for i in range(tam):
	if a[i] % 2 == 0:
		par[i] = a[i]
	else:
		impar[i] = a[i]

print("Par")
escribirArray(par)
print("Impar")
escribirArray(impar)

j = 0
b = list(i*0 for i in range(199))
for i in range(tam):
	if par[i] != 0:
		b[j] = par[i]
		j+=1
for i in range(tam):
	if impar[i] != 0:
		b[j] = impar[i]
		j+=1

print("Resultado final")
escribirArray(b)
