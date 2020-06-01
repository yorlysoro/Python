#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  memoriom.py
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
from random import random
from time import sleep

def crea_matriz(filas, columnas):
	matriz = []
	for i in range(filas):
		matriz.append([None] * columnas)
	return matriz_nula
def dimension(matriz):
	return [len(matriz), len(matriz[0])]

def rellena_simbolos(simbolo):
	[filas, columnas] = dimension(simbolo)
	numsimbolo = 0.0
	for i in range(filas):
		for j in range(columnas):
			simbolo[i][j] = chr(ord('a')+int(numsimbolo))
			numsimbolo += .5
	for i in range(1000):
		[f1, c1] = [ int(filas * random()), int(columnas * random())]
		[f2, c2] = [ int(filas * random()), int(columnas * random())]
		tmp = simbolo[f1][c1]
		simbolo[f1][c1] = simbolo[f2][c2]
		simbolo[f2][c2] = tmp
		
def hay_baldosas(baldosas):
	[filas, columnas] = dimension(baldosas)
	for fila in range(filas):
		for columna in range(columnas):
			if baldosas[fila][columna] != None:
				return True
	return False
	
def dibuja_simbolos(simbolo):
	[filas, columnas] = dimension(simbolo)
	for i in range(filas):
		for j in range(columnas):
			create_text(j+.5, i+.5, simbolo[i][j], 18)
			
def dibuja_baldosas(baldosa):
	[filas, columnas] = dimension(simbolo)
	for i in range(filas):
		for j in range(columnas):
			dibuja_baldosa(baldosa,i,j)
			
def dibuja_baldosa(baldosa, f, c):
	baldosa[f][c] = create_filled_rectangule(c, f, c+1, f+1, 'black', 'blue')
	
def borra_baldosa(baldosa, f, c):
	erase(baldosa[f][c])
	baldosa[f][c] = None
	
def pulsacion_raton():
	boton_antes = 0
	boton_ahora = 0
	while not(boton_antes == 1 and boton_ahora == 0):
		boton_antes = boton_ahora
		[boton_ahora, x, y] = mouse_state()
	return [int(y), int(x)]

filas = 4
columnas = 6
windows_coordinates(0,0,columnas,filas)
window_size(columnas*40, filas*40)

simbolo = crea_matriz(filas, columnas)
baldosa = crea_matriz(filas, columnas)
rellena_simbolos(simbolo)
dibuja_simbolos(simbolo)
dibuja_baldosas(simbolo)

jugadas = 0

while hay_baldosas(baldosa):
	while 1:
		[f1, c1] = pulsacion_raton()
		if baldosa[f1][c1] != None:
			borra_baldosa(baldosa, f1, c1)
			break
	while 1:
		[f2, c2] = pulsacion_raton()
		if baldosa[f2][c2] != None:
			borra_baldosa(baldosa, f2, c2)
			break
		sleep(0.5)
		if simbolo[f1][c1] != simbolo[f2][c2]:
			dibuja_baldosa(baldosa,f1,c1)
			dibuja_baldosa(baldosa,f2,c2)
		jugadas += 1
		
print "Lo hicistes en %s jugadas." % jugadas
