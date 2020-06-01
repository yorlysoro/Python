#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  cajero.py
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
carga50 = 100
carga20 = 100
carga10 = 100

def sacar_dinero(cantidad):
	global carga50, carga20, carga10
	if cantidad <= 50 * carga50 + 20 * carga20 + 10 * carga10:
		de50 = cantidad / 50
		cantidad = cantidad % 50
		if de50 >= carga50:
			cantidad = cantidad + (de50 - carga50) * 50
			de50 = carga50
		de20 = cantidad / 20
		cantidad = cantidad % 20
		if de20 >= carga20:
			cantidad = cantidad +(de20 - carga20) * 20
			de20 = carga20
		de10 = cantidad / 10
		cantidad = cantidad / 10
		if de10 >= carga10:
			cantidad = cantidad + (de10 - carga10) * 10
			de10 = carga10
		if cantidad == 0:
			carga50 = carga50 - de50
			carga20 = carga20 - de20
			carga10 = carga10 - de10
			return [de50, de20, de10]
		else:
			return [0, 0, 0]
	else:
		return [0, 0, 0]
		
while 50*carga50 + 20*carga20 + 10*carga10 > 0:
	peticion = int(raw_input('Cantidad que desea sacar: '))
	[de50, de20, de10] = sacar_dinero(peticion)
	if [de50, de20, de10] != [0, 0, 0]:
		if de50 > 0:
			print 'Billetes de 50 euros: ', de50
		if de20 > 0:
			print 'Billetes de 20 euros: ', de20
		if de10 > 0:
			print 'Billetes de 10 euros: ', de10
		print 'Gracias por usar el cajero.'
		print
	else:
		print 'Lamentos no poder atender su peticion.'
		print
print 'Cajero sin dinero. Avise a mantenimiento.'
