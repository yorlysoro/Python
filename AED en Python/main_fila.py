#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main_fila.py
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

from Fila import Fila_Implementacion

fila = Fila_Implementacion()

print ("La fila esta vacia ", fila.Vacia())
print ("La fila esta llena ", fila.Llena())
print ("Elementos en la fila ", fila.Elementos())
print ("Elemento al frente ", fila.Frente())
print ("Elemento al final ", fila.Final())

fila.Insertar(5)
print ("La fila esta vacia ", fila.Vacia())
print ("La fila esta llena ", fila.Llena())
print ("Elementos en la fila ", fila.Elementos())
print ("Elemento al frente ", fila.Frente())
print ("Elemento al final ", fila.Final())

fila.Insertar(10)
print ("La fila esta vacia ", fila.Vacia())
print ("La fila esta llena ", fila.Llena())
print ("Elementos en la fila ", fila.Elementos())
print ("Elemento al frente ", fila.Frente())
print ("Elemento al final ", fila.Final())

fila.Insertar(15)
print ("La fila esta vacia ", fila.Vacia())
print ("La fila esta llena ", fila.Llena())
print ("Elementos en la fila ", fila.Elementos())
print ("Elemento al frente ", fila.Frente())
print ("Elemento al final ", fila.Final())

fila.Insertar(35)
print ("La fila esta vacia ", fila.Vacia())
print ("La fila esta llena ", fila.Llena())
print ("Elementos en la fila ", fila.Elementos())
print ("Elemento al frente ", fila.Frente())
print ("Elemento al final ", fila.Final())

fila.Insertar(45)
print ("La fila esta vacia ", fila.Vacia())
print ("La fila esta llena ", fila.Llena())
print ("Elementos en la fila ", fila.Elementos())
print ("Elemento al frente ", fila.Frente())
print ("Elemento al final ", fila.Final())

fila.Insertar(25)

fila.Eliminar()
print ("La fila esta vacia ", fila.Vacia())
print ("La fila esta llena ", fila.Llena())
print ("Elementos en la fila ", fila.Elementos())
print ("Elemento al frente ", fila.Frente())
print ("Elemento al final ", fila.Final())

fila.Eliminar()
print ("La fila esta vacia ", fila.Vacia())
print ("La fila esta llena ", fila.Llena())
print ("Elementos en la fila ", fila.Elementos())
print ("Elemento al frente ", fila.Frente())
print ("Elemento al final ", fila.Final())

fila.Eliminar()
fila.Eliminar()
print ("La fila esta vacia ", fila.Vacia())
print ("La fila esta llena ", fila.Llena())
print ("Elementos en la fila ", fila.Elementos())
print ("Elemento al frente ", fila.Frente())
print ("Elemento al final ", fila.Final())
fila.Eliminar()
fila.Eliminar()

