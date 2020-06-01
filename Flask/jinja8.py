#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  jinja8.py
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
#Macros 2
from jinja2 import Environment, FileSystemLoader
with open('formfield2.html', 'w') as file:
	file.write("""
	{% macro input(name) -%}
	<input id='{{ name }}' name='{{ name }}' {% for k,v in kawrgs.items() -%}{{ k }} = '{{ v }}' {% endfor %} ></input>
	{% endmacro %}
	""".strip())
with open('index2.html', 'w') as file:
	file.write("""
	{% from 'formfield2.html' import input %}
	{# use method='post' whenever sendign sensitive data over http #}
	<form method='post' action='.' >
	{{ input('name', type='text') }}
	{{ input('passwd', type='password') }}
	<input type='submit' value='Send'></input>
	</form>
	""".strip())
	
env = Environment()
env.loader = FileSystemLoader('.')
print(env.get_template('index.html').render())
