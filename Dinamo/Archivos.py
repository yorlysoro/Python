import re
f = open("pila.py", "r")
lines = f.read()
print(lines)
search = re.search('class', lines)
print(search.group(0))
f.close()


f2 = open("text.txt", "a+")
f2.write(lines)
f2.close()

f2 = open("text.txt","r")

lines2 = f2.read()

print(lines2)
f2.close()
