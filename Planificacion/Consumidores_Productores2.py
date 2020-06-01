#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Consumidores_Productores2.py
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

from threading import Thread, Condition, Semaphore
import time, random

class Productor(Thread):
	def __init__(self, elementos, vacio, condicion, lleno):
		Thread.__init__(self)
		self.elementos = elementos
		self.vacio = vacio
		self.lleno = lleno
		self.condicion = condicion
		
	def run(self):
		while True:
			time.sleep(random.randint(0,100) % 2)
			elemento = random.randint(0,100)
			self.vacio.release()
			self.condicion.acquire()
			print "Productor", elemento
			self.elementos.append(elemento)
			self.condicion.notify()
			self.condicion.release()
			self.lleno.acquire()
		
class Consumidor(Thread):
	def __init__(self, elementos, vacio, condicion, lleno):
		Thread.__init__(self)
		self.elementos = elementos
		self.vacio = vacio
		self.condicion = condicion
		self.lleno = lleno
		
	def run(self):
		while True:
			time.sleep(random.randint(0,100) % 2)
			self.lleno.release()
			self.condicion.acquire()
			elemento = self.elementos.pop()
			print "Consumidor", elemento
			self.condicion.wait()
			self.condicion.release()
			self.vacio.acquire()
		
elementos = []
condicion = Condition()
vacio = Semaphore(10)
lleno = Semaphore(10)

tProductor = Productor(elementos, vacio, condicion, lleno)
tConsumidor = Consumidor(elementos, vacio, condicion, lleno)

tProductor.start()
tConsumidor.start()
time.sleep(30)
tProductor.join()
tConsumidor.join()

