#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
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
import re
import random
programas = {
	'salir' : ["chao", "hasta luego", "adios", "salir", "hasta mañana", "me voy", "me despido", "nos vemos"],
	'agregar' : ["agregar", "agrega", "nuevos programas", "nuevo programa"],
	'ver' : ["ver programas", "mostrar programas", "guardados", "ver guardados", "ver programas guardados", "mostrar programas guardados"],
	'abrir' : ["ejecutar", "abrir programas", "abrir programa"],
	'actualizar' : ["actualizar", "actualizar sistema", "actualizar programa"],
	'instalar' : ["instalar", "instalar programa", "instalar programas"]
}
def inicio():
	entrada = raw_input()
	verificar(entrada)
	
def salir():
	a = random.randint(0,4)
	adios = ["chao", "hasta luego", "adios", "hasta mañana", "nos vemos"]
	print adios[a]

def verificar(entrada):
	for i in range(0,7):
		if programas['salir'][i] == entrada:
			salir()
			break
	for i in range(0,3):
		if programas['agregar'][i] == entrada:
			agregar()
			break
	for i in range(0,3):
		if programas['ver'][i] == entrada:
			ver()
			break
	for i in range(0,2):		
		if programas['abrir'][i] == entrada:
			abrir()
			break
	for i in range(0,2):
		if programas['actualizar'][i] == entrada:
			actualizar()
			break
	for i in range(0,2):
		if programas['instalar'][i] == entrada:
			instalar()
			break

inicio()	


