from flask import Blueprint, jsonify
from algorithms.random_forest import listing_prediction


random_forest_bp = Blueprint(
    "random_forest",
    __name__
)


@random_forest_bp.route(
    "/api/random-forest",
    methods=["GET"]
)
def random_forest_prediction():

    df = listing_prediction()


    summary = {

        "total_products": len(df),

        "actual_revenue":
            float(df["Revenue"].sum()),

        "predicted_revenue":
            float(df["PredictedRevenue"].sum())
    }


    return jsonify({

        "summary": summary,

        "predictions":
            df.to_dict(
                orient="records"
            )

    })