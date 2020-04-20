# Contains Version 1 of myCalculator

from flask import Blueprint, request, jsonify
from simple import SimpleCalculator

mycalc_blueprint_v1 = Blueprint('simple_page', __name__)
calulator = SimpleCalculator()


@mycalc_blueprint_v1.route('/v1/calculate', methods=['GET'])
def login():
    # TODO: Validate headers(authtoken) if present
    try:
        if "expression" not in request.args:
            response = jsonify({"result": "No expression found"})
            response.status_code = 404
        else:
            calulator.run(request.args["expression"])
            if calulator.lcd == "Error":
                response = jsonify({"result": "Bad parameters"})
                response.status_code = 400
                return response
            response = jsonify({"result": calulator.lcd})
            response.status_code = 200
        return response
    except Exception as e:
        response = jsonify({
            "result": str(e)
        })
        response.status_code = 500
        return response
