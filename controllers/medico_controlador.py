from models.medico_modelo import *
 
mod_medico = MedicoModelo()

class MedicoControlador:

    def buscar_paciente (self, id):
        query = mod_medico.buscar_paciente(id)
        return query
    
    def obtener_reportes_paciente(self, id):
        query = mod_medico.obtener_reportes_paciente(id)
        return query