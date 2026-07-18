from algorithms.kmeans import CustomerSegmentation

segment = CustomerSegmentation()
result = segment.perform_clustering()
print(result[["CustomerName", "TotalOrders", "TotalRevenue", "Cluster"]])