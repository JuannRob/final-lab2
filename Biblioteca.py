class Biblioteca():
    def __init__(self):
        self.listaLibros = []
        self.listaCompras = []

    def agregarLibro(self, libro):
        self.listaLibros.append(libro)

    def eliminarLibro(self, id):
        return None

    def agregarCompra(self, compra):
        self.listaCompras.append(compra)

    def eliminarCompra(self, id):
        return None

    def __str__(self):
        return None
