class CursorExtendido(Cursor):
    def valor_maximo(self):
        actual = self.arbol.raiz
        while actual.derecha is not None:
            actual = actual.derecha
        return actual.valor

    def valor_minimo(self):
        actual = self.arbol.raiz
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual.valor
