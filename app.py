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
                "background-color: rgb(203, 95, 59); color: rgb(204, 204, 204);")  # pone color de deshabilitado

        # cuando se modifica cualquier input llama a la funcion onChange
        self.nombre.textChanged.connect(self.onChange)
        self.apellido.textChanged.connect(self.onChange)
        self.email.textChanged.connect(self.onChange)

    def onChange(self):
        # guardo el boton Ok
        okBtn = self.buttonBox.button(QDialogButtonBox.StandardButton.Ok)

        # si todos los inputs tienen texto se habilita el boton Ok. cambia el color respectivamente
        if self.nombre.text() and self.apellido.text() and self.email.text():
            okBtn.setEnabled(True)
            okBtn.setStyleSheet(
                "background-color:rgb(254, 120, 75); color:white;")
        else:
            okBtn.setEnabled(False)
            okBtn.setStyleSheet(
                "background-color: rgb(203, 95, 59); color: rgb(204, 204, 204);")

    # crea y retorna un Cliente con los datos de los inputs
    def getCliente(self):
        nombre = self.nombre.text()
        apellido = self.apellido.text()
        email = self.email.text()
        return Cliente(nombre, apellido, email)


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("./win.ui", self)

        # asigna los botones de la app a funciones
        self.agregarLibro.clicked.connect(self.onAgregarLibro)
        self.comprar.clicked.connect(self.onComprar)
        self.quitarSeleccion.clicked.connect(self.onQuitarSeleccion)
        self.quitarTodos.clicked.connect(self.onQuitarTodos)

        # deshabilita el boton comprar desde el comienzo y le cambia el color
        self.comprar.setEnabled(False)
        self.comprar.setStyleSheet(
            'background: rgb(25, 146, 69); border-radius:  24; color: white')

        # crea los objetos importantes, en el caso de cliente y compra estan vacíos al comienzo
        # llama a la funcion para ingresar
        self.biblioteca = Biblioteca()
        self.cliente = None
        self.compra = None
        self.ingresar()

        archivo = open('./libros.csv')  # abre el archivo csv
        data = csv.reader(archivo, delimiter=',',
                          quotechar='"')  # este objeto lee csv
        data.__next__()  # salta la primera linea (nombre de los campos)

        # por cada fila da la data, crea un nuevoLibro vacio y dependiendo de si está la columna
        # 14 o no crea un libro fisico o ebook y le pasa los datos de la fila del csv
        for fila in data:
            nuevoLibro = None
            if (not fila[14]):
                nuevoLibro = Fisico(fila[0], fila[1], fila[2], fila[3],
                                    fila[4], fila[5], fila[6], fila[7], fila[8], fila[9], fila[10], fila[11], fila[12])
            else:
                nuevoLibro = Ebook(fila[0], fila[1], fila[2], fila[3],
                                   fila[4], fila[5], fila[6], fila[7], fila[8], fila[9], fila[13], fila[14])
            self.biblioteca.agregarLibro(nuevoLibro)  # guarda libro en biblio
        archivo.close()  # cierra el archivo

        self.actualizarBiblioteca()  # llama a la primera carga de tabla

    def ingresar(self):
        # crea el dialogo login
        loginDialog = LoginDialog()
        # si el boton presionado es ok se ejecuta lo siguiente:
        if loginDialog.exec():
            # trae el cliente generado en el dialogo
            self.cliente = loginDialog.getCliente()
            self.compra = Compra(self.cliente)  # lo agrega a la compra

    def actualizarCompra(self):
        # limpia carrito
        self.carrito.clear()
        # por cada libro en la compra agrega la info a la lista y calcula total
        for libro in self.compra.librosComprados:
            self.carrito.addItem(
                f'{libro.titulo} - {libro.autor} |  ${str(libro.precio)}')
        self.total.setText('$ ' + str(self.compra.calcularTotal()))

        # activa o desactiva el boton y le cambia el color en cada caso
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
        # limpio tabla y me posiciono en el lugar 0 de la tabla
        self.tabla.clear()
        self.tabla.setRowCount(0)
        # por cada libro de la biblio si está disponible (stock) carga la tabla
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
        # habilita el boton comprar
        self.comprar.setEnabled(True)

        # si el cliente no esta ingresado muestra login
        if self.cliente == None:
            self.ingresar()
        else:
            # fila actual de la tabla e id del libro seleccionado en la tabla
            filaActual = self.tabla.currentRow()
            idSeleccionada = self.tabla.item(filaActual, 0).text()

            # chequeo que el libro no esté en el carrito ya
            libroEnCarrito = False
            for libro in self.compra.librosComprados:
                if idSeleccionada == libro.id:
                    libroEnCarrito = True

            # si no esta, busco el libro por id en la biblio y lo agrego a la compra
            if not libroEnCarrito:
                for libro in self.biblioteca.listaLibros:
                    if libro.id == idSeleccionada:
                        self.compra.agregarLibro(libro)
                self.actualizarCompra()  # actualizo compra

    def onQuitarSeleccion(self):
        # si carrito tiene algo llama a la función quitar libro de Compra y actualizarCompra()
        if self.carrito.count():
            self.compra.quitarLibro(self.carrito.currentRow())
            self.actualizarCompra()

    def onQuitarTodos(self):
        # si carrito tiene algo llama a la función quitar todos de Compra y actualizarCompra()
        if self.carrito.count():
            self.compra.quitarTodos()
            self.actualizarCompra()

    def onComprar(self):
        # crea mensaje de confirmacion
        msjConfirmacion = QMessageBox()
        msjConfirmacion.setWindowTitle('Confirmación')
        msjConfirmacion.setText('¿Desea realizar la compra?')
        msjConfirmacion.setIcon(QMessageBox.Icon.Question)
        msjConfirmacion.setStandardButtons(
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        resultado = msjConfirmacion.exec()

        if (resultado == QMessageBox.StandardButton.Yes):

            # fija la fecha actual y agrega la compra a la biblioteca
            self.compra.fijarFecha()
            self.biblioteca.agregarCompra(self.compra)

            # crea el mensaje de éxito
            msjExito = QMessageBox()
            msjExito.setWindowTitle('¡Éxito!')
            msjExito.setText(
                'Compra realizada con éxito.\n\nSu recibo ha sido generado.')
            msjExito.setIcon(QMessageBox.Icon.Information)
            msjExito.setStandardButtons(QMessageBox.StandardButton.Ok)
            msjExito.exec()

            # crea y muestra recibo
            self.recibo = Recibo(self.compra)
            self.recibo.show()

            # Actualizar carrito, biblio y stock
            for libro in self.compra.librosComprados:
                libro.reducirStock()
            self.actualizarBiblioteca()
            self.onQuitarTodos()


class Recibo(QMainWindow):
    # al recibo le paso el objeto compra para que tenga todos los metodos y atributos
    def __init__(self, compra):
        super().__init__()
        uic.loadUi("./recibo.ui", self)
        self.salir.clicked.connect(self.onSalir)  # el boton llama a onSalir
        self.compra = compra  # aca guardo el objeto compra

        # agrego la data del objeto compra para mostrar la info
        self.cliente.setText(str(self.compra.cliente))
        self.total.setText('Total: $' + str(self.compra.calcularTotal()))
        self.fecha.setText(
            'Fecha: ' + self.compra.fecha.strftime("%d/%m/%Y (%H:%M:%S)"))
        for libro in self.compra.librosComprados:
            self.librosLista.addItem(
                f'{libro.titulo} - {libro.autor} |  ${str(libro.precio)}')

    # cierra la ventana
    def onSalir(self):
        self.close()


app = QApplication([])
win = VentanaPrincipal()
win.show()
app.exec()
