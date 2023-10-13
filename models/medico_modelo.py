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
            id_patient = request.json.get('id_patient')
            response = requests.get('https://tscfmjlnezdjlzwsmcmx.supabase.co/rest/v1/patients?id_patient=eq.'+str(id_patient),
                                   headers = self.headers)
            
            response_data = json.loads(response.text)
            id_patient = response_data[0]['id_patient']
            name = response_data[0]['name']
            last_name = response_data[0]['last_name']
            email_address = response_data[0]['email_address']
            phone_number = response_data[0]['phone_number']


            return jsonify({"id_patient": id_patient,
                            "name": name,
                            "last_name": last_name,
                            "email_address": email_address,
                            "phone_number":phone_number,
                            })

        except requests.exceptions.HTTPError as err:
            print(err)
        return 201
    
    def obtener_reportes_paciente(self):

        try:
            id_patient = request.json.get('id_patient')
            response = requests.get('https://tscfmjlnezdjlzwsmcmx.supabase.co/rest/v1/patients?id_patient=eq.'+str(id_patient),
            headers = self.headers)
            
            response2 = requests.get('https://tscfmjlnezdjlzwsmcmx.supabase.co/rest/v1/reports?id_patient=eq.'+str(id_patient),
            headers = self.headers)

            response3 = requests.get('https://tscfmjlnezdjlzwsmcmx.supabase.co/rest/v1/medicine_reminders?id_patient=eq.'+str(id_patient),
            headers = self.headers)

            lista_reportes = []
            for reportes in response2.json():
                lista_reportes.append(reportes)

            lista_recordatorio_medicamentos = []
            for recordatorio_medicamentos in response3.json():
                lista_recordatorio_medicamentos.append(recordatorio_medicamentos)


            return jsonify({
                "datos_pacientes": {
                    "id_patient": response.json()[0]['id_patient'],
                    "name": response.json()[0]['name'],
                    "last_name": response.json()[0]['last_name'],
                    "email_address": response.json()[0]['email_address'],
                    "phone_number": response.json()[0]['phone_number'],
                },
                "reportes": lista_reportes,

                "recordatorios_medicamentos": lista_recordatorio_medicamentos
            })

        
        except requests.exceptions.HTTPError as err:
            print(err)
        return 201