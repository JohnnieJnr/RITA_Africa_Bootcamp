def add_numbers(a, b):
    add = a + b
    return add

def sub_numbers(a, b):
    sub = a -b
    return sub

def multiply_numbers(a, b):
    multi = a * b
    return multi

def divide_numbers(a, b):
    
    if b == 0 or a == 0:
        return None
    divide = a / b
   
    return divide


num_list = [23, 44, 10]

# Addition
print("All numbers added to 5")
for num in num_list:  
    print(add_numbers(num, 5))
print("\n")

# Subtraction
print("Subtract All numbers by 5")
for num in num_list:    
    print(sub_numbers(num, 5))
print("\n")

# Divide
print("Divide All numbers by 5")
for num in num_list:
    print(divide_numbers(num, 0))
    
print("\n")

# Multiply
print("Multiply All numbers by 5")
for num in num_list:   
    print(multiply_numbers(num, 5))
    
