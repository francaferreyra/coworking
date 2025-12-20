import os
import sqlite3


def get_connection():
    # Ruta absoluta al archivo de base de datos, independiente del cwd
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(project_root, 'instance', 'coworking.db')

    # Asegura que la carpeta exista
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    return sqlite3.connect(db_path)
