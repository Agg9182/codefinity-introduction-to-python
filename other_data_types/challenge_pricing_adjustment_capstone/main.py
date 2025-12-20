grocery_inventory = {

"Milk": ("Dairy", 3.50, 8),
"Eggs": ("Dairy", 5.50, 30),
"Bread": ("Bakery", 2.99, 15),
"Apples": ("Produce", 1.50, 50),    
}
#check eggs price
eggs_tuple = grocery_inventory["Eggs"]
eggs_price = eggs_tuple[1]
#print(eggs_price)
if eggs_price >=5 :
    print("Eggs are too expensive, reducing the price by $1.")
    eggs_price = eggs_price - 1
    #print(eggs_price)
    grocery_inventory.update({"Eggs": ("Dairy", eggs_price, 30)})
else :
    print("The price of Eggs is reasonable.")


#update inventory
grocery_inventory.update({"Tomatoes": ("Produce",1.20,30)})
print("Inventory after adding Tomatoes:",grocery_inventory)

#check milk stock 
milk_tuple = grocery_inventory["Milk"]
milk_stock = milk_tuple [2]
if milk_stock <= 10 :
   print ("milk needs to be restocked. Increasing stock by 20 units.") 
   milk_stock = milk_stock + 20 
   grocery_inventory.update({"Milk": ("Dairy", 3.5, milk_stock)}) 
else :
    print("Milk has sufficient stock.")

#apple price 
apple_tuple = grocery_inventory["Apples"]
apple_price = apple_tuple[1]
if apple_price > 2 :
   grocery_inventory.pop("Apples")
   print("Apples removed from inventory due to high price.")

print("updated inventory:",grocery_inventory)
