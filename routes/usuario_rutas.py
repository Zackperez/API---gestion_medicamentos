from flask import Blueprint
from flask_cors import  cross_origin
from controllers.usuario_controlador import *

con_usuarios = UsuarioControlador()
obtener_datos_usuario = Blueprint('obtener_datos_usuario', __name__)

@obtener_datos_usuario.route('/obtener-datos-usuario/<id>', methods=['GET'])
@cross_origin()
def datos_usuario(id):
   return con_usuarios.obtener_datos_usuario(id)