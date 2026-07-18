# test__apriori.py
from algorithms.apriori import apriori_analysis

result = apriori_analysis()
print(f"\nTotal Transactions: {result['total_transactions']}")
print("Rules:")
for r in result['association_rules']:
    print(r)