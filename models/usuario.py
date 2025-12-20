class Usuario:
    def __init__(self, id, nombre, email, rol):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.rol = rol

    def __str__(self):
        return f"{self.id} - {self.nombre} ({self.email}) [{self.rol}]"
    
    