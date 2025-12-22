prices = [29.99, 45.50, 12.75, 38.20]
# List of grocery items
grocery_list = ["Apples", "Bananas", "Carrots", "Cucumbers"]
discountfactor = [.90,.80,.85,.95]
for cost in range(len(prices)):
    #apply disccount
    prices[cost] = prices[cost] * discountfactor[cost]
    #cost + 1 para imprimir indice desde 1 
    print(f"Updated price for item {cost + 1}: ${prices[cost]:.1f}")
    
    