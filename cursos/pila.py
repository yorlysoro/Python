class Pila:
    def __init__(self):
        self.elementos = []

    def push(self, elemento):
        self.elementos.append(elemento)
    def pop(self):
        return self.elementos.pop()
    def isEmpty(self):
        return (self.elementos == [])
    def evalPostfijo(expr):
        import re
        listaTokens = re.split("([^0-9])", expr)
        pila = Pila()
        for token in listaTokens:
            if token == '' or token == '':
                continue
            if token == '+':
                suma = pila.pop() + pila.pop()
                pila.push(suma)
            elif token == '*':
                producto = pila.pop() * pila.pop()
                pila.push(producto)
            else:
                pila.push(int(token))
        return pila.pop()
