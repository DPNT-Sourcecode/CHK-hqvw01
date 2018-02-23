
PRICES = {"A": 50,
          "B": 30,
          "C": 20,
          "D": 15}

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    
    if not isinstance(skus, unicode):
        return -1
        
    for item in skus:
        if item not in PRICES:
            return -1
        
    skus = str(skus)
    cost = 0
    sku_to_count = {}
    for sku in PRICES:
        sku_to_count[sku] = skus.count(sku)
        
    # Apply special offers.
    if sku_to_count["A"] >= 3:
        cost += 130 * (sku_to_count["A"] // 3)
        sku_to_count["A"] = sku_to_count["A"] % 3
    
    if sku_to_count["B"] >= 2:
        cost += 45 * (sku_to_count["B"] // 2)
        sku_to_count["B"] = sku_to_count["B"] % 2
    
    # Now iterate over and add the remaining prices
    for item in PRICES:
        cost += (sku_to_count[item] * PRICES[item])
        
    return cost
    
