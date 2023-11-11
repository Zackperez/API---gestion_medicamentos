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
    
    def datos_de_doctor(self, id):
        try:
            response = requests.get(f'https://tscfmjlnezdjlzwsmcmx.supabase.co/rest/v1/DOCTORES?id_doctor=eq.{id}',
                                   headers = self.headers)
            
            response_data = json.loads(response.text)
            id_doctor = response_data[0]['id_doctor']
            nombre = response_data[0]['nombre']
            apellido = response_data[0]['apellido']
            celular = response_data[0]['celular']
            correo = response_data[0]['correo']
            print(id_doctor)

            return jsonify({"id_doctor": id_doctor,
                            "nombre": nombre,
                            "apellido": apellido,
                            "correo": correo,
                            "celular":celular,
                            })
        except requests.exceptions.HTTPError as err:
            print(err)
        return 201

    # Realizar una solicitud POST a la API de SUPABASE
    def buscar_paciente(self, id):
        try:
            response = requests.get(f'https://tscfmjlnezdjlzwsmcmx.supabase.co/rest/v1/PACIENTES?id_paciente=eq.{id}',
                                   headers = self.headers)
            
            response_data = json.loads(response.text)

            print(response_data)
            id_paciente = response_data[0]['id_paciente']
            nombre = response_data[0]['nombre']
            apellido = response_data[0]['apellido']
            correo = response_data[0]['correo']
            celular = response_data[0]['celular']
            fecha = response_data[0]['fecha']
            sexo = response_data[0]['sexo']
            direccion = response_data[0]['direccion']

            return jsonify({"id_paciente": id_paciente,
                            "nombre": nombre,
                            "apellido": apellido,
                            "correo": correo,
                            "celular":celular,
                            "fecha":fecha,
                            "sexo": sexo,
                            "direccion": direccion,
                            })

        except requests.exceptions.HTTPError as err:
            print(err)
        return 201
    
    def obtener_reportes_paciente(self, id):
        try:
            response = requests.get(f'https://tscfmjlnezdjlzwsmcmx.supabase.co/rest/v1/PACIENTES?id_paciente=eq.{id}',
            headers = self.headers)
            
            response2 = requests.get(f'https://tscfmjlnezdjlzwsmcmx.supabase.co/rest/v1/REPORTES?id_paciente=eq.{id}',
            headers = self.headers)

            response3 = requests.get(f'https://tscfmjlnezdjlzwsmcmx.supabase.co/rest/v1/RECORDATORIOS_MEDICINAS?id_paciente=eq.{id}',
            headers = self.headers)

            response_data = json.loads(response.text)
            id_paciente = response_data[0]['id_paciente']
            nombre = response_data[0]['nombre']
            apellido = response_data[0]['apellido']
            correo = response_data[0]['correo']
            celular = response_data[0]['celular']
            fecha = response_data[0]['fecha']
            sexo = response_data[0]['sexo']
            direccion = response_data[0]['direccion']

            lista_reportes = []
            for reportes in response2.json():
                lista_reportes.append(reportes)

            lista_recordatorio_medicamentos = []
            for recordatorio_medicamentos in response3.json():
                lista_recordatorio_medicamentos.append(recordatorio_medicamentos)


            return jsonify({
                "datos_pacientes": {
                            "id_paciente": id_paciente,
                            "nombre": nombre,
                            "apellido": apellido,
                            "correo": correo,
                            "celular":celular,
                            "fecha":fecha,
                            "sexo": sexo,
                            "direccion": direccion,
                },
                "reportes": lista_reportes,

                "recordatorios_medicamentos": lista_recordatorio_medicamentos
            })

        
        except requests.exceptions.HTTPError as err:
            print(err)
        return 201