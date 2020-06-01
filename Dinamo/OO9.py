class AudioFile:
	def __init__(self, filename):
		if not filename.endswith(self.ext):
			raise Exception("Invalid file format")
		self.filename = filename
		
class MP3File(AudioFile):
	ext = "mp3"
	def play(self):
		print("Palying {} as mp3", format(self.filename))
class WavFile(AudioFile):
	ext = "wav"
	def play(self):
		print("Playing {} as wav", format(self.filename))
class OggFile(AudioFile):
	ext = "ogg"
	def play(self):
		print("Playin {} as ogg", format(self.filename))
ogg = OggFile("MyFile.ogg")
ogg.play()
mp3 = MP3File("File.ogg")
