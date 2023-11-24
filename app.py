import csv
from Biblioteca import Biblioteca
from Cliente import Cliente
from Compra import Compra
from Libro import Fisico, Ebook
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem, QDialog, QDialogButtonBox
from PyQt6 import uic


class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("./login.ui", self)

        self.buttonBox.button(
            QDialogButtonBox.StandardButton.Ok).setEnabled(False)
        self.buttonBox.button(
            QDialogButtonBox.StandardButton.Ok).setStyleSheet(
                "background-color: rgb(203, 95, 59); color: rgb(204, 204, 204);")

        self.nombre.textChanged.connect(self.onChange)
        self.apellido.textChanged.connect(self.onChange)
        self.email.textChanged.connect(self.onChange)

    def onChange(self):
        okBtn = self.buttonBox.button(QDialogButtonBox.StandardButton.Ok)

        if self.nombre.text() and self.apellido.text() and self.email.text():
            okBtn.setEnabled(True)
            okBtn.setStyleSheet(
                "background-color:rgb(254, 120, 75); color:white;")
        else:
            okBtn.setEnabled(False)
            okBtn.setStyleSheet(
                "background-color: rgb(203, 95, 59); color: rgb(204, 204, 204);")

    def getCliente(self):
        nombre = self.nombre.text()
        apellido = self.apellido.text()
        email = self.email.text()
        return Cliente(nombre, apellido, email)


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./win.ui", self)

        self.agregarLibro.clicked.connect(self.onAgregarLibro)
        self.comprar.clicked.connect(self.onComprar)
        self.quitarSeleccion.clicked.connect(self.onQuitarSeleccion)
        self.quitarTodos.clicked.connect(self.onQuitarTodos)

        self.comprar.setEnabled(False)
        self.comprar.setStyleSheet(
            'background: rgb(25, 146, 69); border-radius:  24; color: white')

        self.biblioteca = Biblioteca()
        self.cliente = None
        self.compra = None
        self.ingresar()

        archivo = open('./libros.csv')
        data = csv.reader(archivo, delimiter=',',
                          quotechar='"')
        data.__next__()  # salta la primera linea

        for fila in data:
            nuevoLibro = None
            if (not fila[14]):
                nuevoLibro = Fisico(fila[0], fila[1], fila[2], fila[3],
                                    fila[4], fila[5], fila[6], fila[7], fila[8], fila[9], fila[10], fila[11], fila[12])
            else:
                nuevoLibro = Ebook(fila[0], fila[1], fila[2], fila[3],
                                   fila[4], fila[5], fila[6], fila[7], fila[8], fila[9], fila[13], fila[14])
            self.biblioteca.agregarLibro(nuevoLibro)
        archivo.close()

        self.actualizarBiblioteca()

    def ingresar(self):
        loginDialog = LoginDialog()
        if loginDialog.exec():
            self.cliente = loginDialog.getCliente()
            self.compra = Compra(self.cliente)
            self.usuario.setText(
                f'Usuario: {self.cliente.nombre} {self.cliente.apellido} ({self.cliente.email})')

    def actualizarCompra(self):
        self.carrito.clear()

        for libro in self.compra.librosComprados:
            self.carrito.addItem(
                f'{libro.titulo} - {libro.autor} |  ${str(libro.precio)}')
        self.total.setText('$ ' + str(self.compra.calcularTotal()))

        if self.carrito.count():
            self.comprar.setEnabled(True)
            self.comprar.setStyleSheet(
                'background: rgb(35, 197, 94); border-radius:  24; color: white')

        else:
            self.comprar.setEnabled(False)
            self.comprar.setStyleSheet(
                'background: rgb(25, 146, 69); border-radius:  24; color: white')
            self.total.setText('Total')

    def actualizarBiblioteca(self):
        self.tabla.clear()

        columnas = ['ID', 'Título', 'Autor', 'Fecha', 'Páginas',
                    'Editorial', 'Género', 'Categoría', 'Sinopsis', 'Formato', 'Precio']
        self.tabla.setHorizontalHeaderLabels(columnas)

        self.tabla.setRowCount(0)

        for libro in self.biblioteca.listaLibros:
            if libro.estaDisponible():
                posicionFila = self.tabla.rowCount()
                self.tabla.insertRow(posicionFila)
                self.tabla.setItem(posicionFila, 0, QTableWidgetItem(libro.id))
                self.tabla.setItem(
                    posicionFila, 1, QTableWidgetItem(libro.titulo))
                self.tabla.setItem(
                    posicionFila, 2, QTableWidgetItem(libro.autor))
                self.tabla.setItem(
                    posicionFila, 3, QTableWidgetItem(libro.fecha_pub))
                self.tabla.setItem(
                    posicionFila, 4, QTableWidgetItem(libro.cantidad_paginas))
                self.tabla.setItem(
                    posicionFila, 5, QTableWidgetItem(libro.editorial))
                self.tabla.setItem(
                    posicionFila, 6, QTableWidgetItem(libro.generos))
                self.tabla.setItem(
                    posicionFila, 7, QTableWidgetItem(libro.categoria))
                self.tabla.setItem(
                    posicionFila, 8, QTableWidgetItem(libro.sinopsis))
                if type(libro).__name__ == 'Fisico':
                    self.tabla.setItem(
                        posicionFila, 9, QTableWidgetItem('Físico'))
                else:
                    self.tabla.setItem(
                        posicionFila, 9, QTableWidgetItem('eBook'))
                self.tabla.setItem(
                    posicionFila, 10, QTableWidgetItem('$ ' + str(libro.precio)))

    def onAgregarLibro(self):
        self.comprar.setEnabled(True)

        if self.cliente == None:
            self.ingresar()
        else:
            filaActual = self.tabla.currentRow()
            idSeleccionada = self.tabla.item(filaActual, 0).text()

            libroEnCarrito = False
            for libro in self.compra.librosComprados:
                if idSeleccionada == libro.id:
                    libroEnCarrito = True

            if not libroEnCarrito:
                for libro in self.biblioteca.listaLibros:
                    if libro.id == idSeleccionada:
                        self.compra.agregarLibro(libro)
                self.actualizarCompra()

    def onQuitarSeleccion(self):
        if self.carrito.count():
            self.compra.quitarLibro(self.carrito.currentRow())
            self.actualizarCompra()

    def onQuitarTodos(self):
        if self.carrito.count():
            self.compra.quitarTodos()
            self.actualizarCompra()

    def onComprar(self):
        msjConfirmacion = QMessageBox()
        msjConfirmacion.setWindowTitle('Confirmación')
        msjConfirmacion.setText('¿Desea realizar la compra?')
        msjConfirmacion.setIcon(QMessageBox.Icon.Question)
        msjConfirmacion.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        resultado = msjConfirmacion.exec()

        if (resultado == QMessageBox.StandardButton.Yes):

            self.compra.fijarFecha()
            self.biblioteca.agregarCompra(self.compra)

            msjExito = QMessageBox()
            msjExito.setWindowTitle('¡Éxito!')
            msjExito.setText(
                'Compra realizada con éxito.\n\nSu recibo ha sido generado.')
            msjExito.setIcon(QMessageBox.Icon.Information)
            msjExito.setStandardButtons(QMessageBox.StandardButton.Ok)
            msjExito.exec()

            self.recibo = Recibo(self.compra)
            self.recibo.show()

            for libro in self.compra.librosComprados:
                libro.reducirStock()
            self.actualizarBiblioteca()
            self.onQuitarTodos()


class Recibo(QMainWindow):
    def __init__(self, compra):
        super().__init__()
        uic.loadUi("./recibo.ui", self)
        self.salir.clicked.connect(self.onSalir)
        self.compra = compra

        self.cliente.setText(str(self.compra.cliente))
        self.total.setText('Total: $' + str(self.compra.calcularTotal()))
        self.fecha.setText(
            'Fecha: ' + self.compra.fecha.strftime("%d/%m/%Y (%H:%M:%S)"))
        for libro in self.compra.librosComprados:
            self.librosLista.addItem(
                f'{libro.titulo} - {libro.autor} |  ${str(libro.precio)}')

    def onSalir(self):
        self.close()


app = QApplication([])
win = VentanaPrincipal()
win.show()
app.exec()
