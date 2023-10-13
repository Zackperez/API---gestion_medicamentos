from flask import Blueprint
from flask_cors import  cross_origin
from controllers.reportes_controlador import *

con_reporte = ReporteControlador()
crear_reporte = Blueprint('crear_reporte', __name__)
obtener_reporte = Blueprint('obtener_reporte', __name__)

@crear_reporte.route('/crear_reporte/', methods=['POST'])
@cross_origin()
def creacion_reporte():
   return con_reporte.crear_reporte()

@obtener_reporte.route('/obtener_reporte/', methods=['GET'])
@cross_origin()
def busqueda_reporte():
   return con_reporte.obtener_reporte()