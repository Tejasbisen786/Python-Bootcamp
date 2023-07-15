# Manual Process 

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = []

# for x in fruits:
#   if "a" in x:
#     newlist.append(x)

# print(newlist)


# # ***List Comprehension Example *****

# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# print(newlist)

# Constructing output list WITHOUT
# Using List comprehensions
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
  
output_list = []
  
# Using loop for constructing output list
# for var in input_list:
#     if var % 2 == 0:
#         output_list.append(var)
  
# print("Output List using for loop:", output_list)


# Using List comprehensions
# for constructing output list
  
# input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
  
  
# list_using_comp = [var for var in input_list if var % 2 == 0]
  
# print("Output List using list comprehensions:",
#                                list_using_comp)

# Constructing output list
# using list comprehension
# list_using_comp = [var**2 for var in range(1, 10)]
  
# print("Output List using list comprehension:", 
#                               list_using_comp)




  
# input_list = [1,2,3,4,5,6,7]
  
# dict_using_comp = {var:var ** 3 for var in input_list if var % 2 != 0}
  
# print("Output Dictionary using dictionary comprehensions:",
#                                            dict_using_comp)


# state = ['Gujarat', 'Maharashtra', 'Rajasthan']
# capital = ['Gandhinagar', 'Mumbai', 'Jaipur']
  
# output_dict = {}
  
# # Using loop for constructing output dictionary
# for (key, value) in zip(state, capital):
#     output_dict[key] = value
  
# print("Output Dictionary using for loop:",
#                               output_dict)