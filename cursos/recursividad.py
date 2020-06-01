def cuenta_atras(n):
    if n == 0:
        print "Despegando!"
    else:
        print n
        cuenta_atras(n-1)

cuenta_atras(3)
