from database.connection import get_connection
from models.sala import Sala

class SalaRepository:
    @staticmethod
    def crear(sala):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO salas (nombre, capacidad, descripcion) VALUES (?, ?, ?)",
            (sala.nombre, sala.capacidad, sala.descripcion)            
        )

        conn.commit()
        conn.close()

    @staticmethod
    def listar():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM salas")
        rows = cursor.fetchall()
        conn.close()

        return [Sala(*row) for row in rows]