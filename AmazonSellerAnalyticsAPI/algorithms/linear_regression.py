from database import Database
from sklearn.linear_model import LinearRegression

def sales_prediction():
    db = Database()
    df = db.execute_query("SELECT * FROM vwProductSales")

    # Your screenshot: TotalUnitsSold = 4, TotalSales = 100.00
    X = df[["TotalUnitsSold"]]  # NOT TotalSold
    y = df["TotalSales"]        # NOT Revenue

    model = LinearRegression()
    model.fit(X, y)
    df["PredictedRevenue"] = model.predict(X)

    return df.to_dict(orient="records")