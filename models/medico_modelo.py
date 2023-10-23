from config import *
from flask import request, jsonify
import requests    
import json

class MedicoModelo():

    headers = {
        'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRzY2ZtamxuZXpkamx6d3NtY214Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODg0ODk2ODEsImV4cCI6MjAwNDA2NTY4MX0.S1vQ1CYSpjvrwXIwSFC1_8dxin8I9XN8aXOdt6zCTWg',
        'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRzY2ZtamxuZXpkamx6d3NtY214Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODg0ODk2ODEsImV4cCI6MjAwNDA2NTY4MX0.S1vQ1CYSpjvrwXIwSFC1_8dxin8I9XN8aXOdt6zCTWg',
        'Content-Type' : 'application/json'
        }

    # Realizar una solicitud POST a la API de SUPABASE
    def buscar_paciente(self):
        try:
            id_paciente = request.json.get('id_paciente')
            response = requests.get('https://tscfmjlnezdjlzwsmcmx.supabase.co/rest/v1/PACIENTES?id_paciente=eq.'+str(id_paciente),
                                   headers = self.headers)
            
            response_data = json.loads(response.text)
            id_paciente = response_data[0]['id_paciente']
            nombre = response_data[0]['nombre']
            apellido = response_data[0]['apellido']
            correo = response_data[0]['correo']
            celular = response_data[0]['celular']


            return jsonify({"id_paciente": id_paciente,
                            "nombre": nombre,
                            "apellido": apellido,
                            "correo": correo,
                            "celular":celular,
                            })

        except requests.exceptions.HTTPError as err:
            print(err)
        return 201
    
    def obtener_reportes_paciente(self):

        try:
            id_paciente = request.json.get('id_paciente')
            response = requests.get('https://tscfmjlnezdjlzwsmcmx.supabase.co/rest/v1/PACIENTES?id_paciente=eq.'+str(id_paciente),
            headers = self.headers)
            
            response2 = requests.get('https://tscfmjlnezdjlzwsmcmx.supabase.co/rest/v1/REPORTES?id_paciente=eq.'+str(id_paciente),
            headers = self.headers)

            response3 = requests.get('https://tscfmjlnezdjlzwsmcmx.supabase.co/rest/v1/RECORDATORIOS_MEDICINA?id_paciente=eq.'+str(id_paciente),
            headers = self.headers)

            lista_reportes = []
            for reportes in response2.json():
                lista_reportes.append(reportes)

            lista_recordatorio_medicamentos = []
            for recordatorio_medicamentos in response3.json():
                lista_recordatorio_medicamentos.append(recordatorio_medicamentos)


            return jsonify({
                "datos_pacientes": {
                    "id_paciente": response.json()[0]['id_paciente'],
                    "nombre": response.json()[0]['nombre'],
                    "apellido": response.json()[0]['apellido'],
                    "correo": response.json()[0]['correo'],
                    "celular": response.json()[0]['celular'],
                },
                "reportes": lista_reportes,

                "recordatorios_medicamentos": lista_recordatorio_medicamentos
            })

        
        except requests.exceptions.HTTPError as err:
            print(err)
        return 201