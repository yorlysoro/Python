#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cifrar.py
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
nombre = raw_input('Nombre del fichero: ')
fichero = open(nombre, 'r')

texto = ''
while 1:
	caracter = fichero.read(1)
	if caracter == '':
		break
	elif caracter >= 'a' and caracter <= 'y':
		texto += chr(ord(caracter) + 1)
	elif caracter == 'z':
		texto += 'a'
	else:
		texto += caracter
fichero.close()
print texto

