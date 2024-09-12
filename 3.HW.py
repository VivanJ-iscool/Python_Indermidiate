#HomeWork:
#1 and 2
# stringz = ["vivan", "suhani", "shreya", "bob:)"]
# # for item in stringz:
# #     print(item)

# #3(Will come back to next class)
# while True:
#     for item in stringz:
#         print(item)
#     add_to_list = input("Do you want to add to the list or modify the list?(add or modify)")
#     if add_to_list == "add":
#         value = input("What do you want to add?")
#         stringz = stringz + [value]
#     elif add_to_list == "modify":
#         index = (input("What index do you want to change?"))
#         while index.isdigit() == False or int(index) < 0 or int(index) >= len(stringz) :
#             index = (input("What index do you want to change?"))
#         else:
#             index=int(index)
#         string_replace = input("What string should it be replaced with")
#         stringz[index]=string_replace
    

#4
#A string is anything surrounded by collons and ONLY COLLONS while a list are multiple strings, integers, floats or variables in one sequenced order.

#5
#This error only occurrs when you try to access an element that isn't in the actual list and doesn't exist.
        

#MR.S SHREYA'S CHALLENGE:
# fn = []
# ln = []
# full_name=[]
# while True:
#     First_name = input("What do want for yout first name? This will be added to the list.(say no to stop)")
#     fn = fn + [First_name]
#     Last_name = input("What do want for yout last name? This will be added to the list.(say no to stop)")  
#     ln = ln + [Last_name]

#     ch = input("Enter y to continue adding to the list")
#     if ch.lower() != "y":
#         break
# for i in range(len(fn)):
#     full_name+= fn[i].title()+ ln[i].title()
#     for i in range():

lst = ["hello", "ucbw"]
lst = lst + ["var"]
print(lst)

names = []
first_name = input("What is your name: ")
last_name = input("What is your last name? ")
while True:
    name = first_name +" "+ last_name
    names = names + [name]
    add = input("do you want to add to the list(type yes to continue, type anything else but yes to stop)")
    if add == "yes":
            first_name = input("What is your name: ")
            last_name = input("What is your last name? ")
    else:
          break
print(names)