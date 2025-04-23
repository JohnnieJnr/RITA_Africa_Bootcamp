import re

password = str(input("Type your preferred password: "))
lenght = len(password)
has_uppercase =  bool(password.upper())
has_lower = bool(password.lower())
has_digit = bool(re.search(r'\d', password))
has_special_char = bool(password.isascii())

if lenght >= 8 and has_uppercase is True and has_lower is True and has_digit is True and has_special_char is True:
    print("Strong password")
elif lenght >= 8 and has_uppercase is True and has_lower is True and has_digit is True and has_special_char is False:
        print("Moderate password. Consider adding more complexity.")
elif lenght >= 8 and has_uppercase is True and has_lower is True and has_digit is False and has_special_char is True:
        print("Moderate password. Consider adding more complexity.")
elif lenght >= 8 and has_uppercase is True and has_lower is False and has_digit is True and has_special_char is True:
        print("Moderate password. Consider adding more complexity.")
elif lenght >= 8 and has_uppercase is False and has_lower is True and has_digit is True and has_special_char is True:
        print("Moderate password. Consider adding more complexity.")
elif lenght < 8:
        print("Weak Password. It should be at least 8 characters long")
else:
    print("Your password does not meet any of the criteria. consider adding more complexity.")

