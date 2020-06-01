#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rutas2.py
#  
#  Copyright 2018 yorlysoro <yorlysoro@gmail.com>
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



from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
	return "Cambios."

@app.route('/saluda')
def saluda():
	return 'Otro mensaje'
@app.route('/params/')
@app.route('/params/<name>')
@app.route('/params/<name>/<int:num>')
def params(name = '', num = ''):
	return 'El parametro es: {} {}'.format(name, num)
if __name__ == "__main__":
	app.run(debug = True, port= 8080)
