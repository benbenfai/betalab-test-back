from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Resource, Api
from flask_bcrypt import Bcrypt
from flask_cors import CORS

import sys
import os.path
import json

from api.login import login, Registration

app = Flask(__name__)
app.config.from_file(os.path.join('config', 'config.json'), load=json.load)

jwt = JWTManager(app)
api = Api(app)
bcrypt = Bcrypt(app)
CORS(app)

@app.route("/")
def hello_world():
    print(123)
    return "<p>Hello, World!</p>"

#pw_hash = bcrypt.generate_password_hash('123').decode('utf-8')
#print(pw_hash)

api.add_resource(login, '/login')
api.add_resource(Registration, '/register')

if __name__ == "__main__":
    app.run()