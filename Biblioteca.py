class Biblioteca():
    def __init__(self):
        self.listaLibros = []
        self.listaCompras = []

    def agregarLibro(self, libro):
        self.listaLibros.append(libro)

    def eliminarLibro(self, id):
        for libro in self.listaLibros:
            if libro.id == id:
                self.listaLibros.remove(libro)

    def agregarCompra(self, compra):
        self.listaCompras.append(compra)

    def eliminarCompra(self, id):
        for libro in self.listaLibros:
            if libro.id == id:
                print(libro)
                self.listaLibros.remove(libro)

    def __str__(self):
        return None
