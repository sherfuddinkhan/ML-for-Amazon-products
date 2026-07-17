from flask import Blueprint, jsonify
from algorithms.isolation_forest import detect_anomaly


anomaly_detection_bp = Blueprint(
    "anomaly_detection",
    __name__
)


@anomaly_detection_bp.route(
    "/api/anomaly-detection",
    methods=["GET"]
)
def anomaly_detection():

    try:

        result = detect_anomaly()

        return jsonify({
            "status": "success",
            "data": result
        })


    except Exception as e:

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500