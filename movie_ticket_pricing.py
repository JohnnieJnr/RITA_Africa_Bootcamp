age = int(input("What is your age: "))
is_student = input("Are youu a student? True or False: ")
is_matinee = input("Is the movie a matinee? True or False: ")
print("\n")

if age < 12:
    print("The price of the movie ticket is $5.")
elif is_student is True and is_matinee is True:
    print("The price of the movie ticket is $8.")
else:
    print("The price of the movie ticket is $12.")