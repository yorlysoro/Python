#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  legible.py
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
print 'Programa para el calculo del perimetro y el area de un recangulo.'

altura = float(raw_input('Dame la altura (en metro): '))
anchura = float(raw_input('Dame la anchura (en metros): '))

area = altura * anchura
perimetro = 2 * altura + 2 * anchura

print 'El perimetro es de %6.2f metros.' % perimetro

print 'El area es de %6.2f metros cuadrados.' % area

