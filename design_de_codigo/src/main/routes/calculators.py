from flask import Blueprint, jsonify, request
from src.main.factories.calculator1_factory import calculator_1_factory
from src.main.factories.calculator2_factory import calculator_2_factory
from src.main.factories.calculator3_factory import calculator_3_factory

calc_routes_bg = Blueprint("cal_routes", __name__)

@calc_routes_bg.route("/calculator/1", methods=["POST"])
def calculator_1():
    cal = calculator_1_factory()
    response = cal.calculate(request)
    
    return jsonify(response), 200

@calc_routes_bg.route("/calculator/2", methods=["POST"])
def calculator_2():
    cal = calculator_2_factory()
    response = cal.calculate(request)

    return jsonify(response), 200

@calc_routes_bg.route("/calculator/3", methods=["POST"])
def calculator_3():
    cal = calculator_3_factory()
    response = cal.calculate(request)

    return jsonify(response), 200

