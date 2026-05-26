from flask import Blueprint, jsonify, request
from src.main.factories.calculator1_factory import calculator_1_factory
from src.main.factories.calculator2_factory import calculator_2_factory
from src.main.factories.calculator3_factory import calculator_3_factory

from src.errors.error_controller import handle_errors

calc_routes_bg = Blueprint("cal_routes", __name__)

@calc_routes_bg.route("/calculator/1", methods=["POST"])
def calculator_1():
    try:
        cal = calculator_1_factory()
        response = cal.calculate(request)
        
        return jsonify(response), 200
    except Exception as exception:
        error_response = handle_errors(exception)
        return jsonify(error_response["body"], error_response["status_code"])

@calc_routes_bg.route("/calculator/2", methods=["POST"])
def calculator_2():
    try:
        cal = calculator_2_factory()
        response = cal.calculate(request)

        return jsonify(response), 200
    except Exception as exception:
        error_response = handle_errors(exception)
        return jsonify(error_response["body"], error_response["status_code"])

@calc_routes_bg.route("/calculator/3", methods=["POST"])
def calculator_3():
    try:
        cal = calculator_3_factory()
        response = cal.calculate(request)

        return jsonify(response), 200
    except Exception as exception:
        error_response = handle_errors(exception)
        return jsonify(error_response["body"], error_response["status_code"])

