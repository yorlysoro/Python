#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  POO1.py
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
class Television:
	
	def __init__(self, marca):
		self.marca=marca
		self.encendida=False
		
	def encenderT(self):
		if(self.encendida==False):
			self.encendida=True
		else:
			print "La television ya estaba encendida"
		
	def apagarT(self):
		if(self.encendida==True):
			self.encendida=False
		else:
			print "La television ya estaba apagada"
	
	def saberMarca(self):
		print self.marca
		
tele = Television("Samsung")
tele.encenderT()
tele.apagarT()
tele.apagarT()
tele.saberMarca()


