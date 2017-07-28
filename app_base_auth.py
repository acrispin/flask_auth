from flask import Flask
from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
api = Api(app, prefix="/api/v2")
auth = HTTPBasicAuth()

USER_AUTH = {
    "admin": "12345678"
}

@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    return USER_AUTH.get(username) == password


class PrivateResource(Resource):
    @auth.login_required
    def get(self):
        return {"code": 12345}


api.add_resource(PrivateResource, '/private')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5002, debug=True)


"""
http://polyglot.ninja/securing-rest-apis-basic-http-authentication-python-flask/

iniciar la aplicacion
$ python app_base_auth.py

probar recurso
$ curl -X GET http://localhost:5002/api/v2/private

probar recurso con credenciales
$ curl -X GET http://localhost:5002/api/v2/private --user admin:SuperSecretPwd

instalar dependencias 
$ pip install flask
$ pip install flask-restful
$ pip install Flask-HTTPAuth

generar el archivo requirements
$ pip freeze > requirements.txt

instalar dependencias con requirements
$ pip install -r requirements.txt

"""