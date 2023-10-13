from models.reportes_modelo import *


mod_reporte = ReporteModelo()
class ReporteControlador:

    def crear_reporte(self):
        query= mod_reporte.crear_reporte()
        return query

    def obtener_reporte(self):
        query= mod_reporte.obtener_reporte()
        return query