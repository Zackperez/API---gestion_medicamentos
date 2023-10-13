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
            
        date = request.json.get('date')
        time = request.json.get('time')
        medicine = request.json.get('medicine')
        information = request.json.get('information')
        id_patient = request.json.get('id_patient')

        datos_crear_recordatorios = {
            'date': date,
            'time': time,
            'medicine': medicine,
            'information': information,
            'id_patient': id_patient
        }

        datos_recordatorio = json.dumps(datos_crear_recordatorios)

        try:
            requests.post('https://tscfmjlnezdjlzwsmcmx.supabase.co/rest/v1/medicine_reminders', 
            data = datos_recordatorio, 
            headers = self.headers)

            return jsonify({"Recordatorio creado para el usuario": id_patient})

        except requests.exceptions.HTTPError as err:
            print(err)

        return 201
    
    def obtener_recordatorio(self):

        try:
            id_patient = request.json.get('id_patient')
            response = requests.get('https://tscfmjlnezdjlzwsmcmx.supabase.co/rest/v1/medicine_reminders?id_patient=eq.'+str(id_patient),
            headers= self.headers)

            lista_recordatorios = []
            for recordatorios in response.json():
                lista_recordatorios.append(recordatorios)

            print(response.text)
            return jsonify({"recordatorios": lista_recordatorios})
        except requests.exceptions.HTTPError as err:
            print(err)
        return 201











             