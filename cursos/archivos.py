#!/usr/bin/env python2
from sys import argv

script, filename = argv

print "Creando el archivo %r" %filename

file = open(filename,'w')
file.write("esta archivo fue creado a travez de python")
file.close()

print "Terminado"
