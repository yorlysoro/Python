import shutil
shutil.copyfile('datos.db', 'copia.db')
shutil.move('/build/ejecutables', 'dirinstalacion')

import glob
glob.glob('*.py')

import sys
print sys.argv

import re
re.findall(r'\bq[a-z]*', 'sabes lo que pasa cuando dices que me quieres')
re.sub(r'(\b[a-z]+)\1', r'\1', 'arde la calle al sol de de poniente')