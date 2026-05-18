from flask import Flask
from src.main.routes.calculators import calc_routes_bg

app = Flask(__name__)

app.register_blueprint(calc_routes_bg)