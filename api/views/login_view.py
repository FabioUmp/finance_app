from api import api
from flask_restful import Resource
from ..schemas import login_schema
from flask import request, make_response, jsonify
from ..services import user_service
from flask_jwt_extended import create_access_token, create_refresh_token
from datetime import timedelta

class LoginList(Resource):
    def post(self):
        ls = login_schema.LoginSchema()
        validate = ls.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            email = request.json["email"]
            password = request.json["password"]

            user = user_service.list_user_by_email(email) 

            if user and user.decrypt_password(password):
                access_token = create_access_token(
                    identity=user.id,
                    expires_delta=timedelta(seconds=60)
                )
                refresh_token = create_refresh_token(
                    identity=user.id
                ) 
                return make_response(jsonify({
                    'access_token':access_token,
                    'refresh_token':refresh_token,
                    'message':'Loogin efetuado com sucesso'
                }), 200)
            else:
                return make_response(jsonify({
                    'message':'credenciais inválidas'
                })) 

api.add_resource(LoginList, '/login')                     