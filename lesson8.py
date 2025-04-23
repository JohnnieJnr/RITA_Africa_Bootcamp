fruits = ["apple","banana","orange","avocado","pineapple"]


first_element = fruits[0]
second_element = fruits[1]
last_element = fruits[-1]
second_to_last_element = fruits[-2]

fruits.remove("orange")

remove_element = fruits.pop(3)

print(fruits)


fruits_tuple = ["apple","banana","avocado","pineapple"]

if "orange" in fruits_tuple:
    print("Yes, orange is in the tuple")
else:
    print("No, orange is not in the tuple")

