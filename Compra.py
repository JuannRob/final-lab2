import datetime


class Compra():
    def __init__(self, cliente):
        self.id = ''
        self.librosComprados = []
        self.cliente = cliente
        self.fecha = None

    def agregarLibro(self, libro):
        self.librosComprados.append(libro)

    def quitarLibro(self, i):
        self.librosComprados.pop(i)

    def quitarTodos(self):
        self.librosComprados.clear()

    def fijarFecha(self):
        self.fecha = datetime.datetime.now()

    def calcularTotal(self):
        total = 0
        if len(self.librosComprados) > 0:
            for libro in self.librosComprados:
                total += libro.precio
        else:
            total = 0
        return total
