#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  vida.py
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
configuracion = [ '......', '..*..', '..*..', '..*..','.....']

filas = len(configuracion)
columnas = len(configuracion[0])

tablero = []
for i in range(filas):
	tablero.append([False] * columnas)
	for j in range(columnas):
		tablero[i][j] = configuracion[i][j] == '*'

for y in range(filas):
	for x in range(filas):
		if tablero[y][x]:
			print '*',
		else:
			print '.',
		print
pulsos = 10
for t in range(pulsos):
	nuevo = []
	for i in range(filas):
		nuevo.append([0]*columnas)
	
	for y in range(filas):
		for x in range(columnas):
			n = 0
			if y > 0 and x > 0 and tablero[y-1][x-1]:
				n +=1
			if x > 0 and tablero[y][x-1]:
				n += 1
			if y < filas-1 and tablero[y+1][x-1]:
				n += 1
			if y > 0 and tablero[y-1][x]:
				n += 1
			if y < filas-1 and > 0 and tablero[y+1][x]:
				n += 1
			if y > 0 and x < columnas-1 and tablero[y-1][x+1]:
				n += 1
			if x < columnas-1 and tablero[y][x+1]:
				n += 1
			if y < filas-1 and x < columnas-1 and tablero[y+1][x+1]:
				n += 1
			if tablero[y][x] and(n == 2 or n == 3):
				nuevo[y][x] = 1
			elif not tablero[y][x] and n == 3:
				nuevo[y][x] = 1
			else:
				nuevo[y][x] = 0
	tablero = nuevo
	
	print "Pulso ", t+1
	for y in range(filas):
		for x in range(columnas):
			if tablero[y][x]:
				print '*',
				
			else:
				print '.',
		print 
		
