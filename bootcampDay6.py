# ********** Classses and Objects **********
#

# me- bike , car , heli
# skin, healthnlife 


# Abstraction and Encapsulation 
# __init__ Function 
# bike ="Pulsar"
# bike1="Speed 400"
# car = "audi"
 

# Abstraction And Encapusulation 

# class Person :

#     def __init__(self,name, age, proof):
#         self.name=name
#         self.age=age
#         self.proof=proof

#         def bioData(self):
#             print("hii I am ,", self.name,
#                    "am",self.age,"year old , and i work as a",
#                     self.proof,"\n")



#             obj1 =Person("Tejas",21,"Developer")
#             obj1.bioData()
        

    
# class Cals:
#     def __init__(self, num, num2):

#         self.num = num

#         self.num2 = num2

#     def add(self):

#         return self.num + self.num2

#     def Subs(self):

#         return self.num - self.num2

#     def Multy(self):

#         return self.num * self.num2
#     def divs(self):

#         return self.num / self.num2

# cal = Cals(20, 10)

# print("Addition:",cal.add())

# print("Substraction:",cal.Subs())

# print("Multiplication:",cal.Multy())

# print("Division:",cal.divs())


class Student:
    def __init__(self):
        self.name="Tejas"
        self.id=100

    def biodata(self):
     print(f"The Name Of student Is: {self.name} with id : {self.id}")

class StudDetails(Student):
    def __init__(self):
        super().__init__()
        super().bioData()
        self.language="Python"
    def ProgramLang(self):
     print(f"The Defualt laguage for {self.name} is {self.language}")

    obj1=Student()
    obj1.ProgramLang()
    