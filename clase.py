#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  clase.py
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
def muestra_nota_de_alumno(alumnos, notas, alumno_buscado):
	encontrado = False
	for i in range(len(alumnos)):
		if alumnos[i] == alumno_buscado:
			print alumnos_buscado, nota[i]
			encontrado = True
			break
		if not encontrado:
			print 'El alumno %s no pertence al grupo' % alumno_buscado

