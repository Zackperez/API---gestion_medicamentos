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
            
        description = request.json.get('description')
        symptoms =  request.json.get('symptoms')
        disease = request.json.get('disease')
        id_patient = request.json.get('id_patient')

        datos_crear_reportes = {
            'description': description,
            'symptoms': symptoms,
            'disease': disease,
            'id_patient': id_patient
        }

        datos_reportes= json.dumps(datos_crear_reportes)

        try:
            requests.post('https://tscfmjlnezdjlzwsmcmx.supabase.co/rest/v1/reports', 
            data = datos_reportes,
            headers = self.headers)

            return jsonify({"Reporte creado para el usuario": id_patient})

        except requests.exceptions.HTTPError as err:
            print(err)

        return 201
    
    def obtener_reporte(self):
        try:
            id_patient = request.json.get('id_patient')
            response = requests.get('https://tscfmjlnezdjlzwsmcmx.supabase.co/rest/v1/reports?id_patient=eq.'+str(id_patient),
                                   headers = self.headers)
            
            print(response.json())
            lista_reportes = []

            for reportes in response.json():
                lista_reportes.append(reportes)
            
            return jsonify({"reportes": lista_reportes})

        except requests.exceptions.HTTPError as err:
            print(err)
        return 201
