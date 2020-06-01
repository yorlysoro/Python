#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  circulo.py
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
from math import pi

radio = float(raw_input('Dame el radio de un circulo: '))

print 'Escoge una opcion: '
print 'a) Calcular el diametro.'
print 'b) Calcular el perimetro.'
print 'c) Calcular el area.'
opcion = raw_input('Teclea a, b o c y pulsa el retorno de carro: ')


if opcion == 'a':
	diametro = 2 * radio
	print 'El diametro es ', diametro
	
else:
	if opcion == 'b':
		perimetro = 2 * pi * radio
		print 'El perimetro es ', perimetro
	else:
		if opcion == 'c':
			area = pi * radio ** 2
			print 'El area es ', area
