import datetime


class Compra():
    def __init__(self, cliente):
        self.id = ''
        self.librosComprados = []
        self.cliente = cliente
        self.fecha = None

    def agregarLibro(self, libro):
        self.librosComprados.append(libro)

    def agregarLibro(self):
        return None

    def setHora(self):
        self.fecha = datetime.datetime.now()

    def calcularTotal(self):
        total = 0
        if len(self.librosComprados) > 0:
            for libro in self.librosComprados:
                total += libro.precio
        return total
