from database import Database

from sklearn.ensemble import IsolationForest

def detect_anomaly():
    db = Database()

    df = db.execute_query("""
        SELECT *
        FROM vwFinance
    """)

    X = df[[
        "Charges",
        "Fees",
        "Taxes",
        "Settlement"
    ]]

    model = IsolationForest(random_state=42)

    df["Anomaly"] = model.fit_predict(X)

    return df.to_dict(orient="records")

