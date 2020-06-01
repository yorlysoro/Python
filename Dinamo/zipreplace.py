from zipprocessor import ZipProcessor
import sys
import os


class ZipReplace:
	def __init__(self, search_string, replace_string):
		self.search_string = search_string
		self.replace_string = replace_string
	def process(self, zipprocessor):
		"""perform a search and replace on all file in the temporary directory..."""
		for filename in os.listdir(zipprocessor.temp_directory):
			with open(zipprocessor._full_filename(filename) ) as file:
				contens = file.read()
			contens = contens.replace(self.search_string, self.replace_string)
			with open(zipprocessor._full_filename(filename), "w") as file:
				file.write(contens)
if __name__ == "__main__":
	zipreplace = ZipReplace(*sys.argv[2:4])
	ZipProcessor(sys.argv[1], zipreplace).process_zip()
