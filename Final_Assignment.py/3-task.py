# fuction cheak whether person eligible for Vote or Not  

def checkAgeForVote(age):
    if age>=18:
        print("Eligible For Vote")
    else:
        print("Not Eligible For Vote")  

#  Taking Input age From Person
age=int(input("Enter Your Age For Vote:")) 
VoteResult=checkAgeForVote(age)



