from flask import Blueprint, jsonify
from algorithms.decision_tree import return_prediction

decision_tree_bp = Blueprint(
    "decision_tree",
    __name__
)

@decision_tree_bp.route(
    "/api/decision-tree",
    methods=["GET"]
)
def get_return_prediction():

    df = return_prediction()

    summary = {
        "total_shipments": len(df),
        "returned_orders": int(df["Returned"].sum()),
        "predicted_returns": int(df["Prediction"].sum())
    }

    return jsonify({
        "summary": summary,
        "predictions": df.to_dict(orient="records")
    })