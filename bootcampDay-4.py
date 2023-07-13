# ***** Revision of List *****


# lists=["Ram",1,4.0,"TUshar"]
    #    -4   -3 -2   -1
# print(lists[-3:-1:1])


# homework Try with numbers including and exclusive 

# forwarding and reversing index 
# print(lists[-3:0:1])   # Return Zero 

# print(lists)




# ********SETS*******

# unordered changable Not-repeatable 
sets={1}


# sets always return the unique value 
# print(type(sets))
# newSets={1,"Tejas",3,4,"Bisen",4,5}  
# list = list(newSets)
# print(list)
# print(newSets)



# *****Dictionary ****


dict1=  { "TEjas":"momo","Kedar":"chapati","Tushar":"poha"}

# print(dict1.keys())
# using indexing 
# dict1["Kedar"] = "Kiran gobhi"
# print(dict1)

# Anothe way of declaring dictionary 

# new_dict= dict(name="Tejas",
#                age=20,


# print(new_dict)
# print(new_dict.keys())
# print(new_dict.values())



# **********File Handling 


# open name of the file 
# r  - read mode 
# a  - append mode 
# # w   - write mode 
 
# file = open("tejas.txt","r")
# print(file.read())
#  making a file and adding text 
file=open("tejas.txt","a")
file.write("Hii I'm tejas")
file.close()


# read the file 

# file = open("tejas.txt","r")
# print(file.read())
# file.close()

# delete the file 

# Real-life code
# module 
# eror handling 
# import os
# if os.path.exists("./tejas.txt"):
#     os.remove("./tejas.txt")
# else:
#     print("File Not Found")

