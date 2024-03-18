from api import api
from flask_restful import Resource
from flask import request, make_response, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity


class RefreshTokenList(Resource):
    @jwt_required(refresh=True)
    def post(self):
        logged_user = get_jwt_identity()
        access_token = create_access_token(
            identity=logged_user
        )
        refresh_token = create_refresh_token(
            identity=logged_user
        )
        return make_response(jsonify({
            'access_token':access_token,
            'refresh_token':refresh_token
        }), 200)
       
api.add_resource(RefreshTokenList, '/token/refresh')                     