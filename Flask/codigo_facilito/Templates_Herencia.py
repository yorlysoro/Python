#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Templates_Herencia.py
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
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	name = 'Yorlys'
	return render_template('index.html', name=name)
	
@app.route('/client')
def client():
	list_name = ['Test1', 'Test2', 'Test3']
	return render_template('client.html', list_n=list_name)
if __name__ == '__main__':
	app.run(debug = True, port= 8080)
