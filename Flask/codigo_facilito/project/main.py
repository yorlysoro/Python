#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
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
import form
from flask import request
from flask_wtf import CsrfProtect
from flask import make_response
from flask import session, redirect, url_for
from flask import flash
from flask import copy_current_request_context
import json
from flask import g
from config import DevelopmentConfig
from models import db, User, Comment
from helper import date_format
from flask_mail import Mail,Message
import threading

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
crsf = CsrfProtect()
mail = Mail()

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404
	
@app.before_request
def before_request():
	if 'username' not in session and request.endpoint in ['comment']:
		return redirect(url_for('login'))
	elif 'username' in session and request.endpoint in ['login', 'create']:
		return redirect(url_for('index'))
	
@app.after_request
def after_request(response):
	return response
	
@app.route('/', methods = ['GET', 'POST'])
def index():
	title = "Index"
	if 'username' in session:
		username = session['username']
		print(username)
	return render_template('index.html', title=title)

@app.route('/login', methods = ['GET', 'POST'])
def login():
	login_form = form.LoginForm(request.form)
	title = "Login"
	if(request.method == 'POST' and login_form.validate()):
		username = login_form.username.data
		password = login_form.password.data
		user = User.query.filter_by(username = username).first()
		if user is not None and user.verify_password(password):
			print("login")
			success_message = "Bienvenido {}".format(username)
			flash(success_message)
			session['username'] = username
			return redirect(url_for('index'))
		else:
			error_message = 'Usuario o contraseña no validos!'
			flash(error_message)
		session['username'] = login_form.username.data
		
	return render_template('login.html', title = title, form = login_form)

@app.route('/logout')
def logout():
	if 'username' in session:
		session.pop('username')
	return redirect(url_for('login'))
	
@app.route('/cookie')
def cookie():
	title = "Cookie"
	response = make_response(render_template('cookie.html', title = title))
	response.set_cookie('custome_cookie', 'Yorlys')
	return response

@app.route('/comment', methods = ['GET', 'POST'])
def comment():
	comment_form = form.CommentForm(request.form)
	if request.method == "POST" and comment_form.validate():
		print("Comentario creado!!")
		user_id = session['user_id']
		comment = Comment(user_id = user_id , text = comment_form.comment.data)
		db.session.add(comment)
		db.session.commit()
		success_message = 'Nuevo comentario creado!'
		flash(success_message)
	title = "Curso Flask"
	return render_template('comment.html', title=title, form = comment_form)
	
@app.route('/ajax-login', methods = ['POST'])
def ajax_login():
	username = request.form['username']
	response = { 'status' : 200, 'username' : username, 'id': 1}
	return json.dumps(response)
	

def send_mail(user_email, username):
	msg = Message('Gracias por tu registro!', sender = app.config['MAIL_USERNAME'], recipie = [user.email])
	msg.html = render_template('email.html', username = username)
	mail.send(msg)

@app.route('/create', methods = ['GET', 'POST'])
def create():
	create_form = form.CreateForm(request.form)
	if request.method == 'POST' and create_form.validate():
		user = User( create_form.username.data,
					create_form.password.data,
					create_form.email.data)
		success_message = 'Usuario registrado en la base de datos'
		db.session.add(user)
		db.session.commit()
		@copy_current_request_context
		def send_message(email, username):
			send_mail(email, username)
		sender = threading.Thread(name='mail_sender', target= send_mail, args = (user.email, user.username))
		sender.start()
		flash(success_message)
	return render_template('create.html', form = create_form)

@app.route('reviews/', methods=['GET'])
@app.route('reviews/<int:page>', methods=['GET'])
def reviews(page = 1):
	per_page = 3
	comment_list = Comment.query.join(User).add_columns(User.username, Comment.text, Comment.created_date ).paginate(page,per_page,False)
	
	
	return render_template('reviews.html', comments = comment_list, date_format = date_format)



if __name__ == '__main__':
	crsf.init_app(app)
	db.init_app(app)
	mail.init_app(app)
	with app.app_context():
		db.create_all()
	app.run()
