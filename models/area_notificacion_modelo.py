from config import *
from flask import request, jsonify
import requests    
import json
import smtplib
from email.mime.text import MIMEText
import pywhatkit

class AreaNotificacionesModelo():

    headers = {
        'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRzY2ZtamxuZXpkamx6d3NtY214Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODg0ODk2ODEsImV4cCI6MjAwNDA2NTY4MX0.S1vQ1CYSpjvrwXIwSFC1_8dxin8I9XN8aXOdt6zCTWg',
        'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRzY2ZtamxuZXpkamx6d3NtY214Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODg0ODk2ODEsImV4cCI6MjAwNDA2NTY4MX0.S1vQ1CYSpjvrwXIwSFC1_8dxin8I9XN8aXOdt6zCTWg',
        'Content-Type' : 'application/json'
        }

    def enviar_notificaciones_usuario(self):
        id_paciente = request.json.get('id_paciente')
        fecha = request.json.get('fecha')
        hora = request.json.get('hora')
        medicina = request.json.get('medicina')
        informacion = request.json.get('informacion')
        asunto = request.json.get('asunto')

        datos_crear_notificacion = {
            'fecha': fecha,
            'hora': hora,
            'medicina': medicina,
            'informacion': informacion,
            'asunto': asunto,
            "id_paciente": id_paciente,
        }

        datos_recordatorio = json.dumps(datos_crear_notificacion)

        print(datos_recordatorio)

        try:
            response = requests.post(f'https://tscfmjlnezdjlzwsmcmx.supabase.co/rest/v1/ENTREGAS_MEDICAMENTOS?id_paciente=eq.{id_paciente}',
            headers= self.headers,
            data = datos_recordatorio)

            response2 = requests.post(f'https://tscfmjlnezdjlzwsmcmx.supabase.co/rest/v1/PACIENTES?id_paciente=eq.{id_paciente}',
            headers= self.headers)

            print(response.text)
            print(response2.text)


            id_paciente = request.json.get('id_paciente')
            fecha = request.json.get('fecha')
            hora = request.json.get('hora')
            medicina = request.json.get('medicina')
            informacion = request.json.get('informacion')
            asunto = request.json.get('asunto')
            celular = request.json.get('celular')

             # Configuración del servidor SMTP
            smtp_server = 'smtp.office365.com'
            smtp_port = 587  # Puerto para TLS
            smtp_username = 'jctrujillop@ul.edu.co'
            smtp_password = 'Kup54232'

            # Configuración del correo electrónico
            from_address = 'jctrujillop@ul.edu.co'
            to_address = '00zacks00@gmail.com'
            subject = f"[NOTIFICACIÓN DE COOMEVA] {asunto} de medicamentos"
            body = f'''
Hola, se te informa que ya puedes hacer el retiro de tu medicina, acá está los detalles:
            
MEDICAMENTO: {medicina} 

LUGAR: {informacion}

FECHA: {fecha}

HORA: {hora}

Enviado desde el area de COOMEVA automaticamente, si tienes algún inconveniente, comunicate con el área.

Se le agradece no responda este correo, solo es informativo.

            '''

            # Crear el objeto MIMEText
            message = MIMEText(body)
            message['Subject'] = subject
            message['From'] = from_address
            message['To'] = to_address

            # Conexión al servidor SMTP y envío del correo
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                # Iniciar la conexión TLS (Transport Layer Security)
                server.starttls()

                # Iniciar sesión en el servidor SMTP
                server.login(smtp_username, smtp_password)

                # Enviar el correo
                server.sendmail(from_address, to_address, message.as_string())

            return jsonify({"estado notificacion":'enviada'})

        except requests.exceptions.HTTPError as err:
            print(err)
        return 201



             