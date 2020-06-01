#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cifrar1.py
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
nombre_entrada = raw_input('Nombre del fichero de entrada: ')
nombre_salida = raw_input('Nombre del fichero de salida: ')

f_entrada = open(nombre_entrada, 'r')
f_salida = open(nombre_salida, 'w')

while 1:
	caracter = f_entrada.read(1)
	if caracter == '':
		break
	elif caracter >= 'a' and caracter <= 'y':
		f_salida.write(chr(ord(caracter) + 1))
	elif caracter == 'z':
		f_salida.write('a')
	else:
		f_salida.write(caracter)
f_entrada.close()
f_salida.close()
