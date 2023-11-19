# Aplicación principal guarda:
#   usuario actual
import csv
from Biblioteca import Biblioteca
from Cliente import Cliente
from Compra import Compra
from Libro import Fisico, Ebook
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem, QDialog
from PyQt6 import uic


class LoginDialog(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("./dialog.ui", self)

    def getCliente(self):
        apellido = self.apellido.text()
        nombre = self.nombre.text()
        email = self.email.text()
        return Cliente(nombre, apellido, email)


class MiVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./win.ui", self)
        self.agregarLibro.clicked.connect(self.onAgregarLibro)
        self.comprar.clicked.connect(self.onComprar)

        usuarioNuevo = None
        self.biblioteca = Biblioteca()
        loginDialog = LoginDialog()
        if (loginDialog.exec()):
            usuarioNuevo = loginDialog.getCliente()
        self.cliente = usuarioNuevo  # creo cliente
        self.compra = Compra(self.cliente)  # creo compra con cliente agregado

        archivo = open('./libros.csv')
        data = csv.reader(archivo, delimiter=',', quotechar='"')
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

        for libro in self.biblioteca.listaLibros:
            posicionFila = self.tabla.rowCount()
            self.tabla.insertRow(posicionFila)
            self.tabla.setItem(posicionFila, 0, QTableWidgetItem(libro.id))
            self.tabla.setItem(posicionFila, 1, QTableWidgetItem(libro.titulo))
            self.tabla.setItem(posicionFila, 2, QTableWidgetItem(libro.autor))
            self.tabla.setItem(
                posicionFila, 3, QTableWidgetItem(libro.fecha_pub))
            self.tabla.setItem(
                posicionFila, 4, QTableWidgetItem(libro.cantidad_paginas))
            self.tabla.setItem(
                posicionFila, 5, QTableWidgetItem(libro.editorial))
            self.tabla.setItem(
                posicionFila, 6, QTableWidgetItem(str(libro.precio)))

    def actualizarCompra(self):
        self.carrito.clear()
        for libro in self.compra.librosComprados:
            self.carrito.addItem(f'{libro.titulo} - {libro.autor}')
        self.total.setText('$ ' + str(self.compra.calcularTotal()))

    def onAgregarLibro(self):
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

    def onComprar(self):
        self.compra.fijarFecha()
        self.biblioteca.agregarCompra(self.compra)

        msjConfirmacion = QMessageBox()
        msjConfirmacion.setWindowTitle('Confirmación')
        msjConfirmacion.setText('¿Desea realizar la compra?')
        msjConfirmacion.setIcon(QMessageBox.Icon.Question)
        msjConfirmacion.setStandardButtons(
            QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        resultado = msjConfirmacion.exec()
        if (resultado == QMessageBox.StandardButton.Ok):
            msjExito = QMessageBox()
            msjExito.setWindowTitle('Éxito!')
            msjExito.setText(
                'Compra realizada con éxito.\n\nSu recibo ha sido generado.')
            msjExito.setIcon(QMessageBox.Icon.Information)
            msjExito.setStandardButtons(QMessageBox.StandardButton.Ok)
            msjExito.exec()
            resumen = f'**********************************\n\nNombre y Apellido: {self.cliente.nombre} {self.cliente.apellido}\nLibros:\n'
            for libro in self.compra.librosComprados:
                resumen += f'       * {libro.titulo} - {libro.autor}\n'
            resumen += f'Fecha: {self.compra.fecha.strftime("%d/%m/%Y (%H:%M:%S)")}\nTotal: $ {str(self.compra.calcularTotal())}\n\n**********************************'
            with open('recibo.txt', 'w') as f:
                f.write(resumen)
            app.quit()


app = QApplication([])
win = MiVentana()
win.show()
app.exec()
