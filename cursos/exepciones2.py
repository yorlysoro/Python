import sys

try:
	f = open('mifichero.txt')
	s = f.readline()
	i = int(s.strip())
except IOError, (errno, stderror):
	print "Error de E/S(%s): %s" %(errno, stderror)
except ValueError:
	print "No ha sido posible convertir los datos a entero"
except:
	print "Error no contemplado:", sys.exc_info()[0]
	raise
