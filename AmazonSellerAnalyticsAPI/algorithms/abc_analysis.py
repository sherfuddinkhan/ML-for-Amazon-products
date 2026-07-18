from database import Database

def abc_analysis():
    db = Database()
    df = db.execute_query("""
        SELECT *
        FROM vwProductSales
    """)

    # Use TotalSales not Revenue - check your view screenshot
    df = df.sort_values(
        by="TotalSales",
        ascending=False
    )

    total = df["TotalSales"].sum()
    if total == 0:
        return []

    df["Percent"] = df["TotalSales"] / total * 100
    df["Cumulative"] = df["Percent"].cumsum()

    def category(x):
        if x <= 80:
            return "A"
        elif x <= 95:
            return "B"
        return "C"

    df["ABC"] = df["Cumulative"].apply(category)

    return df.to_dict(orient="records")