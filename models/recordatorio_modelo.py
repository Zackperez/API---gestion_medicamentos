from config import *
from flask import request, jsonify
import requests    
import json

class RecordatorioModelo():

    headers = {
        'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRzY2ZtamxuZXpkamx6d3NtY214Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODg0ODk2ODEsImV4cCI6MjAwNDA2NTY4MX0.S1vQ1CYSpjvrwXIwSFC1_8dxin8I9XN8aXOdt6zCTWg',
        'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRzY2ZtamxuZXpkamx6d3NtY214Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODg0ODk2ODEsImV4cCI6MjAwNDA2NTY4MX0.S1vQ1CYSpjvrwXIwSFC1_8dxin8I9XN8aXOdt6zCTWg',
        'Content-Type' : 'application/json'
        }
    
    def crear_recordatorio(self):
            
        fecha = request.json.get('fecha')
        hora = request.json.get('hora')
        medicamento = request.json.get('medicamento')
        informacion = request.json.get('informacion')
        id_paciente = request.json.get('id_paciente')

        datos_crear_recordatorios = {
            'fecha': fecha,
            'hora': hora,
            'medicamento': medicamento,
            'informacion': informacion,
            'id_paciente': id_paciente
        }

        datos_recordatorio = json.dumps(datos_crear_recordatorios)

        try:
            requests.post('https://tscfmjlnezdjlzwsmcmx.supabase.co/rest/v1/RECORDATORIOS_MEDICINAS', 
            data = datos_recordatorio, 
            headers = self.headers)

            return jsonify({"Recordatorio creado para el usuario": id_paciente})

        except requests.exceptions.HTTPError as err:
            print(err)

        return 201
    
    def obtener_recordatorio(self, id):

        try:

            response = requests.get(f'https://tscfmjlnezdjlzwsmcmx.supabase.co/rest/v1/RECORDATORIOS_MEDICINAS?id_paciente=eq.{id}',
            headers= self.headers)

            print(response)

            lista_recordatorios = []
            for recordatorios in response.json():
                lista_recordatorios.append(recordatorios)

            print(response.text)
            return jsonify({"recordatorios": lista_recordatorios})
        except requests.exceptions.HTTPError as err:
            print(err)
        return 201

    def eliminar_recordatorio(self, id_recordatorio_eliminar):

        try:
            asd = requests.delete(f'https://tscfmjlnezdjlzwsmcmx.supabase.co/rest/v1/RECORDATORIOS_MEDICINAS?id_recordatorio=eq.{id_recordatorio_eliminar}', 
            headers = self.headers)
            print(asd)
            return jsonify({"Recordatorio eliminado": "Exitoso"})

        except requests.exceptions.HTTPError as err:
            print(err)

        return 201









             