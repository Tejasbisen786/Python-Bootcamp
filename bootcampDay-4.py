# Reading the scores from the text file and calculating the average score

total_score = 0
num_students = 0

# Assuming the file is in the same directory as the Python script
file_path = "./Final_Assignment.py/marks.txt"


with open(file_path, 'r') as file:
        for line in file:
            name, score = line.strip().split()
            score = int(score)
            total_score += score
            num_students += 1

if num_students == 0:
        print("No student scores found in the file.")
else:
        average_score = total_score / num_students
        print(f"The average score of {num_students} students is: {average_score:.2f}")

