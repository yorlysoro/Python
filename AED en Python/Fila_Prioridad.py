#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Fila_Prioridad.py
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
from Nodo_Fila_Prioridad import Fila_Prioridad

class Fila_Prioridad_Implementacion:
	def __init__(self):
		self.filaprioridad = Fila_Prioridad()
		for x in range(self.filaprioridad.filaTamano):
			self.filaprioridad.arrayFila.Elemento.insert(x,-1)
	def Vacia(self):
		if self.filaprioridad.Final == -1:
			return True
		else:
			return False
	def Frente(self):
		self.xElemento = Fila_Prioridad()
		señf.xElemento.arrayFila.Elemento.insert(0,-1)
		self.xElemento.arrayFila.Prioridad = -1

		if self.Vacia():
			return self.xElemento.arrayFila.Elemento[0]
		else:
			return self.filaprioridad.arrayFila.Elemento[self.filaprioridad.Frente]
			
	def Final(self):
		xElemento = Fila_Prioridad()
		xElemento.arrayFila.Elemento.insert(0,-1)
		xElemento.arrayFila.Prioridad = -1

		if self.Vacia():
			return xElemento.arrayFila.Elemento[0]
		else:
			return self.filaprioridad.arrayFila.Elemento[self.filaprioridad.Final]

	def Elementos(self):
		if self.Vacia():
			return 0
		else:
			if self.filaprioridad.Final >= self.filaprioridad.Frente:
				return self.filaprioridad.Final - self.filaprioridad.Frente + 1
			else:
				return self.filaprioridad.filaTamano - self.filaprioridad.Frente + self.filaprioridad.Final + 1
	def Llena(self):
		if self.Elementos() == self.filaprioridad.filaTamano:
			return True
		else:
			return False

	def Insertar(self,dato,prioridad):
		xElementoFinal = Fila_Prioridad()
		xElementoFinal.arrayFila.Elemento.insert(0,self.Final)
		xElementoFinal.arrayFila.Prioridad = self.filaprioridad.arrayFila.Prioridad

		if self.Llena():
			print("La fila esta llena no se puede agregar el elemento ", dato)
		else:
			if self.filaprioridad.Final == -1:
				self.filaprioridad.Frente = 0
				self.filaprioridad.Final += 1
				self.filaprioridad.arrayFila.Elemento[self.filaprioridad.Final] = dato
				self.filaprioridad.arrayFila.Prioridad = prioridad
			else:
				if xElementoFinal.arrayFila.Prioridad >= self.filaprioridad.arrayFila.Prioridad:
					if self.filaprioridad.Final + 1 == self.filaprioridad.filaTamano:
						self.filaprioridad.Final = 0
						self.filaprioridad.arrayFila.Elemento[self.filaprioridad.Final] = dato
						self.filaprioridad.arrayFila.Prioridad = Prioridad
					else:
						self.filaprioridad.arrayFila.Elemento[self.filaprioridad.Final] = dato
						self.filaprioridad.arrayFila.Prioridad = prioridad
				else:
					if self.filaprioridad.Final >= self.filaprioridad.Frente:
						for indice in range(self.filaprioridad.Final):
							if xElementoFinal.arrayFila.Prioridad > self.filaprioridad.arrayFila.Prioridad:
								break
						if self.filaprioridad.Final +1 == self.filaprioridad.filaTamano:
							self.filaprioridad.arrayFila.Elemento[0] = self.filaprioridad.arrayFila.Elemento[self.filaprioridad.Final]
							self.filaprioridad.arrayFila.Prioridad = prioridad
						else:
							self.filaprioridad.arrayFila.Elemento[self.filaprioridad.Final+1] = self.filaprioridad.arrayFila.Elemento[self.filaprioridad.Final]
							self.filaprioridad.arrayFila.Prioridad = prioridad
						indice2 = self.filaprioridad.Final
						while indice2 >= indice:
							self.filaprioridad.arrayFila.Elemento[indice2+1] = self.filaprioridad.arrayFila.Elemento[indice2]
							indice2 -= 1
						self.filaprioridad.arrayFila.Elemento[indice] = dato
						self.filaprioridad.arrayFila.Prioridad = prioridad
						if self.filaprioridad.Final + 1 == self.filaprioridad.filaTamano:
							self.filaprioridad.Final = 0
						else:
							self.filaprioridad.Final += 1
					else:
						indice = self.filaprioridad.Frente
						while indice <= self.filaprioridad.filaTamano:
							if xElementoFinal.arrayFila.Prioridad > self.filaprioridad.arrayFila.Prioridad:
								break
						if indice < self.filaprioridad.filaTamano:
							indice2 = self.filaprioridad.Final
							while indice2 != -1:
								self.filaprioridad.arrayFila.Elemento[indice2+1] = self.filaprioridad.arrayFila.Elemento[indice2]
								indice2 -= 1
							self.filaprioridad.arrayFila.Elemento[0] = self.filaprioridad.arrayFila.Elemento[self.filaprioridad.Final]
							self.filaprioridad.arrayFila.Prioridad = prioridad

							indice2 = self.filaprioridad.Final
							while indice2 >= indice:
								self.filaprioridad.arrayFila.Elemento[indice2+1] = self.filaprioridad.arrayFila.Elemento[indice2]
								indice2 -= 1
							self.filaprioridad.arrayFila.Elemento[indice] = dato
							self.filaprioridad.arrayFila.Prioridad = prioridad
							self.filaprioridad.Final += 1
						else:
							for indice in range(self.filaprioridad.Final):
								if xElementoFinal.arrayFila.Prioridad > self.filaprioridad.arrayFila.Prioridad:
									break
							indice2 = self.filaprioridad.Final
							while indice2 >= indice:
								self.filaprioridad.arrayFila.Elemento[indice2+1] = self.filaprioridad.arrayFila.Elemento[indice2]
								indice2 -= 1
							self.filaprioridad.arrayFila.Elemento[indice] = dato
							self.filaprioridad.arrayFila.Prioridad = prioridad
							indice2 = self.filaprioridad.Final-1
							while indice2 >= indice:
								indice2 -= 1
							self.filaprioridad.Final += 1
	def Eliminar(self):
		if self.Vacia():
			print ("La fila esta vacia no es posible sacar elementos")
			return -1
		else:
			result = self.filaprioridad.arrayFila.Elemento[self.filaprioridad.Frente]
			self.filaprioridad.arrayFila.Elemento[self.filaprioridad.Frente] = -1
			if self.filaprioridad.Final == self.filaprioridad.Frente:
				self.filaprioridad.Frente = -1
				self.filaprioridad.Final = -1
			else:
				if self.filaprioridad.Frente+1 == self.filaprioridad.filaTamano:
					self.filaprioridad.Frente = 0
				else:
					self.filaprioridad.Frente += 1
			return result
