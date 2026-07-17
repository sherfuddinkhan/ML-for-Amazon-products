from database import Database
from sklearn.linear_model import LinearRegression

def sales_prediction():

    db = Database()

    df = db.execute_query("""
        SELECT *
        FROM vwProductSales
    """)

    X = df[["TotalSold"]]

    y = df["Revenue"]

    model = LinearRegression()

    model.fit(X, y)

    df["PredictedRevenue"] = model.predict(X)

    return df