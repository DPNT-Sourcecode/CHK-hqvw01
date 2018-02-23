
# Basic price table, without offers 
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
          "K": 70,
          "L": 90,
          "M": 15,
          "N": 40,
          "O": 10,
          "P": 50,
          "Q": 30,
          "R": 50,
          "S": 20,
          "T": 20,
          "U": 40,
          "V": 50,
          "W": 20,
          "X": 17,
          "Y": 20,
          "Z": 21}
#------------------------------------------------------------------------------
# Offer Functions
#   - The names of the functions should make their purpose fairly clear.
#------------------------------------------------------------------------------
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
    
def any_3_stxyz_45(sku_to_count, cost):
    # note that the following is in order of decreasing price.
    products = ["Z", "Y", "S", "T", "X"]
    number_of_items = sum([sku_to_count[item] for item in products])
 
#------------------------------------------------------------------------------
# End offer functions
#------------------------------------------------------------------------------ 
  
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
        
    sku_to_count = x_get_one_y_free(sku_to_count, "E", 2, "B")

    # As above for R.
    sku_to_count = x_get_one_y_free(sku_to_count, "R", 3, "Q")
    
    # Begin remaining offers in order.
    sku_to_count, cost = x_for_y(sku_to_count, cost, "A", 5, 200)
    sku_to_count, cost = x_for_y(sku_to_count, cost, "A", 3, 130)
    
    sku_to_count, cost = x_for_y(sku_to_count, cost, "B", 2, 45)
    
    sku_to_count = x_get_x_free(sku_to_count, "F", 3)
    
    sku_to_count, cost = x_for_y(sku_to_count, cost, "H", 10, 80)
    sku_to_count, cost = x_for_y(sku_to_count, cost, "H", 5, 45)
    
    sku_to_count, cost = x_for_y(sku_to_count, cost, "K", 2, 120)
    
    sku_to_count = x_get_one_y_free(sku_to_count, "N", 3, "M")
 
    sku_to_count, cost = x_for_y(sku_to_count, cost, "P", 5, 200)
    
    sku_to_count, cost = x_for_y(sku_to_count, cost, "Q", 3, 80)
    
    sku_to_count = x_get_x_free(sku_to_count, "U", 4)
    
    sku_to_count, cost = x_for_y(sku_to_count, cost, "V", 3, 130)
    sku_to_count, cost = x_for_y(sku_to_count, cost, "V", 2, 90)
    
    
    # Now iterate over and add the remaining prices
    for item in PRICES:
        cost += (sku_to_count[item] * PRICES[item])
        
    return cost
    
