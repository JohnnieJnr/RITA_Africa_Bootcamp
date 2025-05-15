try:
    user_input = input("Enter a number: ")
    result = user_input + 5
   
except Exception as e:
    print("Error: Can not add string to an integer without casting")



try:
    numberator = int(input("Enter a numberator: "))
    denominator = int(input("Enter a denominator: "))

    result = numberator / denominator
    print("Result: ", result)
except Exception as e:
    print("Error: Invalid input. Please enter valid numeric input")
except ZeroDivisionError as e:
    print("Error: Division by zero is not allowed")


try:
    numberator = int(input("Enter a numberator: "))
    denominator = int(input("Enter a denominator: "))

    result = numberator / denominator
    print("Result: ", result)
except Exception as e:
    print("Error: Invalid input. Please enter valid numeric input")
except ZeroDivisionError as e:
    print("Error: Division by zero is not allowed")
except:
    print("An unexpected error occured")