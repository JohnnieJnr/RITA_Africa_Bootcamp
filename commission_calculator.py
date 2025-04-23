# User input
total_sales_amnt = float(input("What is the total sales amount: "))

commission_percentage = float(input("what is the commission percentage: "))

# Commission calculation
commission = commission_percentage / 100 * total_sales_amnt

# Result
print(f"The commission percentage of the total sales is {commission}")
