#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  jinja6.py
#  
#  Copyright 2018 yorlysoro <yorlysoro@gmail.com>
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
#Funcion Include 
from jinja2 import Environment, FileSystemLoader

with open('base.txt', 'w') as file:
	file.write("""
	{{ myvar }}
	You wanna hear a dirty joke?
	{% include 'joke.txt' %}
	""".strip())

with open('joke.txt', 'w') as file:
	file.write("""
	A boy fell in a mud puddle. {{ myvar }}
	""".strip())
	
env = Environment()

env.loader = FileSystemLoader('.')

print(env.get_template('base.txt').render(myvar='Ha ha!'))
