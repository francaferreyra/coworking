class Reserva:
    def __init__(self, id, sala_id, usuario_id, fecha, hora_inicio, hora_fin):
        self.id = id
        self.sala_id = sala_id
        self.usuario_id = usuario_id
        self.fecha = fecha
        self.hora_inicio = hora_inicio
        self.hora_fin = hora_fin

    def __str__(self):
        return f"Reserva {self.id} - Sala {self.sala_id} por {self.usuario} el {self.fecha} de {self.hora_inicio} a {self.hora_fin}"