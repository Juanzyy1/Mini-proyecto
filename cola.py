class Cola:
    """
    Cola (FIFO) implementada con lista.
    Notas:
      - encolar: O(1)
      - desencolar: O(n) (por pop(0) en listas).
    """

    def __init__(self):
        self.items = []

    def encolar(self, persona):
        """Añade `persona` al final de la cola."""
        self.items.append(persona)

    def desencolar(self):
        """Elimina y devuelve el primer elemento; devuelve None si está vacía."""
        if not self.esta_vacia():
            return self.items.pop(0)
        return None

    def esta_vacia(self):
        """Devuelve True si la cola no tiene elementos."""
        return len(self.items) == 0

    def tamaño(self):
        """Devuelve el número de elementos en la cola."""
        return len(self.items)

    def mostrar(self):
        """Devuelve una lista con la representación en cadena de cada elemento."""
        return [str(p) for p in self.items]


