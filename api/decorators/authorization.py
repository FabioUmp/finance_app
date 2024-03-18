from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from ..services import account_service, operation_service
from flask import make_response, jsonify

def user_account(view_function):
    @wraps(view_function)
    def decorator(*args, **kwargs):
        verify_jwt_in_request()
        user_logged = get_jwt_identity()
        account = account_service.list_account_by_id(kwargs["id"])
        if account is None:
            return make_response(jsonify("Conta não encontrada"), 404)
        elif account.user_id == user_logged:
            return view_function(*args, **kwargs)
        else:
            return make_response(jsonify("Esta conta não pertence ao usário logado"), 403)
    return decorator 

def user_operation(view_function):
    @wraps(view_function)
    def decorator(*args, **kwargs):
        verify_jwt_in_request()
        user_logged = get_jwt_identity()
        operation =  operation_service.list_operation_by_id(**kwargs['id'])
        if operation is None:
            return make_response(jsonify("Operação não encontrada"), 404)
        else:
            account = account_service.list_account_by_id(operation.account_id)
            if account.user_id == user_logged:
                return view_function(*args, **kwargs)
            else:
                return make_response(jsonify("Esta operação não pertence ao usuário logado"), 403) 
    return decorator 