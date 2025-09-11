from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return 'Hola mundo'

class InicioDeSesion(Resource):
    def get(self):
        return 'Hola, estamos construyendo un inicio de sesion'

api.add_resource(HelloWorld, '/')
api.add_resource(InicioDeSesion, '/login')


app.run(debug=True, port=8000)
    
    # 172.24.160.1