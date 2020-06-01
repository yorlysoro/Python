#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  01.py
#  
#  Copyright 2016 Yorlys Oropeza <yorlys@debian>
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

print "Hola\n";

a = 10;

pi = 3.14;


print a, " hola \n";


cadd = "Hola como estas\n \t hola";


print cadd;

cadc = """
Jaeaskdñam
adkmasmdñasm
ñadkñamsdmasd

	akasdadska
	
	"""
	
print cadc;

print cadd + cadc;


bT = True;

bF = False;

bAnd = True and False;

bOr = True or False;

bNot = not True;

print bAnd;
print bOr;

print bNot;

print float(3);

print

tupla = (2,True, "Hola");

print tupla;

print tupla[1];
a = 2;
d = { 'Clave1': [1,12,13],
		a : True
}

print d[a];

v = 5;
c = 5;

r = c != v;

print r;

edad = 11;

m_edad = 18;

if edad >= m_edad:
	print "Eres mayor de edad";
	if True:
		print "Esto es verdadero";
else:
	print "No eres mayor de edad";
print "Esto es otra cosa";


if edad >= 0 and edad < 18:
	print "Eres niño";
elif edad >= 18 and edad < 27:
	print "Eres un joven";
elif edad >= 27 and edad < 60:
	print "Eres un adulto";
else:
	print "Eres de la tercera edad";
	
while edad <= 20:
	print "Hola";
	edad += 1;
	
lista = ['Elemento 1', 'Elemento 2', 'Elemento 3'];

for cosa in lista:
	print cosa;
	
def mi_funcion(num1, num2):
	print num1 + num2;
	
mi_funcion(1,2);

class Humano:
	def __init__(self,edad):
		self.edad = edad;
		print "Soy un nuevo objeto";
		
	def hablar(self,mensaje):
		print mensaje;
pedro = Humano(26);

raul = Humano(25);

print "Soy pedro y tengo ", pedro.edad;
print "Soy raul y tengo ", raul.edad;
pedro.hablar('Hola');

raul.hablar('Hola,pedro!');


class IngSistemas(Humano):
	def programar(self, lenguaje):
		print "Voy a programar en ", lenguaje

class LicDerecho:
	def estudiaCaso(self,de):
		print "Debo estudiar el caso de ", de

class estudioso(IngSistemas,LicDerecho):
	pass
	
s = "hola mundo"

print len(s) 

print s.count("o",0,3)

print s.upper()

print s.lower()

print s.replace('o', 'x', 1)
print s.split('a')

print s.find('a')

t = ("H", "o", "l", "a")
s = ";"

print s.join(t)

print type(s.join(t))

lista = [1, "Dos", 3]

buscar = 1

print buscar in lista

print lista.index(buscar)

if buscar in lista:
	print lista.index(buscar)
else:
	print "No esta el elemento"
	
print lista
lista.append("Nuevo elemento")

print lista

print lista.count(3)

print lista

lista.insert(2,"Nuevo")

print lista


print lista

iterable = "Cadena"

lista.extend(iterable)

print lista

print lista

print lista.pop(2)

print lista

print lista 

lista.remove(3)

print lista


print lista
lista.reverse()
print lista


diccionario = {
	
	"redes_sociales" : ['Twitter', 'Facebook', 'Linkedin'],
	3 : 'Tres',
	'Hola' : "Mundo"
}

print diccionario.has_key("Hola")

print diccionario.items()

print diccionario.keys()

print diccionario.values()

print diccionario
print diccionario.pop(3)
print diccionario

print diccionario
del diccionario['Hola']
print diccionario

print diccionario
diccionario.clear()

diccionario['Nuevo'] = "Valor"
print diccionario


print diccionario

diccionario_2 = diccionario.copy()
print diccionario_2

class Prueba(object):
	def __init__(self):
		self.__privado = "Soy privado"
		self.privado = "Soy publico"
		
	def __metodoPrivado(self):
		return "Soy privado"
		
	def metodoPublico(self):
		print "Soy publico"
		
	def getPrivado(self):
		return self.__privado
		
	def setPrivado(sefl,valor):
		self.__privado = self.__metodoPrivado()
		
obj = Prueba()

#obj.setPrivado("Tengo nuevo valor")
print obj.getPrivado()

