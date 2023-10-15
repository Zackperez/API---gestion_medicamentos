from flask import Blueprint
from flask_cors import  cross_origin
from controllers.recordatorio_controlador import *

con_recordatorio= RecordatorioControlador()
crear_recordatorio = Blueprint('crear_recordatorio', __name__)
obtener_recordatorio = Blueprint('obtener_recordatorio', __name__)

@crear_recordatorio.route('/crear_recordatorio/', methods=['POST'])
@cross_origin()
def creacion_recordatorio():
   return con_recordatorio.crear_recordatorio()

@obtener_recordatorio.route('/obtener_recordatorio/', methods=['POST'])
@cross_origin()
def busqueda_recordatorio():
   return con_recordatorio.obtener_recordatorio()