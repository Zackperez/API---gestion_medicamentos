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
            usuario = request.json.get('usuario')
            contrasena = request.json.get('contrasena')
            nombre = request.json.get('nombre')
            apellido = request.json.get('apellido')
            correo = request.json.get('correo')
            celular = request.json.get('celular')
            id_paciente = request.json.get('id_paciente')
            sexo = request.json.get('sexo')
            fecha = request.json.get('fecha')
            
            datos_registro_usuario = {
                'usuario': usuario,
                'contrasena': contrasena,
                'id_paciente': id_paciente
            }

            datos_registro_paciente = {
                'id_paciente': id_paciente,
                'nombre': nombre,
                'apellido': apellido,
                'correo': correo,
                'fecha': fecha,
                'sexo': sexo,
                'celular': celular,
            }
            
            datos_reporte_paciente = {
                 'descripcion': "no tiene",
                 'sintomas': "no tiene",
                 'enfermedad': "no tiene",
                 'id_paciente': id_paciente
            }

            datos_recordatorio_medicina = {
                'fecha': "",
                'hora': "",
                'medicina': "",
                'informacion': "",
                'id_paciente': id_paciente
            }
            
            datos_insertar_usuario_nuevo = json.dumps(datos_registro_usuario)
            datos_insertar_paciente_nuevo = json.dumps(datos_registro_paciente)
            datos_insertar_nuevo_reporte = json.dumps(datos_reporte_paciente)
            datos_recordatorio_tiempo_medicina = json.dumps(datos_recordatorio_medicina)

            response = requests.post('https://tscfmjlnezdjlzwsmcmx.supabase.co/rest/v1/USUARIOS', 
                                     
                data = datos_insertar_usuario_nuevo, 
                headers = self.headers)

            response2 = requests.post('https://tscfmjlnezdjlzwsmcmx.supabase.co/rest/v1/PACIENTES', 
                                     
                data = datos_insertar_paciente_nuevo, 
                headers = self.headers)
            #response3 = requests.post('https://tscfmjlnezdjlzwsmcmx.supabase.co/rest/v1/REPORTES',
                                      
            #    data= datos_insertar_nuevo_reporte,
            #    headers=self.headers)

            #response4 = requests.post('https://tscfmjlnezdjlzwsmcmx.supabase.co/rest/v1/RECORDATORIOS_MEDICINAS',
                                      
            #   data= datos_recordatorio_tiempo_medicina,
            #   headers=self.headers)

            return jsonify({"Registro de usuario": "Exitoso", "Registro de paciente": "Exitoso", "Registro de reporte": "Exitoso"})
        
        except requests.exceptions.HTTPError as err:
            print(err)
        return 201
    