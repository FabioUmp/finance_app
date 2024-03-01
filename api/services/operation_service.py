from api import db
from ..services import account_service
from ..models import operation_model, account_model

def register_operation(operation):
    db.session.add(operation)
    db.session.commit()
    account_service.debit_value(operation.account_id, operation, 2)
    return operation

def list_operation():
    operations = operation_model.Operation.query.all()
    return operations

def list_operation_by_id(id):
    operation = operation_model.Operation.query.filter_by(id=id).first()
    return operation  

def update_operation(operation, new_operation):
    old_value = operation.cost
    operation.name = new_operation.name
    operation.resume = new_operation.resume
    operation.cost = new_operation.cost
    operation.type = new_operation.type
    operation.account = new_operation.account
    db.session.commit()
    account_service.debit_value(new_operation.account, new_operation, 2, old_value)
    return operation

def delete_operation(operation):
    db.session.delete(operation)
    db.session.commit() 
    account_service.debit_value(operation.account_id, operation, 3) 
         