from flask import Blueprint
from flask_cors import  cross_origin
from controllers.recordatorio_controlador import *

con_recordatorio= RecordatorioControlador()
crear_recordatorio = Blueprint('crear-recordatorio', __name__)
obtener_recordatorio = Blueprint('obtener_recordatorio', __name__)
eliminar_recordatorio = Blueprint('eliminar_recordatorio', __name__)


@crear_recordatorio.route('/crear-recordatorio/', methods=['POST'])
@cross_origin()
def creacion_recordatorio():
   return con_recordatorio.crear_recordatorio()

@obtener_recordatorio.route('/obtener-recordatorio/', methods=['POST'])
@cross_origin()
def busqueda_recordatorio():
   return con_recordatorio.obtener_recordatorio()

@obtener_recordatorio.route('/eliminar-recordatorio/<id>', methods=['DELETE'])
@cross_origin()
def eliminar_recordatorio(id):
   return con_recordatorio.eliminar_recordatorio(id)