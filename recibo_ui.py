# Form implementation generated from reading ui file 'd:\Clases\Uni\1ero\Lab_2\Final\final-lab2\recibo.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(511, 489)
        MainWindow.setStyleSheet("background-color:rgb(250, 250, 250);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cliente = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Volkswagen-Serial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cliente.setFont(font)
        self.cliente.setObjectName("cliente")
        self.verticalLayout_2.addWidget(self.cliente)
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Volkswagen-Serial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5, 0, QtCore.Qt.AlignmentFlag.AlignBottom)
        self.librosLista = QtWidgets.QListWidget(parent=self.centralwidget)
        self.librosLista.setStyleSheet("border-radius: 24;background-color:rgb(255,255,255)")
        self.librosLista.setObjectName("librosLista")
        self.verticalLayout_2.addWidget(self.librosLista)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.fecha = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Volkswagen-Serial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.fecha.setFont(font)
        self.fecha.setObjectName("fecha")
        self.verticalLayout_2.addWidget(self.fecha)
        self.total = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Volkswagen-Serial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.total.setFont(font)
        self.total.setObjectName("total")
        self.verticalLayout_2.addWidget(self.total)
        self.salir = QtWidgets.QPushButton(parent=self.centralwidget)
        self.salir.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.salir.setFont(font)
        self.salir.setObjectName("salir")
        self.verticalLayout_2.addWidget(self.salir, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 3)
        self.verticalLayout_2.setStretch(4, 1)
        self.verticalLayout_2.setStretch(5, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Recibo"))
        self.cliente.setText(_translate("MainWindow", "Cliente:"))
        self.label_5.setText(_translate("MainWindow", "Libros:"))
        self.fecha.setText(_translate("MainWindow", "Fecha:"))
        self.total.setText(_translate("MainWindow", "Total:"))
        self.salir.setText(_translate("MainWindow", "Salir"))
