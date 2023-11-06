from models.usuario_modelo import *
 
mod_usuario = UsuarioModelo()

class UsuarioControlador:

    def obtener_datos_usuario (self, id):
        query = mod_usuario.obtener_datos_usuario(id)
        return query
    
    def obtener_notificaciones_usuario (self, id):
        query = mod_usuario.notificaciones_usuario(id)
        return query