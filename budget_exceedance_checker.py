#
budget = float(input("Enter your monthly budget: "))
expenses = float(input("Enter your monthly expenses: "))
print("\n")

# Using comparison operators to check if the some coditions are True or False
over_budget = expenses > budget
within_budget = expenses < budget
ex_budget = expenses == budget

#Using assignment operators for reward and penalties.
if over_budget == True:
    budget -= 10
    print(f"A penalty of 10 was deducted for going over your budget. Your current amount is {budget}")
if within_budget == True:
    budget += 10
    print(f"A reward of 10 was added to your budget for staying withing your budget. Your current budget is {budget}")
    print("\n")

#results
print(f"Are you over budget? {over_budget}")
print(f"Are you within budget? {within_budget}")
print(f"Have you spent exaclty your budget? {ex_budget}")