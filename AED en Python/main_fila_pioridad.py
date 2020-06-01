#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main_fila_pioridad.py
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

from Fila_Prioridad import Fila_Prioridad_Implementacion

filaprioridad = Fila_Prioridad_Implementacion()

filaprioridad.Insertar(45,0)
filaprioridad.Insertar(50,1)
filaprioridad.Insertar(48,0)
filaprioridad.Insertar(59,1)
filaprioridad.Insertar(62,2)
filaprioridad.Insertar(12,2)
filaprioridad.Insertar(14,2)

print (filaprioridad.Eliminar())
print (filaprioridad.Eliminar())
print (filaprioridad.Eliminar())
