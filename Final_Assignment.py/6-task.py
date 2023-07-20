total_score = 0
num_students = 0

file_path = "../Final_Assignment.py/marks.txt"

# Check if the file exists before reading it
import os
if not os.path.exists(file_path):
    print(f"Error: File '{file_path}' not found.")
else:
    with open(file_path, "r") as file:
        for line in file:
            name, score = line.split()
            total_score += int(score)
            num_students += 1

    if num_students == 0:
        print("No student scores found in the file.")
    else:
        average_score = total_score / num_students
        print(f"The average score of {num_students} students is: {average_score:.2f}")
