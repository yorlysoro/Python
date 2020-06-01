#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  integral.py
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
def integral_x2(a,b,n):
	if n == 0:
		sumatorio = 0
	else:
		deltax = (b-a) / float(n)
		sumatorio = 0
		for i in range(n):
			sumatorio += deltax * (a + i * deltax) ** 2
		return sumatorio

inicio = float(raw_input('Inicio del intervalo: '))
final = float(raw_input('Final del intervalo: '))
partes = int(raw_input('Numero de rectangulos: '))

print 'La integral de x**2 entre %f y %f' %(inicio, final),
print ' vale aproximadamente %f' % integral_x2(inicio, final, partes)
