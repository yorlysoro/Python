#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Threads2.py
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
import thread

def myfunction(string, sleeptime, lock, *args):
	while True:
		#obtenemos permiso para acceder a la session critica
		lock.acquire()
		#tras adquirir el lock(), suspendemeos el hilo
		time.sleep(sleeptime)
		#aqui vendria la SC
		print string
		#soltamos el Lock para que entre el otro hilo
		lock.release()
		
		time.sleep(sleeptime)
		
if __name__ == '__main__':
	lock = thread.allocate_lock()
	thread.start_new_thread(myfunction, ("Thread No:1", 2, lock))
	thread.start_new_thread(myfunction, ("Thread No:2", 2, lock))
	while True: pass
