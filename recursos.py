from flask_restful import Resource
from flask import render_template, make_response

class HelloWorld(Resource):
    def get(self):
        return 'Hola mundo'


class InicioDeSesion(Resource):
    def get(self):
        return make_response(render_template('login.html'))

    def post(self):
        from flask import request
        email = request.form.get('email')
        password = request.form.get('password')
        # Aquí podrías validar el usuario
        return f"Recibido login: {email}, {password}"

class RegistrodeUsuario(Resource):
    def get(self):
        return make_response(render_template('registro.html'))

    def post(self):
        from flask import request
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        password = request.form.get('password')
        telefono = request.form.get('telefono')
        # Aquí podrías guardar el usuario
        return f"Recibido registro: {nombre}, {email}, {telefono}"
