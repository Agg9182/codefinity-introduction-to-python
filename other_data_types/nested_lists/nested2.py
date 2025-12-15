# Define individual grocery items as lists containing details
bread = ["Bread", 4.80, 3, "Gluten Free"] # Item name, price quantity, type
milk = ["Milk", 5.99, 2, "2% Milk"] # Item name, price, quantity,type
apple = ["Apple", 1.27, 12, "Fuji"] # Item name, price, quantity, type
# Create the main grocery list that contains these items
grocery_list = [bread, apple, milk]
print("Grocery List:" , grocery_list)
# Accessing and printing specific item details using indexing
print("Item:", grocery_list[2][0]) # Accesses "Milk" title
print("Price:", grocery_list[2][1]) # Accesses price of a Milk, whichis 5.99
print("Quantity:", grocery_list[2][2]) # Accesses quantity of Milk,which is 2
print("Type:", grocery_list[2][3]) # Accesses type of Milk, which is"2% Milk"
# Adding a new sublist item to the grocery list
onion = ["Onions", 1.30, 10, "Yellow"]
grocery_list.append(onion)
# Removing an item from the grocery list
grocery_list.remove(bread)
# Sorting the grocery list alphabetically
grocery_list.sort()
print("Updated Grocery List:", grocery_list)