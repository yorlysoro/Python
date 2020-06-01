#/usr/bin/env python3
import sys

print("I AM SAM!")
for i in  sys.argv:
	print(i)
argv = sys.argv
print("Son", len(argv),"argumentos")
