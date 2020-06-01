#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  videoclub.py
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

class Socio(record):
	dni = ''
	nombre = ''
	telefono = ''
	domicilio = ''
	
class Pelicula(record):
	titulo = ''
	genero = ''
	
class Videoclub(record):
	socios = []
	peliculas = []
	
def menu():
	print '*** VIDEOCLUB ***'
	print '1) Dar de alto nuevo socio'
	print '2) Dar de baja un socio'
	print '3) Dar de alta nueva pelicula'
	print '4) Dar de baja una pelicula'
	print '5) Salir'
	opcion = int(raw_input('Escoge opcion: '))
	while opcion < 1 or opcion > 5:
		opcion = int(raw_input('Escoge opcion (entre 1 y 5): '))
		
	return opcion
	
videoclub = Videoclub()

opcion = menu()
while opcion != 5:
	if opcion == 1:
		print 'Alta de socio'
		socio = lee_socio()
		if contiene_socio_con_dni(videoclub, socio.dni):
			print 'Operacion anulada: Ya existia un socio con DNI ', socio.dni
		else:
			alta_socio(videoclub, socio)
			print 'Socio con DNI ', socio.dni, ' dado de alta'
	elif opcion == 2:
		print 'Baja de socio'
		dni = raw_input('DNI: ')
		if contiene_socio_con_dni(videoclub, dni):
			baja_socio(videoclub, dni)
			print 'Socio con DNI ', dni , ' dado de baja'
		else:
			print 'Operacion anulada: No existe ningun socio con DNI ', dni
	elif opcion == 3:
		print 'Alta de pelicula'
		pelicula = lee_pelicula()
		if contiene_pelicula_con_titulo(videoclub, pelicula.titulo):
			print 'Operacion anulada: Ya hay una pelicula con titulo ', pelicula.titulo
		else:
			alta_pelicula(videoclub, pelicula)
			print 'Pelicula ', pelicula.titulo, ' dada de alta'
	elif opcion == 4:
		print 'Baja de pelicula'
		titulo = raw_input('Titulo: ')
		if contiene_pelicula_con_titulo(videoclub, titulo):
			baja_pelicula(videoclub, titulo)
			print 'Pelicula ', titulo, ' dada de baja'
		else:
			print 'Operacion anulada: No existe ninguna pelicula llamada ', titulo
	opcion = menu()
	
	
print 'Gracias por usar nuestro programa'
