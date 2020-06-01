#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ejercicio4.py
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
LIBRE = 0
OCUPADO = 1
def mostrarMenu():
	print("""
	1) Reservar Asiento
	2) Cancelar Asiento
	3) Mostrar Ocupacion
	4) Salir""")
	resp = int(input())
	return resp

def reservaAsiento(asientos):
	fila = int(input("Escriba la fila del asiento a reservar: "))
	col = int(input("Escriba la columna del asiento a reservar: "))
	if asientos[fila][col] == OCUPADO:
		print("Ese asiento ya esta reservado")
	else:
		asientos[fila][col] = OCUPADO
		print("Reserva realizada")

def cancelarAsiento(asientos):
	fila = int(input("Escriba la fila del asiento a cancelar: "))
	col = int(input("Escriba la columna del asiento a cancelar: "))
	if asientos[fila][col] == LIBRE:
		print("Ese asiento no esta ocupado")
	else:
		asientos[fila][col] = LIBRE
		print("Cancelacion Realizada")
		
def mostrarOcupacion(asientos):
	for i in range(25):
		for j in range(4):
			print("fila", i, "columna", j)
			if asientos[i][j] == LIBRE:
				print("Libre")
			else:
				print("Ocupado")
				
asiento = list([i*0 for i in range(4)] for i in range(25))
entrada = mostrarMenu()
while entrada != 4:
	if entrada == 1:
		reservaAsiento(asiento)
	elif entrada == 2:
		cancelarAsiento(asiento)
	elif entrada == 3:
		mostrarOcupacion(asiento)
	entrada = mostrarMenu()
