
PRICES = {"A": 50,
          "B": 30,
          "C": 20,
          "D": 15,
          "E": 40}

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
        
    # We always start with E - it should be applied before B's as it's the
    # cheaper way.        
    if sku_to_count["E"] >= 2:
        if sku_to_count["B"] > 0:
            sku_to_count["B"] -= 1

    if sku_to_count["A"] >= 5:
        cost += 200 * (sku_to_count["A"] // 5)
        sku_to_count["A"] = sku_to_count["A"] % 5
        
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
    
