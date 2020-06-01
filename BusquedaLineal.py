#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  BusquedaLineal.py
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

def busquedalineal(dato):
	for x in range(0,len(lista)):
		print ("[%d] => [%d]"%(x,lista[x]))
		if lista[x] == dato:
			return x
	return None
		
def buscar(dato):
	if busquedalineal(dato) == None:
		return "El dato %d no se encontro"%(dato)
	else:
		return "El dato %d se encontro en el indice: %d"%(dato,busquedalineal(dato))


lista = [12,45,78,9,6,5,4,2,1,0,12,45,78,63,25,98]
print (lista)

#for i in range(len(lista)):
	#print ("[%d] => [%d]" %(i,lista[i]))

print (buscar(100))
