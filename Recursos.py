import weakref
class Foo(object): pass

root = Foo()
child1 = weakref.proxy(root)
child2 = weakref.ref(root)

child1.attr = child1
print child2().attr
del root

print child2()
try:	print child1.attr
except ReferenceError, err: print err
