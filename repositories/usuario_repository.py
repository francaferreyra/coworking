from database.connection import get_connection
from models.usuario import Usuario

class UsuarioRepository:

    @staticmethod
    def crear(usuario):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO usuarios (nombre, email, rol) VALUES (?, ?, ?)",
            (usuario.nombre, usuario.email, usuario.rol)            
        )

        conn.commit()
        conn.close()

    @staticmethod
    def listar():
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM usuarios")
        rows = cursor.fetchall()
        conn.close()

        return [Usuario(*row) for row in rows]