#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Forms.py
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

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['get', 'post'])

def login_view():
	msg = ''
	
	if(request.method == 'POST'):
		usename = request.form["username"]
		passw = request.form["passwd"]
		
		if(username == 'you' and passwd == 'flask'):
			msg = 'Username and password are correct'
		else:
			msg = 'Username or password are incorrect'
	return render_template('form.html', message=msg)

app.run()
