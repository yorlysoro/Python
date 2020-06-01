#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Threads3.py
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
import time
from threading import Thread

class MiHilo(Thread):
	def __init__(self, num):
		Thread.__init__(self)
		self.bignum = num
		
	def run(self):
		for l in range(10):
			for k in range(self.bignum):
				res = 0
				for i in range(self.bignum):
					res += 1
def test():
	num = 1000
	thr1 = MiHilo(num)
	thr1.start()
	thr1.join()
	
if __name__ == '__main__':
	test()
