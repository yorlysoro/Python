#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  POO1.py
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
class perro:
	patas = 4
	nombre = ""
	
	def nombrar(self,n):
		self.nombre = n
		
	
mascota = perro()
mascota2 = perro()

mascota.nombrar("Tom")
mascota2.nombrar("Lunna")
print "tengo un perro, se llama %s y tiene %s patas" %(mascota.nombre, mascota.patas)
print "tengo otro perro y se llama %s"%(mascota2.nombre)
