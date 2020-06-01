#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main_lista_circular.py
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
from Lista_Circular import ListaCircular

lista = ListaCircular()

lista.agregar_final(10)
lista.agregar_final(56)
lista.agregar_final(78)
lista.agregar_final(90)

lista.agregar_inicio(60)
lista.agregar_final(100)

lista.recorrer()

lista.remover_final()

lista.recorrer()

lista.remover_inicio()
lista.recorrer()

print ("Primero: ", lista.primero.dato)
print ("Ultimo: ", lista.ultimo.dato)
print ("Ultimo.siguiente apunta a", lista.ultimo.siguiente.dato)
