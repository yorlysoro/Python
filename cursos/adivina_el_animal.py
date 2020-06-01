def animal():
    raiz = Arbol("pajaro")

    while 1:
        print
        if not si("Estas pensando en un animal?"): break
        arbol = raiz
        while arbol.tomaIzquierda() != None:
            indicador = arbol.tomaCarga() + "? "
            if si(indicador):
                arbol = arbol.tomaDerecha()
            else:
                arbol = arbol.tomaIzquierda()

            adivina = arbol.tomaCarga()
            indicador = "Es un " + adivina +"? "
            if si(indicador):
                print "Soy el mas grande!"
                continue
            indicador = "Como se llama el animal?"
            animal = raw_input(indicador)
            indicador = "Que pregunta distiguira a un %s de un %s?"
            pregunta = raw_input(indicador % (animal,adivina))

            arbol.ponCarga(pregunta)
            indicador = "Si el animal fuera un %s, cual seria la respuesta?"
            if si(indicador % animal):
                arbol.ponIzquierda(Arbol(adivina))
                arbol.ponDerecha(Arbol(animal))
            else:
                arbol.ponIzquierda(Arbol(animal))
                arbol.ponDerecha(Arbol(adivina))
        def si(preg):
            from string import lower
            resp = lower(raw_imput(preg))
            return (resp[0:1] == 's')
        
