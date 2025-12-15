# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")

#count and print apples
apple_count = shelf.count("apples")
print("Number of Apples:", apple_count)

#find banana index and print it 
banana_index = shelf.index("bananas")
print("First Banana Index:", banana_index)
#print("First Banana Index:", shelf.index("bananas"))
count_bananas = shelf.count("bananas")

#check stock of apples
if count_bananas <= 5:
    print("Apples need to be restocked.")
else :
    Print("Apples are sufficiently stocked.")

#count stock of grapes
grapes_count = shelf.count("grapes")
if grapes_count <= 1:
    print("Grapes need to be restocked.")
else :
    print("Grapes are sufficiently stocked.")

#use In to check if a word is inside a list
if "oranges" in shelf :
    print("Oranges are at index:", shelf.index("oranges"))
else :
    print ("Oranges are out of stock.")