from flask import Blueprint
from flask_cors import  cross_origin
from controllers.area_notificaciones_controlador import *

con_notificaciones = AreaNotificacion()
enviar_notificaciones_usuario = Blueprint('enviar_notificaciones_usuario', __name__)

@enviar_notificaciones_usuario.route('/enviar-notificaciones-usuario/', methods=['POST'])
@cross_origin()
def notificaciones_usuario():
   return con_notificaciones.enviar_notificaciones_usuario()
