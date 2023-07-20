# Importing from the custom package 'my_project'
from module1 import multiply, divide
from module2 import Dog


    # Using functions from module1
result_multiply = multiply(5, 3)
result_divide = divide(10, 2)

print(f"Multiplication: {result_multiply}")
print(f"Division: {result_divide}")

    # Using class from module2
dog = Dog("Buddy")
dog_bark = dog.bark()
print(dog_bark)
