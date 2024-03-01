from api import ma
from ..models import operation_model
from marshmallow import fields
from marshmallow_enum import EnumField

class OperationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = operation_model.Operation
        load_instance = True
        include_fk=True

    name = fields.String(required=True)
    resume = fields.String(required=True)
    cost = fields.Float(required=True)
    account_id = fields.Integer(required=True)
    type = EnumField(operation_model.TypeEnum)
