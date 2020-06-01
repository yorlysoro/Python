#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Cola.py
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


class Cola:
	def __init__(self):
		self.cola = []
		self.size = 0
	def empty(self):
		return len(self.cola) == 0

	def push(self,dato):
		self.cola += [dato]
		self.size += 1

	def pop(self):
		if self.empty():
			print ("La cola esta vacia")
		else:
			self.cola = [self.cola[i] for i in range(1,self.size)]
			self.size -= 1
	def show(self):
		n = self.size - 1
		while n > -1:
			print ("[%d]=>  %d"%(n,self.cola[n]))
			n -= 1
	def front(self):
		if self.empty():
			print ("Cola vacia")
		else:
			print ("Primer dato %d"%(self.cola[0]))
