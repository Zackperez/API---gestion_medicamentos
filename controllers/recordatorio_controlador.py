from models.recordatorio_modelo import *


mod_recordatorio = RecordatorioModelo()
class RecordatorioControlador:

    def crear_recordatorio(self):
        query= mod_recordatorio.crear_recordatorio()
        return query
    
    def obtener_recordatorio(self, id):
        query= mod_recordatorio.obtener_recordatorio(id)
        return query
    
    def eliminar_recordatorio(self, id):
        query= mod_recordatorio.eliminar_recordatorio(id)
        return query