#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main_lista_simplemente_enlazada.py
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
from Lista_Simplemente_Enlazada import ListaSimpleEnlazada

lista = ListaSimpleEnlazada()

lista.agregar_ultimo(12)
lista.agregar_ultimo(2)
lista.agregar_ultimo(25)
lista.agregar_ultimo(19)
lista.agregar_ultimo(30)

lista.recorrido()
print ("***************")
print (lista.primero.dato)
print (lista.ultimo.dato)
print (lista.ultimo.siguiente)

lista.eliminar_ultimo()
print ("***************")
lista.agregar_ultimo(40)
lista.recorrido()
print("****************")
lista.agregar_inicio(10)
lista.agregar_inicio(14)
lista.recorrido()
print("****************")
lista.eliminar_inicio()
lista.recorrido()
lista.eliminar_ultimo()
lista.eliminar_ultimo()
lista.eliminar_ultimo()
lista.eliminar_ultimo()
lista.eliminar_ultimo()
lista.eliminar_ultimo()
lista.eliminar_ultimo()
