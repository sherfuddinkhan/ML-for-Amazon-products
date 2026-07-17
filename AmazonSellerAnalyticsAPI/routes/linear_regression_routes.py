from flask import Blueprint, jsonify
from algorithms.linear_regression import sales_prediction


linear_regression_bp = Blueprint(
    "linear_regression",
    __name__
)

@linear_regression_bp.route(
    "/api/linear-regression",
    methods=["GET"]
)
def get_sales_prediction():

    df = sales_prediction()

    summary = {
        "total_products": len(df),
        "total_revenue": float(df["Revenue"].sum()),
        "average_revenue": float(df["Revenue"].mean())
    }

    predictions = df.to_dict(orient="records")

    return jsonify({
        "summary": summary,
        "predictions": predictions
    })