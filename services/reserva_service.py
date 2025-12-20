from repositories.reserva_repository import ReservaRepository
from models.reserva import Reserva

class ReservaService:

    def crear_reserva(self, fecha, hora_inicio, hora_fin, usuario_id, sala_id):
        reserva = Reserva(id=None, 
                          fecha=fecha, 
                          hora_inicio=hora_inicio, 
                          hora_fin=hora_fin, 
                          usuario_id=usuario_id, 
                          sala_id=sala_id)
        if self.existe_superposicion(reserva):
            raise Exception("La sala ya está reservada en ese horario.")
        
        ReservaRepository.crear(reserva)

    def existe_superposicion(self, nueva):
        reservas = ReservaRepository.buscar_por_sala_y_fecha(
            nueva.sala_id, nueva.fecha
        )

        for r in reservas:
            if nueva.hora_inicio < r.hora_fin and nueva.hora_fin > r.hora_inicio:
                return True
        return False

    