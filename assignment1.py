# Item names and Quantity
milk = 9
sugar = 5
candy = 54
chocolate = 90
bottle_water  = 23
biscuit = 10
doughnut = 40

# Calculation of the entire stock in the shop
total = milk + sugar + candy + chocolate + bottle_water + biscuit + doughnut

# Finding the item with the highest quantity
highest_stock = max(milk,sugar,candy,chocolate,bottle_water,biscuit,doughnut)

# Finding the item with the lowest quantity
lowest_stock = min(milk,sugar,candy,chocolate,bottle_water,biscuit,doughnut)

# Printing the result to the user
print(f"The total value of stock in the shop is {total}\n")
print(f"The highest value of item in the shop is {highest_stock}\n")
print(f"The lowest value of item in the shop is {lowest_stock}")