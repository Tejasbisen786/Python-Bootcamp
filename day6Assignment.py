# Abstraction and Encapsulation 

# class Person :
#     def __init__(self,name,age,prof):
#         self.name= name
#         self.age= age
#         self.prof= prof

#         def bioData(self):
#             print(self.name)


#             obj1 = Person("Tejas",21,"Programmer")
#             obj1.bioData


class makeAdd:
  def __init__(self,num,num1):
    self.num=num
    self.num1=num1

  def add(self):
    print("Addition is:",self.num+self.num1)

    n1=makeAdd(12,13)
    n1.add()

# class Doadd():
#     def __init__(self,num,num1):
#         self.num=num
#         self.num1=num1

#         def doAddition(self):
#             print("addition is : ", self.num + self.num1)
        
# n1=Doadd(12,45)
# n1.doAddition()

#         class calculator():
#   def __init__(self,x,y):
#     self.x=x
#     self.y=y

#   def add(self):
#     print("Sum :",self.x+self.y)

#   def subtraction(self):
#     print("Subtraction :",self.x-self.y)  

#   def multiplication(self):
#     print("Multiplication :",self.x*self.y)

#   def division(self):
#     print("Division :",self.x/self.y)  
# #x=int(input("Enter first number : "))
# #y=int(input("Enter second number : "))
# #n1=calculator(x,y) # object 
# n1=calculator(5,4) # object 

# n1.add()
# n1.subtraction()
# n1.multiplication()
# n1.division()


# Calculator Program using Procedural Programming 

# def getAdd(num ,num1):
#     return num+num1
# def getSub(num ,num1):
#     return num-num1
# def getMul(num ,num1):
#     return num*num1
# def getDiv(num ,num1):
#     return num/num1

# num = int(input("Enter The First Numbe: r"))
# num1= int(input("Enter The Second Number: "))
# res= getAdd(num,num1)
# print("Addition is:",res)
# res= getSub(num,num1)
# print("Subtraction is: ",res)
# res= getSub(num,num1)
# print("Division is: ",res)
# res= getMul(num,num1)
# print("Multiplication is: ",res)

# Polymorphism And Inheritance 
