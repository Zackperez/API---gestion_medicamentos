from models.medico_modelo import *
 
mod_medico = MedicoModelo()

class MedicoControlador:

    def buscar_paciente (self):
        query = mod_medico.buscar_paciente()
        return query
    
    def obtener_reportes_paciente(self):
        query = mod_medico.obtener_reportes_paciente()
        return query