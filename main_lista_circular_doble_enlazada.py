#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main_lista_circular_doble_enlazada.py
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
#  
from Lista_Circular_Doble_Enlazada import ListaCircularDobleEnlazada

lista = ListaCircularDobleEnlazada()

lista.agregar_inicio(12)
lista.agregar_inicio(45)
lista.agregar_inicio(18)
lista.agregar_inicio(36)
lista.agregar_inicio(10)

lista.recorrer_inicio_a_fin()

print ("*" * 25)

lista.recorrer_fin_a_inicio()

print ("*" * 25)

print (lista.primero.dato)
print (lista.ultimo.dato)

print ("*" * 25)
print (lista.primero.anterior.dato)
print (lista.ultimo.siguiente.dato)

print ("*" * 25)
lista.eliminar_ultimo()
print (lista.primero.dato)
print (lista.ultimo.dato)

print ("*" * 25)
lista.eliminar_inicio()
print (lista.primero.dato)
print (lista.ultimo.dato)

print ("*" * 25)
print (lista.buscar(10))
