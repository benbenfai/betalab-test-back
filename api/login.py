
from flask import request, make_response, abort
from flask.json import jsonify

from flask_restful import Resource

class login(Resource):
    def get(self):

        try:

            return make_response(jsonify({
                'test': 'test',
            }))
            
        except:

            abort(403)
