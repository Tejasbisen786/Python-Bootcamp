# This Function Calculate the avrage 
def calculate_average(scores):
    total_score = sum(scores)
    num_students = len(scores)
    average_score = total_score / num_students
    return average_score

file_name = "../Final_Assignment.py/marks.txt"   # adding enternal file 
with open(file_name, "r") as file:
    scores = [int(line.strip().split()[1]) for line in file]  # List Compression used and spilt fucntion separate the value and convert into the separate one 


# cheack for file file present not   it can also done using os module 
if scores:
    average_score = calculate_average(scores)
    print(f"The average score of all students is: {average_score:.2f}")
else:
    print("No scores found in the file.")
