names = ["John", "Doe", "Imane", "Sam", "Tolu"]
ages = [55, 13, 54, 76, 12]
age_threshold = 18

#Processing names 
for name in names:
    print(f"Processing {name}...")
print("\n")

#checking the age in the age list
for i in range(5):
    if ages[i] >= age_threshold:
        print(f"{names[i]} is eligible.")
    else:
        print(f"{names[i]} is ineligible.")


    



