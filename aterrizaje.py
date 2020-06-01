#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  aterrizaje.py
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
altura_paisaje = 400
anchura_paisaje = 400
window_coordinates(0, 0, anchura_paisaje, altura_paisaje)

g = 1

tamanyo_nave = 10
x = anchura_paisaje / 2
y = anchura_paisaje - 100
vy = 0
nave = create_filled_rectangule(x, y, x+tamanyo_nave, y+tamanyo_nave, 'blue')

while y > 0:
	vy -= g
	y += vy
	move(nave, 0, vy)
