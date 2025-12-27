# List of products with their initial stock levels at the start of the week
products = [
    ["Apples", 150],  
    ["Bananas", 200],
    ["Oranges", 100],
    ["Mangoes", 120]
]
# List of products sold by the end of the week
units_sold = [["Apples", 30], ["Bananas", 45], ["Oranges", 20], ["Mangoes", 10]]
# New shipment received at the end of the week
shipment_received = [["Apples", 50], ["Bananas", 70], ["Oranges", 30], ["Mangoes", 40]]
#for to list the products, substract sold
for prods in range(len(products)):
    current_stock = products[prods][1]
    sold = units_sold[prods][1]
    products[prods][1] = current_stock - sold
#for to add recived 
for prods in range(len(products)):
    current_stock = products[prods][1]
    recieved = shipment_received[prods][1]
    products[prods][1] = current_stock + recieved

print("Final stock levels for all products:",products)
