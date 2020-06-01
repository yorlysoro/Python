#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  integracion.py
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
def cuadrado(x):
	return x**2
def cubo(x):
	return x**3
	
def integral_definida(f,a,b,n):
	if n == 0:
		sumatorio = 0
	else:
		deltax = (b - a) / float(n)
		sumatorio = 0
		for i in range(n):
			sumatorio += deltax * f(a + i * deltax)
		return sumatorio

a = 1
b = 2
print 'Integracion entre %f y %f' %(a,b)
print 'Integral de x**2: ', integral_definida(cuadrado, a, b, 100)
print 'Integral de x**3: ', integral_definida(cubo, a, b, 100)
