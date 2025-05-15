number = {1, 2, 3, 4, 5}

fruits = {"apple", "banana", "orange"}

mixed_list = {1, 2, 3.5, "apple", "banana", True}


fruits_set = {"apple", "banana", "orange", "avocado", "pineapple"}

if "orange" in fruits_set:
    print("Yes, orange is in the set.")
else:
    print("No, orange is not in the set")
print("\n")


# Example 2
fruits_set = {"apple", "banana", "orange", "avocado", "pineapple"}

# Adding a new element to the set
fruits_set.add("Kiwi")

# Display the modified set
print(fruits_set)
print("\n")

#Example
fruits_set = {"apple", "banana", "orange", "avocado", "pineapple"}

# Adding multiple elements to the set
fruits_set.update(["grape", "watermelon"])

# Display the modified set
print(fruits_set)
print("\n")

# Example 2
fruits_set = {"apple", "banana", "orange", "avocado", "pineapple"}

# Removing the element "banana"
fruits_set.remove("banana")

# Display the modified set
print(fruits_set)

# Dictionaries
# Example 1: Membership Information
menmber_info = {'name': 'Jael', 'Age': 25, 'city': 'Accra'}

# Example 2: Student Information
student_info = {
    "name": "Abdul Rasheed",
    "age": 20,
    "grade": "A",
    "subjects": ["Math", "Science", "English"]
}

# Example
fruits_dict = {
    "appple": 1,
    "banana": 2,
    "orange": 3,
    "avocado": 4,
    "pineapple": 5
}

# Modifying the value for the key "banana"
fruits_dict["banana"] = 10

# Display the modified dictionary
fruits_dict


# Adding a new key-value pair
fruits_dict ["kiwi"] = 8

# Display the modified dictionary
fruits_dict

# Removing the key-value pair for the key "apple"
fruits_dict.pop("apple")

# Dispay the modified dictionary
fruits_dict

# Other removal options


original_dict = {'name': 'Jael', 'Age': 25, 'city': 'Accra'}

age_value = original_dict.get('Age')

print("Get Result: ", age_value)

original_dict = {'name': 'Jael', 'Age': 25, 'city': 'Kumasi'}

key_list = original_dict.keys()

print("Keys Result: ", key_list)

# Iterate through keys
my_dict = {
    "appple": 1,
    "banana": 2,
    "orange": 3,
    "avocado": 4,
    "pineapple": 5
}

for key in my_dict:
    print(key)

# Iterate through values
fruits_dict = {
    "appple": 1,
    "banana": 2,
    "orange": 3,
    "avocado": 4,
    "pineapple": 5
}

for value in my_dict.values():
    print(value)

# Iterate through key-value pair
fruits_dict = {
    "appple": 1,
    "banana": 2,
    "orange": 3,
    "avocado": 4,
    "pineapple": 5
}

for key, value in my_dict.items():
    print(key, value)