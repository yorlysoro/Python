
def format_string(string, formatter=None):
	'''Format a string using the formatter object, which
is expected to have a format() method that accepts
a string.'''
	class DefaultFormater:
		'''Format a string  in title case'''
		def format(self, string):
			return str(string).title()
	if not formatter:
		formatter = DefaultFormater()
	return formatter.format(string)

hello_string = "hello world, how are you today?"
print(" input: " + hello_string)
print("ouput: "+ format_string(hello_string))
