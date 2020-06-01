#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Nodo_Arbol_Binario.py
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

class Nodo:
	def __init__(self,value=None,parent=None,is_root=False,is_left=False,is_right=False):
		self.value = value
		self.left = None
		self.right = None
		self.parent = parent
		self.is_root = is_root
		self.is_left = is_left
		self.is_right = is_right
