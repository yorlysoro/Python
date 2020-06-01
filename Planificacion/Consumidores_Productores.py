#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Consumidores_Productores.py
#  
#  Copyright 2017 yorlys <yorlys@debian>
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

from threading import Thread, Condition
import time, random

class Productor(Thread):
	def __init__(self, lista, condicion):
		Thread.__init__(self)
		self.lista = lista
		self.condicion = condicion
		
	def run(self):
		while True:
			lista = random.randint(0,10)
			self.condicion.acquire()
			print "Condicion adquirida por productor"
			self.lista.append(lista)
			print "%d agregado a la lista por Productor" %(lista)
			print 'Condicion notificada por productor' 
			self.condicion.notify()
			print 'Condicion liberarda por consumidor'
			self.condicion.release()
			time.sleep(1)


class Consumidor(Thread):
	def __init__(self, lista, condicion):
		Thread.__init__(self)
		self.lista = lista
		self.condicion = condicion
		
	def run(self):
		while True:
			self.condicion.acquire()
			print 'Condicion adquirida por el consumidor'
			while True:
				if self.lista:
					lista = self.lista.pop()
					print '%d removido de la lista' % (lista)
					break
				print 'Condicion espera por productor'
				self.condicion.wait()
			print 'condicion liberada por consumidor'
			self.condicion.release()
			
lista = []
condicion = Condition()
hilo1 = Productor(lista, condicion)
hilo2 = Consumidor(lista, condicion)
hilo1.start()
hilo2.start()
hilo1.join()
hilo2.join()
