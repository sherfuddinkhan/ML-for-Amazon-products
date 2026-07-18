import pandas as pd
from database import Database
from sklearn.ensemble import RandomForestRegressor

def listing_prediction():
    db = Database()

    query = """
    SELECT
        ProductKey,
        ProductName,
        TotalUnitsSold,
        TotalSales
    FROM vwProductSales
    """

    df = db.execute_query(query)

    if df.empty:
        return df

    # Features - your view has TotalUnitsSold
    X = df[["TotalUnitsSold"]]

    # Target - your view has TotalSales
    y = df["TotalSales"]

    # Model
    model = RandomForestRegressor(
        n_estimators=100,
        random_state=42
    )

    # Train
    model.fit(X, y)

    # Prediction
    df["PredictedRevenue"] = model.predict(X)

    return df.to_dict(orient="records")