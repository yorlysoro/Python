#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  notas.py
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

class Estudiante(record):
	nombre = ''
	grupo = ''
	nota = 0.0
	practica = False
	
def existe_estudiante(lista, nombre):
	for estudiante in lista:
		if nombre == estudiante.nombre:
			return True
	return False
	
def crea_estudinate_por_teclado():
	nombre = raw_input('Nombre: ')
	grupo = raw_input('Grupo (A, B o C): ')
	while grupo not in ['A', 'B', 'C']:
		grupo = raw_input('Grupo (A, B o C: ')
	nota = float(raw_input('Nota de examen: '))
	while nota < 0 or nota > 10:
		nota = float(raw_input('Nota de examen: '))
	entregada = raw_input('Practica entregada (s/n): ')
	while entregada.lower() not in ['s', 'n']:
		entregada = raw_input('Practica entregada (s/n): ')
	practica = entregada.lower() == 's'
	return Estudiante(nombre=nombre, grupo=grupo, nota=nota, practica=practica)
	
def anyade_estudiante(lista, estudiante):
	if not existe_estudiante(lista, estudiante.nombre):
		lista.append(estudiante)
		return True
	else:
		return False
		
def modifica_estudiante(lista, estudiante):
	for i in range(len(lista)):
		if lista[i].nombre == estudiante.nombre:
			lista[i] = estudiante
			return True
	return False
	
def elimina_estudiante(lista, nombre):
	for i in range(len(lista)):
		if lista[i].nombre == nombre:
			del lista[i]
			return True
	return False

def muestra_estudiante(estudiante):
	print 'Nombre:		%s' % estudiante.nombre
	print 'Grupo:		  %s' % estudiante.grupo
	print 'Nota examen: %3.1f' % estudiante.nota
	if estudiante.practica:
		print 'Memoria de practicas entragada'
	else:
		print 'Memoria de practicas no entragada'

def busca_y_muestra_estudiante(lista, nombre):
	for estudiante in lista:
		if estudiante.nombre == nombre:
			muestra_estudiante(estudiante)
			return
	print 'No existe ese estudiante'

def lista_completo(lista):
	for estudiante in lista:
		muestra_estudiante(estudiante)

def listado_de_nombres(lista):
	for estudiante in lista:
		print estudiante.nombre

def menu():
	print '-' * 79
	opcion = 0
	while opcion < 1 or opcion > 7:
		print '1) Dar de alta un nuevo estudiante.'
		print '2) Modificar los datos de un estudinate.'
		print '3) Dar de baja un estudinate.'
		print '4) Mostrar ficha de estudiante.'
		print '5) Mostrar listado completo.'
		print '6) Mostrar listado de nombres.'
		print '7) Salir.'
		opcion = int(raw_input('Escoge opcion: '))
	return opcion


estudiantes = []

opcion = 0
while opcion != 7:
	opcion = menu()
	if opcion == 1:
		estudiante = crea_estudinate_por_teclado()
		if anyade_estudiante(estudiantes, estudiante):
			print 'Estudiante %s dado de alta.' % estudiante.nombre
		else:
			print 'El estudiante %s ya habia sido dado de alta.' % estudiante.nombre
	elif opcion == 2:
		estudiante = crea_estudinate_por_teclado()
		if modifica_estudiante(estudiantes, estudiante):
			print 'Estudiante %s modificado.' % estudiante.nombre
		else:
			print 'No existe el estudiante %s.' % estudiante.nombre
	elif opcion == 3:
		nombre = raw_input('Nombre: ')
		if elimina_estudiante(estudiantes, nombre):
			print 'Estudiante %s eliminado.' % nombre
		else:
			print 'No existe el estudiante %s.' % nombre
	elif opcion == 4:
		nombre = raw_input('Nombre: ')
		busca_y_muestra_estudiante(estudiantes, nombre)
	elif opcion == 5:
		listado_completo(estudiantes)
	elif opcion == 6:
		listado_de_nombres(estudiantes)

print 'Gracias por usar el programa'
