from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app, prefix="/api/v1")


class PrivateResource(Resource):
    def get(self):
        return {"code": 12345}


api.add_resource(PrivateResource, '/private')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)


"""

iniciar la aplicacion
$ python app.py

probar recurso
$ curl -X GET http://localhost:5001/api/v1/private

instalar dependencias 
$ pip install flask
$ pip install flask-restful

generar el archivo requirements
$ pip freeze > requirements.txt

instalar dependencias con requirements
$ pip install -r requirements.txt

"""