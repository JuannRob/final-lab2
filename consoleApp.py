import csv
from Biblioteca import Biblioteca
from Cliente import Cliente
from Compra import Compra

biblioteca = Biblioteca()
cliente = Cliente('Juan', 'Robledo', 'juannrob@gmail.com')
compra = Compra(cliente)

# Usuario agrega un libro:
#   transaccion.agregarLibro(libro)

# Usuario aprieta comprar:
#   biblioteca.agregarCompra(transaccion)


# Abrir archivo
archivo = open('./data.csv')
# archivo = open('2023-11-06/01-datos2.csv')
filas = csv.reader(archivo, delimiter=',', quotechar='"')

# Leer filas
for fila in filas:
    print(fila[0], ' ', fila[1], ' ', fila[2])

# cerrar archivo
archivo.close()
