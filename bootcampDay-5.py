# result=1
# for i in range(1,11):
#     result+=i
# print(result)

# Dictonary 
new_dict=dict(name="Tejas",age=20,place="gondia")
# print(new_dict)

# #accesss
# new_dict["age"]=25
# print(new_dict)

# #delete
# del new_dict["place"]
# print(new_dict)

# # addding a new element in dictinary 

# new_dict["place"]= "Mumbai"
# print(new_dict)

# # Adding profession in Dictinonary 
# new_dict["Profession"]="BE"
# print(new_dict)

# new_dict["course_Complete"]=True
# print(new_dict)

def myfuc():
    global sum
    sum=0
    for i in range(1,11):
        sum+=i
        return sum
    res =myfuc()

    print(res)

