# List of products on promotion for each weekday
daily_promotions = ["milk", "eggs", "bread", "apples", "oranges"]
# List of weekdays corresponding to the promotions
weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday"]

for day in range(5):
 weekdays1 = weekdays[day]
 promos = daily_promotions[day]
 print(f"{weekdays1}: promotion on {promos}")