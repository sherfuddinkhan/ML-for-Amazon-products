from flask import Blueprint, jsonify

from algorithms.abc_analysis import abc_analysis


analytics_bp = Blueprint(
    "analytics",
    __name__
)


@analytics_bp.route("/abc-analysis",methods=["GET"])
def abc_analysis_route():

    result = abc_analysis()

    return jsonify({
        "status": "success",
        "data": result
    })