import jwt
import datetime
import time
from jwt.exceptions import ExpiredSignatureError

payload = {
    "uid": 23,
    "name": "admin",
    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=2)
}

SECRET_KEY = "N0TV3RY53CR3T"

token = jwt.encode(payload=payload, key=SECRET_KEY)

print("Generated Token: {}".format(token.decode()))

decoded_payload = jwt.decode(jwt=token, key=SECRET_KEY)

print(decoded_payload)


## con expiracion de 2 segundos
payload = {
    "uid": 25,
    "name": "admin2",
    "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=2)
}

token = jwt.encode(payload=payload, key=SECRET_KEY)

print("Generated Token2: {}".format(token.decode()))

time.sleep(4)  # wait 4 secs so the token expires

try:
    decoded_payload = jwt.decode(jwt=token, key=SECRET_KEY)
except ExpiredSignatureError as ex:
    print("ExpiredSignatureError:", ex)
else:
    print("No error")
finally:
    print("Finish")


print(decoded_payload)


"""
http://polyglot.ninja/understanding-jwt-json-web-tokens/

instalar dependencias
$ pip install pyjwt


"""