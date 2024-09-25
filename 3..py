class Cursor:
    
    def inorden(self, nodo):
        if nodo is not None:
            self.inorden(nodo.izquierda)
            print(nodo.valor, end=' ')
            self.inorden(nodo.derecha)

   
    def preorden(self, nodo):
        if nodo is not None:
            print(nodo.valor, end=' ')
            self.preorden(nodo.izquierda)
            self.preorden(nodo.derecha)


    def postorden(self, nodo):
        if nodo is not None:
            self.postorden(nodo.izquierda)
            self.postorden(nodo.derecha)
            print(nodo.valor, end=' ')
