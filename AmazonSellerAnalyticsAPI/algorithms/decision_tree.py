from database import Database
from sklearn.tree import DecisionTreeClassifier

def return_prediction():

    db = Database()

    df = db.execute_query("""
        SELECT *
        FROM vwShipping
    """)

    df["ShipmentStatus"] = df["ShipmentStatus"].astype("category").cat.codes

    X = df[
        [
            "ShipmentStatus",
            "DeliveryDays"
        ]
    ]

    y = df["Returned"]

    model = DecisionTreeClassifier(random_state=42)

    model.fit(X, y)

    df["Prediction"] = model.predict(X)

    return df