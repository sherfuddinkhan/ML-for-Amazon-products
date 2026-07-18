import pandas as pd
from sklearn.cluster import KMeans
from database import Database

class CustomerSegmentation:
    def __init__(self):
        self.db = Database()

    def load_data(self):
        return self.db.execute_query("SELECT * FROM vwCustomerSales")

    def perform_clustering(self):
        dataframe = self.load_data()
        
        if dataframe.empty:
            return dataframe

        features = dataframe[[
            "TotalOrders",
            "TotalQuantity",
            "TotalRevenue",
            "AverageOrderValue"
        ]]

        model = KMeans(n_clusters=3, random_state=42)
        dataframe["Cluster"] = model.fit_predict(features)
        return dataframe