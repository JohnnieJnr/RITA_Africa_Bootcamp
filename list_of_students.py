def process_students():
    # Define function double_score
    def double_score(score):
        return score * 2

    # Create the list of students
    students = [
        {"name": "Alice", "score": 10},
        {"name": "Bob", "score": 15},
        {"name": "Charlie", "score": 20},
        {"name": "Diana", "score": 25}
    ]

    # Iterate through the students list
    for student in students:
        original_score = student["score"]
        doubled_score = double_score(original_score)
        
        # Print the output
        print(f"Student: {student['name']}, Original Score: {original_score}, Doubled Score: {doubled_score}")

# Call the function
process_students()
