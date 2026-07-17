from flask import Flask
from flask_cors import CORS

# Import Blueprint
from routes.kmeans_routes import kmeans_bp
from routes.linear_regression_routes import linear_regression_bp
from routes.decision_tree_routes import decision_tree_bp
from routes.random_forest_routes import random_forest_bp
from routes.isolation_forest_routes import anomaly_detection_bp

from routes.abc_analysis_routes import analytics_bp



# Create Flask App
app = Flask(__name__)

# Enable CORS
CORS(app)

# Register Routes
app.register_blueprint(kmeans_bp)
app.register_blueprint(linear_regression_bp)
app.register_blueprint(decision_tree_bp)
app.register_blueprint(random_forest_bp)
app.register_blueprint(anomaly_detection_bp)
app.register_blueprint(analytics_bp,url_prefix="/api")


# Home Route
@app.route("/")
def home():
    return {
        "message": "Amazon Seller Analytics API is Running",
        "status": "success"
    }


# Run Flask Application
if __name__ == "__main__":
    app.run(debug=True)