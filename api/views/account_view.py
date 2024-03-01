from flask_restful import Resource
from ..schemas import account_schema
from flask import request, make_response, jsonify
from ..entities import account
from ..services import account_service
from api import api


class AccountList(Resource):
    def get(self):
     accounts = account_service.list_account()
     cs = account_schema.AccountSchema(many=True)
     return make_response(cs.jsonify(accounts), 201)    
    def post(self):
        cs = account_schema.AccountSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json["name"]
            resume = request.json["resume"]
            value = request.json["value"]  
            new_account = account.Account(name=name, resume=resume, value=value)
            result = account_service.register_account(new_account)
            return make_response(cs.jsonify(result), 201) 

class AccountDetail(Resource):
    def get(self, id):
        account = account_service.list_account_by_id(id)
        if account is None:
            return make_response(jsonify("Conta não encontrada"), 404)
        cs = account_schema.AccountSchema()
        return make_response(cs.jsonify(account), 200) 
    def put(self, id):
        old_account = account_service.list_account_by_id(id)
        if old_account is None:
             return make_response(jsonify("Conta não encontrada"), 404)
        cs = account_schema.AccountSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json["name"]
            resume = request.json["resume"]
            value = request.json["value"]
            new_account = account.Account(name=name, resume=resume, value=value)
            result = account_service.update_account(old_account, new_account)
            return make_response(cs.jsonify(result), 201)
    def delete(self, id):
        account = account_service.list_account_by_id(id)
        if account is None:
            return make_response(jsonify("Conta não encontrada"), 404)
        account_service.delete_account(account)
        return make_response(jsonify(""), 204)             



api.add_resource(AccountList, '/contas') 
api.add_resource(AccountDetail, '/contas/<int:id>')            
