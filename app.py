# Aplicación principal guarda:
#   libros en el carrito
#   usuario actual

from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./win.ui", self)

    # Inicia la app:
    #   biblioteca = Biblioteca([], [])
    #   cliente = Cliente('Pedo', 'Papo', 'juan_k-po@gmail.com')
    #   transaccion = Compra(cliente, '12/12/12')

    # Usuario agrega un libro:
    #   transaccion.agregarLibro(libro)

    # Usuario aprieta comprar:
    #   biblioteca.agregarCompra(transaccion)


app = QApplication([])
win = MiVentana()
win.show()
app.exec()
