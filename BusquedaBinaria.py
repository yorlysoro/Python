#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  BusquedaBinaria.py
#  
#  Copyright 2016 Yorlys Oropeza <yorlys@debian>
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

lista = [5,12,15,30,50,65,70,87,88,96]

def busqueda_binaria(dato):
	izquierda = 0
	derecha = len(lista)-1
	while izquierda <= derecha:
		medio = (izquierda+derecha)//2
		if dato == lista[medio]:
			return medio
		elif dato < lista[medio]:
			derecha = medio - 1
		else:
			izquierda = medio + 1
	return None
	
def buscar(dato):
	if busqueda_binaria(dato) == None:
		return "El dato %d no se encontro" %(dato)
	else:
		return "El dato %d se encontro en el indice: %d" %(dato,busqueda_binaria(dato))

print (buscar(70))


