#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2020 yorlysoro <yorlysoro@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#  
#  You should have received a copy of the GNU Lesser General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from flask import Flask, url_for
app = Flask(__name__)

@app.route('/')
def index():
	return 'Index Page'
	
#@app.route('/welcome')
#def hello():
#	return 'Hello World'
@app.route('/show_name/<name>')
def print_name(name):
	return 'Hello, %s!' % name

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name = None):
	if name is None:
		return 'A horse with no name'
	else:
		return 'A horse named %s' % name

@app.route('/test')
def test():
	func_name, user_name = 'print_name', 'Alex'
	return 'url for "%s" = "%s"' %(func_name, url_for(func_name, name = user_name))
app.run()
