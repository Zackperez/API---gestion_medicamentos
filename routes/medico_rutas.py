from flask import Blueprint
from flask_cors import  cross_origin
from controllers.medico_controlador import *

con_medico= MedicoControlador()
buscar_paciente = Blueprint('buscar_paciente', __name__)
obtener_reportes_paciente = Blueprint('obtener_reportes_paciente', __name__)
datos_de_doctor = Blueprint('datos_de_doctor', __name__)


@datos_de_doctor.route('/datos-doctor/<id>', methods=['GET'])
@cross_origin()
def datos_doctor(id):
   return con_medico.datos_de_doctor(id)

@buscar_paciente.route('/buscar-paciente/<id>', methods=['GET'])
@cross_origin()
def busqueda_paciente(id):
   return con_medico.buscar_paciente(id)

@obtener_reportes_paciente.route('/obtener-reportes-paciente/<id>', methods=['GET'])
@cross_origin()
def busqueda_reporte_paciente(id):
   return con_medico.obtener_reportes_paciente(id)