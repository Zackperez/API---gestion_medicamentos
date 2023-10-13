from models.registro_usuario_modelo import *

mod_registro_usuario = RegistroUsuario()

class RegistroSesionControlador():
    def registro_usuario(self):
        query = mod_registro_usuario.registrar_datos_usuario()
        return query