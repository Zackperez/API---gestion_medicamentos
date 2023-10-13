from flask import Blueprint
from flask_cors import  cross_origin
from controllers.registro_sesion_controlador import *

con_registro_sesion= RegistroSesionControlador()
registrar_usuario = Blueprint('registrar_usuario', __name__)

@registrar_usuario.route('/registrar-usuario', methods=['POST'])

@cross_origin()
def registro_usuario():
   return con_registro_sesion.registro_usuario()

