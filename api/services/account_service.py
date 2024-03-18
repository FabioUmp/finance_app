from api import db
from ..models import account_model


def register_account(account):
    account = account_model.Account(name=account.name, resume=account.resume, value=account.value, user_id=account.user)
    db.session.add(account)
    db.session.commit()
    return account

def list_account(user):
    accounts = account_model.Account.query.filter_by( user_id=user).all()
    return accounts

def list_account_by_id(id):
    account = account_model.Account.query.filter_by(id=id).first()
    return account

def update_account(account, new_account):
    account.name = new_account.name
    account.resume = new_account.resume
    account.value = new_account.value
    db.session.commit()
    return account

def delete_account(account):
    db.session.delete(account)
    db.session.commit()   

def debit_value(account_id, operation, function_type, old_value=None):
    account = account_model.Account.query.filter_by(id=account_id).first()
    #function_type -> 1 = Cadastro de Operação
    #function_type -> 2 = Atualização de Operação
    #function_type -> 3 = Remoção de Operação
    if function_type == 1:
        if operation.type == "deposit":
            account.value = account.value + operation.cost
        else:
            account.value = account.value - operation.cost
    elif function_type == 2:
        if operation.type == "deposit":
            account.value = account.value - old_value
            account.value = account.value + operation.cost
        else:
            account.value = account.value + operation.cost
            account.value = account.value - operation.cost
    else:
        if operation.type.value == "deposit":
            account.value = account.value - operation.cost 
        else:
             account.value = account.value + operation.cost           
    db.session.commit()
    return account   