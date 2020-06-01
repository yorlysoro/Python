#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  jinja7.py
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
#Macros
from jinja2 import Environment, FileSystemLoader
with open('formfield.html', 'w') as file:
	file.write("""
	{% macro input(name, value='', label='') %}
	{% if label %}
	<label for='{{ name }}'> {{ label }} < /label>
	{% endif %}
	<input id='{{ name }}' name='{{ name }}' value='{{ name }}'> </input>
	{% endmacro %}
	""".strip())
	
with open('index.html', 'w') as file:
	file.write("""
	{% from 'formfield.html' import input %}
	< input type='submit' value='Send'> </input>
	</form>
	""".strip())
	
env = Environment()
env.loader = FileSystemLoader('.')
print(env.get_template('index.html').render())
