class Cliente():
    def __init__(self, nombre, apellido, email):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email

    def __str__(self):
        return f'Nombre y apellido: {self.nombre} {self.apellido}.\nEmail: {self.email}'
