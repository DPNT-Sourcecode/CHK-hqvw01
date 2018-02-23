

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    sku_to_count = {}
    for sku in ["A", "B", "C", "D"]:
        sku_to_count[sku] = skus.count(sku)
        
    
