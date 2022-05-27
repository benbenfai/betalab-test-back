from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Resource, Api

import sys
import os.path
import json

from api.login import login

app = Flask(__name__)
app.config.from_file(os.path.join('config', 'config.json'), load=json.load)

jwt = JWTManager(app)
api = Api(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

api.add_resource(login, '/login')

if __name__ == "__main__":
    app.run()