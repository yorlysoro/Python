#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main_pila.py
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
from Pila import Implementacion_Pila

pila = Implementacion_Pila()

print ("La pila esta vacia ", pila.Pila_Vacia())
print ("La pila esta llena ", pila.Pila_Llena())
print ("Elementos en la pila ", pila.Pila_Elementos())
pila.Pila_Cima()

pila.Pila_Push(5)

print ("La pila esta vacia ", pila.Pila_Vacia())
print ("La pila esta llena ", pila.Pila_Llena())
print ("Elementos en la pila ", pila.Pila_Elementos())
pila.Pila_Cima()

pila.Pila_Push(10)

print ("La pila esta vacia ", pila.Pila_Vacia())
print ("La pila esta llena ", pila.Pila_Llena())
print ("Elementos en la pila ", pila.Pila_Elementos())
pila.Pila_Cima()

pila.Pila_Push(30)

print ("La pila esta vacia ", pila.Pila_Vacia())
print ("La pila esta llena ", pila.Pila_Llena())
print ("Elementos en la pila ", pila.Pila_Elementos())
pila.Pila_Cima()

pila.Pila_Push(55)

print ("La pila esta vacia ", pila.Pila_Vacia())
print ("La pila esta llena ", pila.Pila_Llena())
print ("Elementos en la pila ", pila.Pila_Elementos())
pila.Pila_Cima()


pila.Pila_Push(60)

print ("La pila esta vacia ", pila.Pila_Vacia())
print ("La pila esta llena ", pila.Pila_Llena())
print ("Elementos en la pila ", pila.Pila_Elementos())
pila.Pila_Cima()

pila.Pila_Push(80)


pila.Pila_Pop()
pila.Pila_Pop()
pila.Pila_Pop()
pila.Pila_Pop()
pila.Pila_Pop()
pila.Pila_Pop()
