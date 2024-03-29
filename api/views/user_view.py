from flask_restful import Resource
from api import api
from ..schemas import user_schema
from flask import request, make_response, jsonify
from ..entities import user
from ..services import user_service
from flask_jwt_extended import jwt_required


class UserList(Resource):
    @jwt_required()
    def post(self):
        us = user_schema.UserSchema()
        validate = us.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json["name"]
            email = request.json["email"] 
            password = request.json["password"] 
            new_user = user.User(name=name, email=email, password=password)
            result = user_service.register_user(new_user)
            return make_response(us.jsonify(result), 201)



api.add_resource(UserList, '/users')