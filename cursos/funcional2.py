def saludar(lang):
	def saludar_es():
		print "Hola"
		
	def saludar_fr():
		print "Salut"
	
	def saludar_en():
		print "Hi"
		
	lang_func = { "es": saludar_es, "en": saludar_en, "fr": saludar_fr}
	
	return lang_func[lang]
	
f = saludar("es")
f()
