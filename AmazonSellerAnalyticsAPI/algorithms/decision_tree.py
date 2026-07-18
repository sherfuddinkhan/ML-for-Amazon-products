from database import Database
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

def return_prediction():
    db = Database()
    df = db.execute_query("SELECT * FROM vwShipping")

    # FactShipping has: ShippingID, SaleID, ShipmentStatus, DeliveryDays, Returned
    print(df.head())
    
    if df.empty:
        return df

    # Encode ShipmentStatus Delivered/Shipped etc to numbers
    df["ShipmentStatus"] = df["ShipmentStatus"].astype("category").cat.codes

    X = df[["ShipmentStatus", "DeliveryDays"]]
    y = df["Returned"].astype(int)  # BIT -> int for sklearn

    model = DecisionTreeClassifier(random_state=42)
    model.fit(X, y)

    df["Prediction"] = model.predict(X)
    
    return df

if __name__ == "__main__":
    df = return_prediction()
    print(df)