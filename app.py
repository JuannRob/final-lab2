# Aplicación principal guarda:
#   usuario actual
from Biblioteca import Biblioteca
from Cliente import Cliente
from Compra import Compra
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6 import uic


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        # uic.loadUi("./win.ui", self)
        self.setGeometry(200, 200, 700, 399)
        self.setWindowTitle("prueba")
        label = QLabel(self)
        label.resize(300, 399)
        pixmap = QPixmap('perrit.jpg')
        pixmap2 = pixmap.scaled(300, 399)
        label.setPixmap(pixmap2)

    # biblioteca = Biblioteca()
    # cliente = Cliente('Juan', 'Robledo', 'juannrob@gmail.com')
    # compra = Compra(cliente)

    # Usuario agrega un libro:
    #   transaccion.agregarLibro(libro)

    # Usuario aprieta comprar:
    #   biblioteca.agregarCompra(transaccion)


app = QApplication([])
win = MiVentana()
win.show()
app.exec()
