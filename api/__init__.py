from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_marshmallow import Marshmallow
from flask_restful import Api

load_dotenv()

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)

ma = Marshmallow(app)

mi = Migrate(app, db)

api = Api(app)

from .models import account_model, operation_model
from .views import account_view, operation_view





