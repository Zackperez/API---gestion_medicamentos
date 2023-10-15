from config import *
from flask import request, jsonify
import requests    
import json

class RegistroUsuario():

    headers = {
        'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRzY2ZtamxuZXpkamx6d3NtY214Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODg0ODk2ODEsImV4cCI6MjAwNDA2NTY4MX0.S1vQ1CYSpjvrwXIwSFC1_8dxin8I9XN8aXOdt6zCTWg',
        'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRzY2ZtamxuZXpkamx6d3NtY214Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODg0ODk2ODEsImV4cCI6MjAwNDA2NTY4MX0.S1vQ1CYSpjvrwXIwSFC1_8dxin8I9XN8aXOdt6zCTWg',
        'Content-Type' : 'application/json'
        }

    # Realizar una solicitud POST a la API de SUPABASE
    def registrar_datos_usuario(self):
        try:
            user = request.json.get('user')
            password = request.json.get('password')
            name = request.json.get('name')
            last_name = request.json.get('last_name')
            email_address = request.json.get('email_address')
            phone_number = request.json.get('phone_number')
            id_patient = request.json.get('id_patient')

            datos_registro_usuario = {
                'user': user,
                'password': password,
                'id_patient': id_patient
            }

            datos_registro_paciente = {
                'id_patient': id_patient,
                'name': name,
                'last_name': last_name,
                'email_address': email_address,
                'phone_number': phone_number,
            }
            
            datos_reporte_paciente = {
                 'description': "no tiene",
                 'symptoms': "no tiene",
                 'disease': "no tiene",
                 'id_patient': id_patient
            }

            datos_recordatorio_medicina = {
                'date': "",
                'time': "",
                'medicine': "",
                'information': "",
                'id_patient': id_patient
            }
            
            datos_insertar_usuario_nuevo = json.dumps(datos_registro_usuario)
            datos_insertar_paciente_nuevo = json.dumps(datos_registro_paciente)
            datos_insertar_nuevo_reporte = json.dumps(datos_reporte_paciente)
            datos_recordatorio_tiempo_medicina = json.dumps(datos_recordatorio_medicina)

            response = requests.post('https://tscfmjlnezdjlzwsmcmx.supabase.co/rest/v1/user', 
                                     
                data = datos_insertar_usuario_nuevo, 
                headers = self.headers)

            response2 = requests.post('https://tscfmjlnezdjlzwsmcmx.supabase.co/rest/v1/patients', 
                                     
                data = datos_insertar_paciente_nuevo, 
                headers = self.headers)
            response3 = requests.post('https://tscfmjlnezdjlzwsmcmx.supabase.co/rest/v1/reports',
                                      
                data= datos_insertar_nuevo_reporte,
                headers=self.headers)

            response4 = requests.post('https://tscfmjlnezdjlzwsmcmx.supabase.co/rest/v1/medicine_reminders',
                                      
                data= datos_recordatorio_tiempo_medicina,
                headers=self.headers)

            return jsonify({"Registro de usuario": "Exitoso", "Registro de paciente": "Exitoso", "Registro de reporte": "Exitoso"})
        
        except requests.exceptions.HTTPError as err:
            print(err)
        return 201
    