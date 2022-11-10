from flask  import  Flask, request
from flask_restful import Api, Resource
import random

app = Flask(__name__)
api = Api(app)

class rastgeleSayiSinif(Resource):
    def get(self):
        randomnumber=random.randint(0,9)
        return {'Sayi' : randomnumber}, 200

class dortKat(Resource):
    def get(self,number):
        dortKat=number*4
        return {'dortKat' : dortKat }, 200

class Name(Resource):
    def get(self,name):
        return {'Mesaj' : 'Böyle bir endpoint bulunmuyor!'}, 404

api.add_resource(rastgeleSayiSinif, '/rastgeleSayi')
api.add_resource(dortKat, '/dortKat/<int:number>')
api.add_resource(Name, '/<string:name>')

if __name__ =='__main__':
    app.run(host="0.0.0.0", port=5000)
    app.run()
