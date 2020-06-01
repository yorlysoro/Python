#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main_arbol_binario.py
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

from Arbol_Binario import Arbol_Binario_Busqueda

tree = Arbol_Binario_Busqueda()

tree.add(8)
tree.add(12)
tree.add(14)
tree.add(2)
tree.add(4)
print("*" * 25)
tree.show_in_order(tree.root)
print("*" * 25)
tree.show_pos_order(tree.root)
print("*" * 25)
tree.show_pre_order(tree.root)

print("*" * 25)
print(tree.search(tree.root,4).is_right)
