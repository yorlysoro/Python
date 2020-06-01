#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  registros.py
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
from record import record

class Persona(record):
	nombre = ''
	dni = ''
	edad = 0
	
def copia(pers):
	return Persona(nombre = pers.nombre[:], dni=pers.dni[:], edad = pers.edad)
	
def nada_util(persona1, persona2):
	persona1.edad = persona1.edad + 1
	persona3 = persona2 
	persona4 = copia(persona2)
	persona3.edad = persona3.edad - 1
	persona4.edad = persona4.edad - 2
	return persona4
	
juan = Persona(nombre = 'Juan Paz', dni = '123456789Z', edad = 19)
pedro = Persona(nombre='Pedro Lopez', dni= '234567889D', edad = 18)

otro = nada_util(juan, pedro)
print juan
print pedro
print otro

