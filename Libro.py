class Libro():
    def __init__(self, id, titulo, autor, fecha_pub, cantidad_paginas, editorial, generos, categoria, sinopsis, imagen, precio):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.fecha_pub = fecha_pub
        self.cantidad_paginas = cantidad_paginas
        self.editorial = editorial
        self.generos = generos
        self.categoria = categoria
        self.sinopsis = sinopsis
        self.imagen = imagen
        self.precio = precio

    def estaDisponible(self):
        return True

    def reducirStock(self):
        return None

    def __str__(self):
        return f'ID: {self.id}. Titulo: {self.titulo}. Autor: {self.autor}'


class Fisico(Libro):
    def __init__(self, id, titulo, autor, fecha_pub, cantidad_paginas, editorial, generos, categoria, sinopsis, imagen, tipo_tapa, dimensiones, stock):
        super().__init__(id, titulo, autor, fecha_pub, cantidad_paginas,
                         editorial, generos, categoria, sinopsis, imagen)
        self.tipo_tapa = tipo_tapa
        self.dimensiones = dimensiones
        self.stock = stock

    def estaDisponible(self):
        return self.stock > 0

    def reducirStock(self):
        self.stock -= 1


class Ebook(Libro):
    def __init__(self, id, titulo, autor, fecha_pub, cantidad_paginas, editorial, generos, categoria, sinopsis, imagen, plataforma, formato):
        super().__init__(id, titulo, autor, fecha_pub, cantidad_paginas,
                         editorial, generos, categoria, sinopsis, imagen)
        self.plataforma = plataforma
        self.formato = formato
