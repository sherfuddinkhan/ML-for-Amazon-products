# algorithms/kmeans.py

import pandas as pd
from sklearn.cluster import KMeans
from database import Database


class CustomerSegmentation:

    def __init__(self):
        self.db = Database()

    def load_data(self):

        query = """
        SELECT *
        FROM vwCustomerSales
        """

        dataframe = self.db.execute_query(query)

        return dataframe

    def perform_clustering(self):

        dataframe = self.load_data()

        features = dataframe[
            [
                "TotalOrders",
                "TotalQuantity",
                "TotalRevenue",
                "AverageOrderValue"
            ]
        ]

        model = KMeans(
            n_clusters=3,
            random_state=42
        )

        dataframe["Cluster"] = model.fit_predict(features)

        return dataframe