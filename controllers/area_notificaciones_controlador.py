from models.area_notificacion_modelo import *
 
mod_notificaciones = AreaNotificacionesModelo()

class AreaNotificacion:

    def enviar_notificaciones_usuario (self):
        query = mod_notificaciones.enviar_notificaciones_usuario()
        return query