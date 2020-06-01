#!/usr/bin/env python2.7
#-*- coding:utf-8 -*-

print "hola mundo"


#cadenas de textos

print "hola \"mundo\""

suma = 8 + 8

print suma

print "hola " + " mundo"

#operacines aritmeticas

print 5*2

print 5+2-5*4/2%4

print 5 > 2

print 5 < 2

print 5 == 2

print 16/4*2

print 16/(4*2)

#variables

var = "esta es una variable"

print var

numero1 = 3.14

numero2 = 7

resultado = numero1*numero2
print "El resultad es ", resultado
print "El resultado es %d" % resultado
print "El resultado es %f" % resultado
print "El resultado es %0.2f" % resultado

#funciones

def saludo(nombre):
    print "hola"
    print nombre
print "Inicio del programa"

saludo("yorlys")

print "Termino del programa"

#entrada por teclado

print "Hola, como te llamas"
nombre = raw_input()
print "Hola ", nombre, " mucho gusto"

print "Dame un numero"
numero = int(raw_input())
print "Dame otro numero"
numero2 = int(raw_input())
resultado = numero + numero2
print "La suma de los numeros es: ", resultado

#impresiones formateo y utf-8

nombre = "Jorge"
edad = 23
print "Hola me llamo ", nombre, " y tengo ", edad, " años"

print "Hola me llamo %s y tengo %d años" %(nombre,edad)

#Modulos
import math

print "Dame un numero"
numero = float(raw_input())
factorial = math.factorial(math.floor(numero))
logaritmo = math.log1p(numero)

print "El logaritmo de %f es %f y su factorial redondeado hacia a abajo es %d" %(numero,logaritmo,factorial)

#condicionales

if(TRUE):
    print("La condicion es verdadera")
print "Termino del programa"
