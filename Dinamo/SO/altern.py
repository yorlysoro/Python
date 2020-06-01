#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  altern.py
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
import threading,time
x = 0
turno = 0
def enter_region(pid):
	while(pid != turno):
		print(pid)
def leave_region(pid):
	turno = 1 - pid
def process_A():
	while(1):
		enter_region(0)
		x += 1
		print(".")
		leave_region(0)
def process_B():
	while(1):
		enter_region(1)
		x -= 1
	print(";")
	leave_region(1)

pA = threading.Thread(target=process_A)
pB = threading.Thread(target=process_B)

print("Main Started")
x = 5
turno = 0

pA.start()
pB.start()

time.sleep(10)
print("Main finished!. x is", x)
