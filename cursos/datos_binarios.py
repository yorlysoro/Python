import struct
datos = open('mifich.zip', 'rb').read()

inicio = 0
for i in range(3):
	inicio += 14
	campos = struct.unpack('LLHH', datos[inicio:inicio+16])
	crc32, tam_comp, tam_descomp, tamnombrefich, tam_extra = campos
	
	inicio += 16
	nombrefich = datos[inicio:inicio+tamanombrefich]
	inicio += tamnombrefich
	extra = datos[inicio:inicio+tam_extra]
	print nombrefich, hex(crc32), tam_comp, tam_descomp
	
	inicio += tam_extra + tam_comp