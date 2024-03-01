from api import ma
from ..models import account_model
from marshmallow import fields
from ..schemas import operation_schema

class AccountSchema(ma.SQLAlchemyAutoSchema):
    operations = ma.Nested(operation_schema.OperationSchema, many=True, only=('name', 'resume', 'type', 'cost'))

    class Meta:
        model = account_model.Account
        load_instance = True

        name = fields.String(required=True)
        resume = fields.String(required=True)
        value = fields.String(required=True)