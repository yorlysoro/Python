#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  area_y_angulo.py
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
from math import sqrt, asin, pi

def area_triangulo(a,b,c):
	s = (a + b + c) / 2.0
	return sqrt(s * (s-a) * (s-b) * (s-c))
	
def angulo_alfa(a, b, c):
	s = area_triangulo(a, b, c)
	return 180 / pi * asin(2.0 * s / (b*c))
	
def menu():
	opcion = 0
	while opcion != 1 and opcion != 2:
		print '1) Calcular area del triangulo'
		print '2) Calcular angulo opuesto al primer lado'
		opcion = int(raw_input('Escoge opcion: '))
	return opcion
	
lado1 = float(raw_input('Dame lado a: '))
lado2 = float(raw_input('Dame lado b: '))
lado3 = float(raw_input('Dame el lado c: '))

s = menu()

if s == 1:
	resultado = area_triangulo(lado1, lado2, lado3)
	
else:
	resultado = angulo_alfa(lado1, lado2, lado3)
	
print 'Escogistes la opcion', s
print 'El resultado es: ', resultado
