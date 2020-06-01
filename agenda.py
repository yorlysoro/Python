#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  agenda.py
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
class Entrada(record):
	nombre = ''
	apellido = ''
	telefono = ''
	
def lee_entrada():
	nombre = raw_input('Nombre: ')
	apellido = raw_input('Apellido: ');
	telefono = raw_input('Telefono: ')
	return Entrada(nombre=nombre, apellido=apellido, telefono=telefono)
	
class Agenda(record):
	lista = []
	
def cargar_agenda(agenda):
	agenda.lista = []
	f = open('agenda.txt', 'r')
	while 1:
		linea1 = f.readline()
		linea2 = f.readline()
		linea3 = f.readline()
		if linea1 == '':
			break
		entrada = Entrada(nombre=linea1[:-1], apellido=linea2[:-1], telefono=linea3[:-1])
		agenda.lista.append(entrada)
	f.close()

def guardar_agenda(agenda):
	f = open('agenda.txt', 'w')
	for entrada in agenda.lista:
		f.write(entrada.nombre + '\n')
		f.write(entrada.apellido + '\n')
		f.write(entrada.telefono + '\n')
	f.close()

def buscar_telefono(agenda, nombre, apellido):
	for entrada in agenda.lista:
		if entrada.nombre == nombre and entrada.apellido == apellido:
			return entrada.telefono
	return ''
	
def anyadir_entrada(agenda, entrada):
	agenda.lista.append(entrada)
	
def borrar_entrada(agenda, nombre, apellido):
	for i in range(len(agenda.lista)):
		if agenda.lista[i].nombre == nombre and agenda.lista[i].apellido == apellido:
			del agenda.lista[i]
			return

def menu():
	print '1) Añadir entrada'
	print '2) Consultar agenda'
	print '3) Borrar entrada'
	print '4) Salir'	
	opcion = int(raw_input('Seleccione opcion: '))
	while opcion < 1 or opcion > 4:
		opcion = int(raw_input('Seleccione opcion(entre 1 y 4): '))
		return opcion
		
agenda = Agenda()
cargar_agenda(agenda)

opcion = menu()
while opcion != 4:
	if opcion == 1:
		entrada = lee_entrada()
		anyadir_entrada(agenda, entrada)
	elif opcion == 2:
		nombre = raw_input('Nombre')
		apellido = raw_input('Apellido: ')
		telefono = buscar_telefono(agenda
		,nombre, apellido)
		if telefono == '':
			print 'No esta en la agenda'
		else:
			print 'Telefono: ', telefono
	elif opcion == 3:
		nombre = raw_input('Nombre: ')
		apellido = raw_input('Apellido: ')
		borrar_entrada(agenda, nombre, apellido)
	opcion = menu()
	
guardar_agenda(agenda)
