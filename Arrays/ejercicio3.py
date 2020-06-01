#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ejercicio3.py
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

def mostrarMenu():
	print("""
1) Añadir datos
2) Mostrar total del vendedor
3) Mostrar total de ventas
4) Salir""")
	try:
		resp = int(input("Introduzca una opcion:"))
		return resp
	except ValueError:
		print("Error introduzca solo numeros enteros!!!")
		main()
def mostrarTotal(ventas):
	resp = 0
	for i in range(18):
		for j in range(10):
			resp += ventas[i][j]
	return resp
	
def totalVendedor(ventas, nvendedor):
	resp = 0
	for i in range(10):
		resp += ventas[nvendedor][i]
	return resp
	
def main():
	ventas = list(([i*0 for i in range(10)] for i in range(18)))
	resp = mostrarMenu()
	try:
		while(resp != 4):
			if resp == 1:
				nvend = int(input("Numero de vendedor: "))
				nprod = int(input("Numero de producto: "))
				cantidad = int(input("Cantidad vendida: "))
				ventas[nvend-1][nprod-1] = cantidad
			elif resp == 2:
				nvend = int(input("Numero de vendedor: "))
				print("Ventas total del vendedor ", nvend, totalVendedor(ventas,nvend-1))
			elif resp == 3:
				print("Total de ventas ", mostrarTotal(ventas))
			resp = mostrarMenu()
	except ValueError:
		print("Error el valor tiene que ser entero!!!")
		main()
main()
