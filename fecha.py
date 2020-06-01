#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  fecha.py
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
from record import record

class Fecha(record):
	dia = 1
	mes = 1
	anyo = 1
	
def fecha_breve(fecha):
	return '%d/%d/%d' %(fecha.dia, fecha.mes, fecha.anyo)
	
def fecha_en_anyo_bisiesto(fecha):
	if fecha.anyo % 4 != 0:
		return False
	if fecha.anyo % 400 == 0:
		return True
	return fecha.anyo % 100 != 0

def lee_fecha():
	dia = int(raw_input('Dia: '))
	while dia < 1  or dia > 31:
		dia = input(raw_input('Dia: '))
	
	mes = int(raw_input('Mes: '))
	while mes < 1 or mes > 12:
		mes = int(raw_input('Mes: '))
		
	anyo = int(raw_input('Año: '))
	
	return Fecha(dia=dia, mes=mes, anyo=anyo)

def fecha_es_menor(fecha1, fecha2):
	if fecha1.anyo < fecha2.anyo:
		return True
	elif fecha1.anyo > fecha2.anyo:
		return False
	if fecha1.mes < fecha2.mes:
		return True
	elif fecha1.mes > fecha2.mes:
		return False
	return fecha1.dia < fecha2.dia
