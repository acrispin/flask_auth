from flask import Flask
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required, current_identity

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'

api = Api(app, prefix="/api/v3")

USER_AUTH = {
    "admin": "12345678"
}


class User(object):
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return "User(id='%s')" % self.id


def verify(username, password):
    if not (username and password):
        return False
    if USER_AUTH.get(username) == password:
        return User(id=123456)


def identity(payload):
    user_id = payload['identity']
    return {"user_id": user_id}


jwt = JWT(app, verify, identity)


class PrivateResource(Resource):
    @jwt_required()
    def get(self):
        return {"code": 12345}


class IdentityResource(Resource):
    @jwt_required()
    def get(self):
        return dict(current_identity)


api.add_resource(PrivateResource, '/private')
api.add_resource(IdentityResource, '/identity')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5003, debug=True)


"""
http://polyglot.ninja/jwt-authentication-python-flask/

iniciar la aplicacion
$ python app_jwt_auth.py

probar recurso
$ curl -X GET http://localhost:5003/api/v3/private

obtener el token
$ curl -H "Content-Type: application/json" -X POST -d '{"username":"admin","password":"12345678"}' http://localhost:5003/auth

token obtenido
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MDEyNjQ3MDQsImlhdCI6MTUwMTI2NDQwNCwibmJmIjoxNTAxMjY0NDA0LCJpZGVudGl0eSI6MTIzfQ.STZVQN14wU9w42OJOKl6o-jF7CmhPnOKzAOg3ZpxKdw

probar recurso con token
$ curl -X GET http://localhost:5003/api/v3/private -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1MDEyNjQ3MDQsImlhdCI6MTUwMTI2NDQwNCwibmJmIjoxNTAxMjY0NDA0LCJpZGVudGl0eSI6MTIzfQ.STZVQN14wU9w42OJOKl6o-jF7CmhPnOKzAOg3ZpxKdw"

instalar dependencias 
$ pip install flask
$ pip install flask-restful
$ pip install Flask-JWT

generar el archivo requirements
$ pip freeze > requirements.txt

instalar dependencias con requirements
$ pip install -r requirements.txt

"""