#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  estadisticas.py
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
from math import sqrt

def media(lista):
	s = 0
	for elemeto in lista:
		s += elemento
	return s / float(len(lista))
	
def varianza(lista):
	s = 0
	m = media(lista)
	for elemento in lista:
		s += (elemento - m) ** 2
	return s / float(len(lista))
	
def desviacion_tipica(lista):
	return sqrt(varianza(lista))
	

