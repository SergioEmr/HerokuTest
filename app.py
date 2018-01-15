from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
	def get(self):
		return {'item': 'Está vivo'}

#Clave agem escobedo 19021
api.add_resource(Item, '/item')
app.run(port=5000, debug = True)
