#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  matrices.py
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
def matriz_nula(file, columnas):
	M = []
	for i in range(fila):
		M.append([0] * columnas)
	return M
	
def lee_matriz(filas, columnas):
	M = matriz_nula(filas, columnas)
	for i in range(filas):
		for j in range(columnas):
			M[i][j] = float(raw_input('Introduce el componente (%d,%d): ' % (i, j)))
	return M
	
def dimension(M):
	return [len(M), len(M[0])]

def suma(A, B):
	if dimension(A) != dimension(B):
		return None
	else:
		[m, n] = dimension(A)
		C = matriz_nula(m, n)
		for i in range(m):
			for j in range(n):
				C[i][j] = A[i][j] + B[i][j]
		return C
		

