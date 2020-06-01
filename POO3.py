#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  POO3.py
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

class Nacimiento:
	def __init__(self):
		self.__anio=2000
		self.__mes=1
		self.__dia=1
		
	def setMes(self, mes):
		if mes>0 and mes < 13:
			self.__mes=mes
		else:
			print "Mes invalido"
			
	def getMes(self):
		return self.__mes

class Television:
	def __init__(self, marca):
		self.__marca=marca
		self.encendida=False
	def encederT(self):
		if(self.encendida == False):
			self.encendida = True
		else:
			print "La television esta encendida"
			
	def apagarT(self):
		if(self.encendida == True):
			self.encendida = False
		else:
			print "La television ya esta apagada"
	
	def getMarca(self):
		return self.__marca
		
objeto = Nacimiento()
objeto.setMes(45)
print objeto.getMes()
objeto.setMes(6)
print objeto.getMes()
tele = Television("Samsung")
tele.encederT()
tele.apagarT()
print tele.getMarca()
