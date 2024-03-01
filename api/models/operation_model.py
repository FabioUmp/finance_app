from api import db
import enum

class TypeEnum(enum.Enum):
    deposit = 1
    withdrawal = 2

class Operation(db.Model):
    __tablename__='operation'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    resume = db.Column(db.String(100), nullable=False)
    cost = db.Column(db.Float, nullable=False)
    type = db.Column(db.Enum(TypeEnum), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey("account.id"))
    account = db.relationship("Account", backref=db.backref("operations", lazy="dynamic"))
