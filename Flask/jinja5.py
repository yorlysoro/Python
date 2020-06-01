#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  jinja5.py
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
#Funcion Extender Extends
from jinja2 import Environment, FileSystemLoader
with open('parent.txt', 'w') as file:
	file.write("""
	{% block template %} parent.txt {% endblock %}
	=========
	I am a powerfull psychic and will tell you your past
	
	{#- "past" is the block identifier #}
	{% block past %}
	You had pimples by the age of 12.
	{% endblock %}
	
	Tremble before my power!!!
	""".strip())
	
with open('child.txt', 'w') as file:
	file.write("""
	{% extends "parent.txt" %}
	{# overwriting the block called template from parent.txt #}
	{% block template %} child.txt {% endblock %}
	
	{#- overwriting the block called past from parent.txt #}
	{% block past %}
	You've bought an ebook recently.
	{% endblock %}
	""".strip())
	
	
with open('other.txt', "w") as file:
	file.write("""
	{% extends "child.txt" %}
	{% block template %} other.txt {% endblock %} 
	""".strip())


env = Environment()

env.loader = FileSystemLoader('.')
tmp1 = env.get_template('parent.txt')

print(tmp1.render())
print("")

tmp2 = env.get_template('child.txt')
print(tmp2.render())
print("")

tmp3 = env.get_template('other.txt')
print(tmp3.render())
print("")
