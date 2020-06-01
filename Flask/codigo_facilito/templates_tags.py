#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  templates_tags.py
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

@app.route('/user/<name>')
def user(name= 'yorlys'):
	age = 19
	my_list = [1,2,3,4]
	return render_template('user.html', nombre=name, age = age, lista= my_list)

if __name__ == "__main__":
	app.run(debug = True, port= 8080)