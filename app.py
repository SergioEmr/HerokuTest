from flask import Flask, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
	def get(self,agem):
		return {'item': agem}

#Clave agem escobedo 19021
api.add_resource(Item, 'item/AGEM=<int:agem>')
app.run(port=5000, debug = True)
