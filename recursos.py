from flask_restful import Resource

class HelloWorld(Resource):
    def get(self):
        return 'Hola mundo'

class InicioDeSesion(Resource):
    def get(self):
        return 'Hola, estamos construyendo un inicio de sesion'
