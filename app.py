from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Resource, Api
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_marshmallow import Marshmallow

import sys
import os.path
import json

from api.login import login, Registration, userinfo, logout, refresh_token

app = Flask(__name__)
app.config.from_file(os.path.join('config', 'config.json'), load=json.load)

jwt = JWTManager(app)
api = Api(app)
bcrypt = Bcrypt(app)
CORS(app)
ma = Marshmallow(app)

api.add_resource(Registration, '/register')
api.add_resource(login, '/login')

# there should a middleware
api.add_resource(userinfo, '/api/auth/userinfo')
api.add_resource(logout, '/api/auth/logout')
api.add_resource(refresh_token, '/api/auth/refresh')

@app.after_request
def apply_caching(response):
    response.headers["X-Frame-Options"] = "SAMEORIGIN"
    response.headers["HTTP-HEADER"] = "VALUE"
    return response

if __name__ == "__main__":
    app.run()