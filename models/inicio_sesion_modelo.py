from config import *
from flask import request, jsonify
import supabase

class Usuario():

    headers = {
        'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRzY2ZtamxuZXpkamx6d3NtY214Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODg0ODk2ODEsImV4cCI6MjAwNDA2NTY4MX0.S1vQ1CYSpjvrwXIwSFC1_8dxin8I9XN8aXOdt6zCTWg',
        'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRzY2ZtamxuZXpkamx6d3NtY214Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODg0ODk2ODEsImV4cCI6MjAwNDA2NTY4MX0.S1vQ1CYSpjvrwXIwSFC1_8dxin8I9XN8aXOdt6zCTWg',
        'Content-Type' : 'application/json'
        }

    def login(self):
        user = request.json.get('user')
        password = request.json.get('password')

        SUPABASE_URL = 'https://tscfmjlnezdjlzwsmcmx.supabase.co'
        SUPABASE_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRzY2ZtamxuZXpkamx6d3NtY214Iiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODg0ODk2ODEsImV4cCI6MjAwNDA2NTY4MX0.S1vQ1CYSpjvrwXIwSFC1_8dxin8I9XN8aXOdt6zCTWg'
        # Conectamos con Supabase
        client = supabase.create_client(SUPABASE_URL, SUPABASE_KEY)

        # Buscamos el usuario en la tabla 'users'
        query = client.table('user').select('*').eq('user', user).eq('password', password)
        res = query.execute()
        print(res)
        # Si el usuario existe y la contraseña es correcta, se devuelve un token JWT
        if len(res.data) == 1:
            return jsonify({"acceso": "ACCESO A LA CUENTA AUTORIZADO"})
        #jsonify({"acceso": "AUTORIZADO" ,"access_token": access_token})
        else:
            return jsonify({"acceso": "ACCESO A LA CUENTA NO AUTORIZADO"})
    
    # def datos_usuario(self):
            
    #     response = requests.get('https://tscfmjlnezdjlzwsmcmx.supabase.co/rest/v1/usuario?select=*', 
    #                             headers= self.headers)
    #     return response.content
    