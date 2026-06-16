from flask import Flask

from src.main.routes.bank_account_routes import banck_routes_dp
from src.models.settings.db_connection_handle import db_connection_handler

db_connection_handler.connect()

app = Flask(__name__)

app.register_blueprint(banck_routes_dp)
