from models.recordatorio_modelo import *


mod_recordatorio = RecordatorioModelo()
class RecordatorioControlador:

    def crear_recordatorio(self):
        query= mod_recordatorio.crear_recordatorio()
        return query
    
    def obtener_recordatorio(self):
        query= mod_recordatorio.obtener_recordatorio()
        return query