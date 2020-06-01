#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Consumidores_Productores3.py
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
from multiprocessing import Process
from threading import Semaphore
import time, random
elementos = []
class Productor(Process):
	def __init__(self, vacio, lleno):
		Process.__init__(self)
		self.vacio = vacio
		self.lleno = lleno
		
	def run(self):
		while True:
			time.sleep(random.randint(0,100) % 2)
			elemento = random.randint(0,100)
			self.vacio.release()
			print "Productor", elemento
			elementos.append(elemento)
			self.lleno.acquire()
		
class Consumidor(Productor, Process):
	def __init__(self, vacio, lleno):
		Process.__init__(self)
		Productor.__init__(self, vacio, lleno)
	def run(self):
		while True:
			time.sleep(random.randint(0,100) % 2)
			self.lleno.release()
			elemento = elementos.pop()
			print "Consumidor", elemento
			self.vacio.acquire()
		
vacio = Semaphore(10)
lleno = Semaphore(10)

pProductor = Productor(vacio, lleno)
pConsumidor = Consumidor(vacio, lleno)

pProductor.start()
pConsumidor.start()
time.sleep(30)
pConsumidor.join()
pProductor.join()
