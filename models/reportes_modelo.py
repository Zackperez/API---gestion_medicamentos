from config import *
from flask import request, jsonify
import requests    
import json

class ReporteModelo():

    headers = {
        'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRzY2ZtamxuZXpkamx6d3NtY214Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODg0ODk2ODEsImV4cCI6MjAwNDA2NTY4MX0.S1vQ1CYSpjvrwXIwSFC1_8dxin8I9XN8aXOdt6zCTWg',
        'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRzY2ZtamxuZXpkamx6d3NtY214Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODg0ODk2ODEsImV4cCI6MjAwNDA2NTY4MX0.S1vQ1CYSpjvrwXIwSFC1_8dxin8I9XN8aXOdt6zCTWg',
        'Content-Type' : 'application/json'
        }

    # Realizar una solicitud POST a la API de SUPABASE
    def crear_reporte(self):
            
        descripcion = request.json.get('descripcion')
        sintomas =  request.json.get('sintomas')
        enfermedad = request.json.get('enfermedad')
        id_paciente = request.json.get('id_paciente')

        datos_crear_reportes = {
            'descripcion': descripcion,
            'sintomas': sintomas,
            'enfermedad': enfermedad,
            'id_paciente': id_paciente
        }

        datos_reportes= json.dumps(datos_crear_reportes)

        try:
            requests.post('https://tscfmjlnezdjlzwsmcmx.supabase.co/rest/v1/REPORTES', 
            data = datos_reportes,
            headers = self.headers)

            return jsonify({"Reporte creado para el usuario": id_paciente})

        except requests.exceptions.HTTPError as err:
            print(err)

        return 201
    
    def obtener_reporte(self):
        try:
            id_paciente = request.json.get('id_paciente')
            response = requests.get('https://tscfmjlnezdjlzwsmcmx.supabase.co/rest/v1/REPORTES?id_paciente=eq.'+str(id_paciente),
                                   headers = self.headers)
            
            print(response.json())
            lista_reportes = []

            for reportes in response.json():
                lista_reportes.append(reportes)
            
            return jsonify({"reportes": lista_reportes})

        except requests.exceptions.HTTPError as err:
            print(err)
        return 201
