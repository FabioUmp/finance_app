from ..models import user_model
from api import db

def register_user(user):
    user = user_model.User(name=user.name, email=user.email, password=user.password)
    user.crypt_password()
    db.session.add(user)
    db.session.commit()
    return user

def list_user_by_email(email):
    return user_model.User.query.filter_by(email=email).first()  

def list_user_by_id(id):
    return user_model.User.query.filter_by(id=id).first()    
