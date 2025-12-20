from repositories.usuario_repository import UsuarioRepository
from models.usuario import Usuario

class UsuarioService:

    
    def crear_usuario(nombre, email, rol):
        usuario = Usuario(id=None, nombre=nombre, email=email, rol=rol)
        UsuarioRepository.crear(usuario)

    
    def listar_usuarios():
        return UsuarioRepository.listar()