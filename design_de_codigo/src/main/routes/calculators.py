from flask import Blueprint, jsonify, request
from src.calculators.calculator_1 import Calculator1

calc_routes_bg = Blueprint("cal_routes", __name__)

@calc_routes_bg.route("/calculator/1", methods=["POST"])
def calculator_1():
    cal = Calculator1()
    response = cal.calculate(request)
    return jsonify(response), 200