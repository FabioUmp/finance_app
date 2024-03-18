from flask_restful import Resource
from ..schemas import operation_schema
from flask import request, make_response, jsonify
from ..entities import operation
from ..services import operation_service, account_service
from api import api
from flask_jwt_extended import jwt_required, get_jwt_identity
from ..decorators.authorization import user_operation

class OperationList(Resource):
    @jwt_required()
    def get(self):
        user = get_jwt_identity()
        operations = operation_service.list_operation(user)
        os = operation_schema.OperationSchema(many=True)
        return make_response(os.jsonify(operations), 201)
    @jwt_required()
    def post(self):
        os = operation_schema.OperationSchema()
        validate = os.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json["name"]
            resume = request.json["resume"]
            cost = request.json["cost"]
            type = request.json["type"]
            account = request.json["account_id"]
            if account_service.list_account_by_id(account) is None:
                return make_response("Conta não existe", 404)
            else:    
                new_operation = os.load(request.json)
            result = operation_service.register_operation(new_operation)
            return make_response(os.jsonify(result), 201) 

class OperationDetail(Resource):
    @user_operation
    def get(self, id):
        operation =  operation_service.list_operation_by_id(id)
        if operation is None:
            return make_response(jsonify("Operação não encontrada"), 404)
        os = operation_schema.OperationSchema()
        return make_response(os.jsonify(operation), 200)
    @user_operation
    def put(self, id):
        old_operation = operation_service.list_operation_by_id(id)
        if old_operation is None:
             return make_response(jsonify("Operação não encontrada"), 404)
        os = operation_schema.OperationSchema()
        validate = os.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json["name"]
            resume = request.json["resume"]
            cost = request.json["cost"]
            type = request.json["type"]
            account = request.json["account_id"]
            new_operation = operation.Operation(name=name, resume=resume, cost=cost, type=type, account=account)
            result = operation_service.update_operation(old_operation, new_operation)
            return make_response(os.jsonify(result), 201)
    @user_operation
    def delete(self, id):
        operation = operation_service.list_operation_by_id(id)
        if operation is None:
            return make_response(jsonify("Operação não encontrada"), 404)
        operation_service.delete_operation(operation)
        return make_response(jsonify(""), 204)                     

api.add_resource(OperationList, '/operations')
api.add_resource(OperationDetail, '/operations/<int:id>')      