from repositories.sala_repository import SalaRepository
from models.sala import Sala

class SalaService:

    def crear_sala(nombre, capacidad, descripcion):
        sala = Sala(id=None, nombre=nombre, capacidad=capacidad, descripcion=descripcion)
        SalaRepository.crear(sala)

    def listar_salas():
        return SalaRepository.listar()