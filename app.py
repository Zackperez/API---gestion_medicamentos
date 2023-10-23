from flask import Flask
from flask_cors import CORS
from config import *
from routes.registro_usuario_rutas import *
from routes.inicio_sesion_rutas import *
from routes.recordatorios_medicamentos_rutas import *
from routes.medico_rutas import *
from routes.reportes_rutas import *

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5000"}})

app.register_blueprint(registrar_usuario)
app.register_blueprint(iniciar_sesion)
app.register_blueprint(buscar_paciente)
app.register_blueprint(obtener_reportes_paciente)
app.register_blueprint(crear_recordatorio)
app.register_blueprint(obtener_recordatorio)
app.register_blueprint(crear_reporte)
app.register_blueprint(obtener_reporte)

def pagina_no_encontrada(error):
    return "<h1>La pagina a la que intentas acceder no existe...</h1>"

if __name__=="__main__":
    app.register_error_handler(404 , pagina_no_encontrada)
    app.run(port=5000, debug=True)
