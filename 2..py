class Cursor:
    def __init__(self, arbol):
        self.arbol = arbol
        self.actual = arbol.raiz

    def mover_izquierda(self):
        if self.actual and self.actual.izquierda:
            self.actual = self.actual.izquierda

    def mover_derecha(self):
        if self.actual and self.actual.derecha:
            self.actual = self.actual.derecha

    def valor_actual(self):
        return self.actual.valor if self.actual else None

    def reiniciar(self):
        self.actual = self.arbol.raiz
