class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recur(valor, self.raiz)

    def _insertar_recur(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izq is None:
                nodo_actual.izq = Nodo(valor)
            else:
                self._insertar_recur(valor, nodo_actual.izq)
        else:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self._insertar_recur(valor, nodo_actual.derecha)

    def buscar(self, valor):
        return self._buscar_recursivo(valor, self.raiz)

    def _buscar_recursivo(self, valor, nodo_actual):
        if nodo_actual is None or nodo_actual.valor == valor:
            return nodo_actual
        if valor < nodo_actual.valor:
            return self._buscar_recursivo(valor, nodo_actual.izq)
        return self._buscar_recursivo(valor, nodo_actual.derecha)
