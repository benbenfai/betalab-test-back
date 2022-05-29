from flask import request, make_response, abort
from flask.json import jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from flask_restful import Resource

from database.user import UserTool
from untity.encry import Tool,Model
from untity.auth import auth_required, authenticate_user, get_authenticated_user, auth_refresh_required, deauthenticate_user, refresh_authentication

from schema.user_schema import LoginSchema,registerSchema

encrypt = Model()
login_schema = LoginSchema(many=False)
register_schema = registerSchema(many=False)
getdata = Tool()

class login(Resource):
    
    def post(self):

        try:

            result = login_schema.load(getdata.get_param())

            access_token, refresh_token = authenticate_user(result['username'], result['password'])

            return make_response(jsonify({
                'access_token': access_token,
                'refresh_token': refresh_token,
            }))

        except:

            abort(403)

class Registration(Resource):

    def post(self):

        result = register_schema.load(getdata.get_param())

        user = UserTool.get_user(result['username']) 

        if user != None:
            return {
                'message': 'username {0} is exist!'.format(result['username'])
            }, 403
        else:
            try:
                user = UserTool()
                user.add_user(result['username'],encrypt.generate_hash(result['password']),result['email'],result['address'],result['phone'],result['picture'],result['company'])
                access_token = create_access_token(identity = result['username'])
                refresh_token = create_refresh_token(identity = result['username'])
                return {
                    'message': 'Registration success',
                    'access_token': access_token,
                    'refresh_token': refresh_token
                    }
            except:
                return {
                    'message': 'database insert error',
                    }

class userinfo(Resource):

    @auth_required
    def get(self):

        try:
            user = get_authenticated_user()

            return make_response(jsonify({
                'username': user[0],
                'enabled': user[1],
            }))
        except:

            abort(403)

class logout(Resource):

    @auth_refresh_required
    def post():

        deauthenticate_user()
        return make_response()

class refresh_token(Resource):

    @jwt_required(refresh=True)
    def post():
        identity = get_jwt_identity()
        access_token = create_access_token(identity=identity)
        return jsonify(access_token=access_token)