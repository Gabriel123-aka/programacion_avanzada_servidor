from flask import Flask
from flask_restful import Resource, Api
from rutas import RutasApi

app = Flask(__name__)
api = Api(app)

rutas = RutasApi()
rutas.inicializar_rutas(api)




app.run(debug=True, port=8070)
    
