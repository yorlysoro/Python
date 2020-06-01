#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  jinja4.py
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
#Funciones
from jinja2 import Template

t = Template("{{ func() }}")

print(t.render(func=lambda: 10))

t = Template("{{ func(x) }}")

print(t.render(func=lambda v: v, x='20'))

t = Template("{{ func(v=30) }}")

print(t.render(func= lambda v: v))

#Operadores Matemticos

print(Template("{{ 3 + 3 }}").render())
print(Template("{{ 3 - 3 }}").render())
print(Template("{{ 3 * 3 }}").render())
print(Template("{{ 3 / 3 }}").render())


#Listas y Diccionarios

print(Template("{{ my_list[0] }}").render(my_list=[1,2,3]))
print(Template("{{ my_list['foo'] }}").render(my_list={ 'foo': 'bar'}))
print(Template("{{ my_list.foo }}").render(my_list={ 'foo': 'bar'}))
