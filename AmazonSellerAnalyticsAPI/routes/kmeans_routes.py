from flask import Blueprint, jsonify
from algorithms.kmeans import CustomerSegmentation

kmeans_bp = Blueprint("kmeans", __name__)

@kmeans_bp.route("/api/kmeans", methods=["GET"])
def get_customer_segments():

    segment = CustomerSegmentation()

    df = segment.perform_clustering()

    total_customers = len(df)

    avg_order_value = float(df["AverageOrderValue"].mean())

    high_value = len(df[df["Cluster"] == 1])

    summary = {
        "total_customers": total_customers,
        "high_value_percentage": round(high_value / total_customers * 100, 2),
        "avg_order_value": avg_order_value,
        "num_clusters": int(df["Cluster"].nunique())
    }

    segments = []

    for cluster in sorted(df["Cluster"].unique()):

        cluster_df = df[df["Cluster"] == cluster]

        segments.append({
            "segment": f"Cluster {cluster}",
            "count": int(len(cluster_df)),
            "percentage": round(len(cluster_df) / total_customers * 100, 2),
            "avg_rfm_score": round(cluster_df["AverageOrderValue"].mean(), 2),
            "avg_order_value": round(cluster_df["AverageOrderValue"].mean(), 2),
            "characteristics": "Automatically generated customer cluster"
        })

    return jsonify({
        "summary": summary,
        "segments": segments
    })