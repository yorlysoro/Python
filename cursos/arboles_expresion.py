def tomaToken(listaToken, esperado):
    if listaToken[0] == esperado:
        listaToken[0:1] = []
        return 1
    else:
        return 0
def obtineProducto(listaToken):
    a = obtieneNumero(listaToken)
    if tomaToken(listaToken, '*'):
        b = obtieneProducto(listaToken)
        return Arbol('*', a, b)
    else:
        return a
def obtieneSuma(listaToken):
    a = obtieneProducto(listaToken)
    if tomaToken(listaToken, '+'):
        b = obtieneSuma(listaToken)
        return Arbol('+', a, b)
    else:
        return a

def obtieneNumero(listaToken):
    if tomaToken(listaToken, '('):
        x = obtieneSuma(listaToken)
        tomaToken(listaToken, ')')
        return x
    else:
        x = listaToken[0]
        if type(x) != type(0): return None
        listaToken[0:1] = []
        return Arbol(x, None, None)

    
