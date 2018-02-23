
PRICES = {"A": 50,
          "B": 30,
          "C": 20,
          "D": 15,
          "E": 40,
          "F": 10,
          "G": 20,
          "H": 10,
          "I": 35,
          "J": 60,
          "K": 80,
          "L": 90,
          "M": 15,
          "N": 40,
          "O": 10,
          "P": 50,
          "Q": 30,
          "R": 50,
          "S": 30,
          "T": 20,
          "U": 40,
          "V": 50,
          "W": 20,
          "X": 90,
          "Y": 10,
          "Z": 50}

# noinspection PyUnusedLocal
# skus = unicode string

def x_for_y(sku_to_count, cost, product, number, item_cost):
    if sku_to_count[product] >= number:
        cost += item_cost * (sku_to_count[product] // number)
        sku_to_count[product] = sku_to_count[product] % number
    return (sku_to_count, cost)
    
def x_get_one_y_free(sku_to_count, buy_prod, number_of_buy, free_prod):
    if sku_to_count[buy_prod] >= number_of_buy:
        
        if sku_to_count[free_prod] > sku_to_count[buy_prod] // number_of_buy:
            sku_to_count[free_prod] -= (sku_to_count[buy_prod] // number_of_buy)
        else:
            sku_to_count[free_prod] = 0  
            
    return sku_to_count
    
def x_get_x_free(sku_to_count, product, number):
    if sku_to_count[product] >= 3:
        sku_to_count[product] -= sku_to_count[product] // number   
    return sku_to_count
    
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
        
    sku_to_count = x_get_one_y_free(sku_to_count, "E", 2, "B")

    # As above for R.
    sku_to_count = x_get_one_y_free(sku_to_count, "R", 3, "Q")
    
    # Begin remaining offers in order.
    sku_to_count, cost = x_for_y(sku_to_count, "A", 5, 200)
    
    offer = x_for_y(sku_to_count, "A", 3, 130)
    cost += offer[1]
    sku_to_count = offer[0]
    
    offer = x_for_y(sku_to_count, "B", 2, 45)
    cost += offer[1]
    sku_to_count = offer[0]
    
    sku_to_count = x_get_x_free(sku_to_count, "F", 3)
        
    offer = x_for_y(sku_to_count, "H", 5, 45)
    cost += offer[1]
    sku_to_count = offer[0]
    
    offer = x_for_y(sku_to_count, "H", 10, 80)
    cost += offer[1]
    sku_to_count = offer[0]
    
    offer = x_for_y(sku_to_count, "K", 2, 150)
    cost += offer[1]
    sku_to_count = offer[0]
    
    sku_to_count = x_get_one_y_free(sku_to_count, "N", 3, "M")
 
    offer = x_for_y(sku_to_count, "P", 5, 200)
    cost += offer[1]
    sku_to_count = offer[0]  
    
    offer = x_for_y(sku_to_count, "Q", 3, 80)
    cost += offer[1]
    sku_to_count = offer[0]
    
    sku_to_count = x_get_x_free(sku_to_count, "U", 3)
    
    offer = x_for_y(sku_to_count, "V", 2, 90)
    cost += offer[1]
    sku_to_count = offer[0]  
    
    offer = x_for_y(sku_to_count, "V", 3, 130)
    cost += offer[1]
    sku_to_count = offer[0]
    
    
    # Now iterate over and add the remaining prices
    for item in PRICES:
        cost += (sku_to_count[item] * PRICES[item])
        
    return cost
    
