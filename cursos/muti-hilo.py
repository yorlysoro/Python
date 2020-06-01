import threading, zipfile

class AsicncZip(threading.Thread):
	def __init__(self, infile, outfile):
		threading.Thread.__init__(self)
		self.infile = infile
		self.outfile = outfile
		
	def run(self):
		f = zipfile.ZipFile(self.outfile, "w", zipfile.ZIP_DEFLATED)
		f.write(self.infile)
		f.close()
		print 'Finished background zip of: ', self.infile
		
segundoplano = AsicncZip('misdatos.txt', 'comprimido.zip'
segundoplano.start()
print "El programa principal sigue ejecutandose en primer plano"

segundoplano.join()
print "El programa principal ha esperado hasta que la tarea en 2 plano he terminado"
