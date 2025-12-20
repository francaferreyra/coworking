class Sala:
    def __init__(self, id, nombre, capacidad, descripcion):
        self.id = id
        self.nombre = nombre
        self.capacidad = capacidad
        self.descripcion = descripcion

    def __str__(self):
        return f"{self.id} - {self.nombre} (Capacidad: {self.capacidad})"