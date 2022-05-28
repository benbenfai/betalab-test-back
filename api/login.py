from flask import request, make_response, abort
from flask.json import jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from flask_restful import Resource

from database.user import UserModel
from untity.encry import Model

encrypt = Model()

class login(Resource):

    def get(self):

        try:

            return make_response(jsonify({
                'test': 'test',
            }))

        except:

            abort(403)
    
    def post(self):

        try:
            
            username = request.json.get('username', None) 
            password = request.json.get('password', None) 

            if username != 'test' or password != 'test': 
                return jsonify({"msg": "Bad username or password"}), 401

            access_token = create_access_token(identity=username)
            #access_token, refresh_token = authenticate_user(username, password)
            #return jsonify(access_token=access_token)

            return make_response(jsonify({
                'access_token': access_token,
                'test': 'test',
            }))

        except:

            abort(403)

class Registration(Resource):

    def post(self):

        print(request.json)

        username = request.json.get('username', None) 
        password = request.json.get('password', None)
        email = request.json.get('email', None)
        address = request.json.get('address', None) 
        phone = request.json.get('phone', None) 
        picture= request.json.get('picture', None) 
        company = request.json.get('company', None)

        user = UserModel.get_user(username) 

        if user != None:
            return {
                'message': 'username {0} is exist!'.format(username)
            }, 403
        else:
            try:
                user = UserModel(username,encrypt.generate_hash(password),email,address,phone,picture,company)
                user.add_user()
                access_token = create_access_token(identity = username)
                refresh_token = create_refresh_token(identity = username)
                return {
                    'message': 'Registration success',
                    'access_token': access_token,
                    'refresh_token': refresh_token
                    }
            except:
                return {
                    'message': 'database insert error',
                    }
