import math # here is the math module ehich perform the varipus mathematical operations 

    
myInput = float(input("Enter a number: "))   # Taking user input
if myInput < 0:
            print("Please enter a non-negative number.")
else:
            result = math.sqrt(myInput)   # Calcualtiong value Using Math Fuction 
            print(f"The square root of {myInput} is: {result:.2f}")


