# algorithms/apriori.py - REPLACE FULL FILE
from database import Database
from itertools import combinations
from collections import defaultdict

def apriori_analysis(min_support=0.02, min_confidence=0.3):
    db = Database()
    # YOUR WORKING QUERY FROM SSMS SCREENSHOT
    df = db.execute_query("""
        SELECT
            fs.CustomerKey,
            dp.SKU as ProductName
        FROM FactSales fs
        JOIN DimProduct dp ON fs.ProductKey = dp.ProductKey
    """)

    if df.empty:
        return {"total_transactions": 0, "frequent_itemsets": [], "association_rules": []}

    print(f"DB Rows: {len(df)}")

    transactions = df.groupby('CustomerKey')['ProductName'].apply(list).tolist()
    total = len(transactions)

    if total == 0:
        return {"total_transactions": 0, "frequent_itemsets": [], "association_rules": []}

    # Count 1-itemsets
    item_count = defaultdict(int)
    for trans in transactions:
        for item in set(trans):
            item_count[item] += 1

    frequent = {}
    for item, count in item_count.items():
        support = count / total
        if support >= min_support:
            frequent[frozenset([item])] = support

    # Count 2-itemsets - Same as your #Transactions JOIN
    pair_count = defaultdict(int)
    for trans in transactions:
        if len(set(trans)) < 2:
            continue
        for pair in combinations(set(trans), 2):
            pair_count[frozenset(pair)] += 1

    for pair, count in pair_count.items():
        support = count / total
        if support >= min_support:
            frequent[pair] = support

    # Rules
    rules = []
    for itemset, support in frequent.items():
        if len(itemset) < 2:
            continue
        for antecedent in combinations(itemset, 1):
            antecedent = frozenset(antecedent)
            consequent = itemset - antecedent
            if antecedent in frequent:
                confidence = support / frequent[antecedent]
                if confidence >= min_confidence:
                    rules.append({
                        "antecedent": list(antecedent)[0],
                        "consequent": list(consequent)[0],
                        "support": round(support, 4),
                        "confidence": round(confidence, 4),
                        "rule": f"{list(antecedent)[0]} -> {list(consequent)[0]}"
                    })

    rules_sorted = sorted(rules, key=lambda x: x['confidence'], reverse=True)

    return {
        "total_transactions": total,
        "frequent_itemsets": [{"items": list(k), "support": round(v,4)} for k,v in frequent.items()],
        "association_rules": rules_sorted
    }

if __name__ == "__main__":
    result = apriori_analysis()
    print(result)