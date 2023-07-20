# Implementing This task using Class And Object 
# Clararing the main class And it has consist the method 
class BankAccount:
    def __init__(self, acNumber, acName, PrimaryBalance=0):
        self.acNumber = acNumber
        self.acName = acName
        self.balance = PrimaryBalance


#   Adding Money logic 
    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount should be greater than 0."
        self.balance += amount
        return f"Deposited {amount:.2f} successfully. New balance: {self.balance:.2f}"
#   Withdarw Money Logic 
    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount should be greater than 0."
        if amount > self.balance:
            return "Insufficient balance."
        self.balance -= amount
        return f"Withdrew {amount:.2f} successfully. New balance: {self.balance:.2f}"

    def check_balance(self):
        return f"Account balance: {self.balance:.2f}"



# Crating Innstance for the class 

account1 = BankAccount("98343395XX", "Tejas Bisen", 1000)
print(account1.check_balance())


# accesing the method that defined inside the class with the hwlp of object 
print(account1.deposit(500))
print(account1.check_balance())

print(account1.withdraw(200))
print(account1.check_balance())
