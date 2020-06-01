#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  POO2.py
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
class Electrodomesticos:
	def __init__(self,nombre):
		self.nombre = nombre
		self.estado = False
	def encenderE(self):
		if self.estado == False:
			self.estado = True
			print "Se ha encendido " + self.nombre
		else:
			print "El electrodomestico ya estaba encendido"
	def apagarE(self):
		if self.estado == True:
			self.estado = False
			print "Se ha apagado " + self.nombre
		else:
			print "El electrodomestico ya estaba apagado"


class Telefono:
	def llamar(self):
		print "Llamando"
		
	def colgar(self):
		print "Llamada finalizada"


class Celular(Electrodomesticos,Telefono):
	def mandarMensaje(self):
		if self.estado == True:
			print "Mandando mensaje"

class Television(Electrodomesticos):
	def cambiarCanal(self):
		if self.estado == True:
			print "Cambiando de canal"
			
cel = Celular("Celular")
cel.encenderE()
cel.mandarMensaje()
cel.llamar()
cel.colgar()
cel.apagarE()
tel = Television("Television")
tel.encenderE()
tel.cambiarCanal()
tel.apagarE()
