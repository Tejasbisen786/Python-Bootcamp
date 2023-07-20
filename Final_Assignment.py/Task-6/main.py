def calculate_average(scores):
    total_score = sum(scores)
    num_students = len(scores)
    average_score = total_score / num_students
    return average_score

file_name = "scores.txt"
with open(file_name, "r") as file:
    scores = [int(line.strip().split()[1]) for line in file]

if scores:
    average_score = calculate_average(scores)
    print(f"The average score of all students is: {average_score:.2f}")
else:
    print("No scores found in the file.")
