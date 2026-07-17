import pandas as pd
from database import Database
from sklearn.ensemble import RandomForestRegressor


def listing_prediction():

    db = Database()


    query = """
    SELECT
        ProductKey,
        ProductName,
        TotalSold,
        Revenue
    FROM vwProductSales
    """


    df = db.execute_query(query)


    # Features
    X = df[
        [
            "TotalSold"
        ]
    ]


    # Target
    y = df["Revenue"]


    # Model
    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )


    # Train
    model.fit(X, y)


    # Prediction
    df["PredictedRevenue"] = model.predict(X)


    return df