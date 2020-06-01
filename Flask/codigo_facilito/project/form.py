#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  form.py
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

from wtforms import Form, StringField, TextField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms import validators
from wtforms import HiddenField
from models import User

def length_honeypot(form, field):
	if len(field.data) > 0:
		raise validators.ValidationError('El campo debe esta vacio.')

class CommentForm(Form):
	username = StringField('Usuario',
	[ validators.length(min=4, max=25, message='Ingrese un username valido!.'),
	validators.Required(message = 'El username es requerido!.')])
	
	email = TextField('Correo Electronico', 
	[validators.Email(message = 'Ingrese un email valido'),
	validators.Required(message = "El correo es requerido!.")])
	
	comment = TextField('Comentario')
	
	honeypot = HiddenField('', [length_honeypot])

class LoginForm(Form):
	username = StringField('username',
	[
		validators.Required(message = "El username es requerido!."),
		validators.length(min = 4 , max=25, message='Ingrese un username valido!.')
	])
	password = PasswordField('Password', [validators.Required(message = 'El password es requerido!.')])


class CreateForm(Form):
	username = TextField('Username',
	[
		validators.Required(message = 'El username es requerido'),
		validators.length(min=4, max=50, message='Ingrese un usename valido')
	])
	email = EmailField('Correo Electronico',
	[
		validators.Required(message = 'El email es requerido!'),
		validators.Email(message='Ingrese un email valido'),
		validators.length(min=4, max=50, message='Ingrese un email valido')
	])
	password = PasswordField('Password', [validators.Required(message='El password es requerido')])

	def validate_username(form, field):
		username = field.data
		user = User.query.filter_by(username = username).first()
		if user is not None:
			raise validators.ValidationError('El usename ya se encuentra registrado!')
