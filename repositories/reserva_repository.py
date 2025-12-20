from database.connection import get_connection
from models.reserva import Reserva

class ReservaRepository:

    @staticmethod
    def crear(reserva):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO reservas (fecha, hora_inicio, hora_fin, usuario_id, sala_id) VALUES (?, ?, ?, ?, ?)",
            (reserva.fecha, 
             reserva.hora_inicio, 
             reserva.hora_fin, 
             reserva.usuario_id, 
             reserva.sala_id)            
        )

        conn.commit()
        conn.close()

    @staticmethod
    def buscar_por_sala_y_fecha(sala_id, fecha):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM reservas WHERE sala_id = ? AND fecha = ?",
            (sala_id, fecha)
        )
        rows = cursor.fetchall()
        conn.close()

        return [Reserva(*row) for row in rows]