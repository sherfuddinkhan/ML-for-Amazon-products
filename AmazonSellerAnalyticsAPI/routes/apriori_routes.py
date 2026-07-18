from flask import Blueprint, jsonify
from algorithms.apriori import apriori_analysis

apriori_bp = Blueprint("apriori", __name__)

@apriori_bp.route("/api/apriori", methods=["GET"])
def apriori():
    try:
        result = apriori_analysis()
        return jsonify({
            "status": "success",
            "data": result
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500