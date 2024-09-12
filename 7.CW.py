# def area_square(width):
#     return width * width

# def area_rectangle(width, length):
#     return width * length

# def area_triangle(base, height):
#     return base * height / 2

# import math as m
# def area_circle(radius): # what information do you need?
#     return m.pow(radius,2) * m.pi # return the area of a circle

# print(area_square(4)) #The width times the width so 4*4
# print(area_rectangle(6,10)) # 6*10 = 60
# print(area_circle(10)) # call your circle function

#Classwork
name = "Robert Downey Jr."
title = "The Iron Giant"
# name and title are 'global' because they are not inside a function.

# def get_first_word(sentence):
#     space_index = sentence.index(' ')
#     first_word = sentence[:space_index]
# # space_index, first_word, and sentence only exist here
# # they are 'local' to this function!
# # can you print name or title here? Try it out
#     return first_word
# print(get_first_word('hi my name is vivan. i hate functions.'))
# print(first_word)

# score = 0
# def check_guess(guess, answer):
#     global score
#     if guess.lower() == answer.lower():
#         score += 1 # an equals sign means you're reassigning score
#     else:
#         score -= 1
# guess1 = input("What is the fastest mammal in the world?")
# check_guess(guess1, "Cheetah")
# print(score)

# guess1 = input("What is the biggest mammal in the world?")
# check_guess(guess1, "Whale")
# print(score)


# def employee_info(name, position = "Labourer"):
#    print(name, "\t", position)

# employee_info("Jenna", "Manager")
# employee_info("Karim", "Supervisor")
# employee_info("Paula")
# employee_info("Lori")


# def peri_sqr(width=1):
#     per = width * 4
#     return per

# print(peri_sqr(7))

# def max(*nums):
#     biggest_so_far = 0 # this only works for positive numbers
#     for num in nums: # nums is a collection!
#         if num > biggest_so_far:
#             biggest_so_far = num
#     return biggest_so_far
# print(max(1,2,34,7))




# def employee_info(name, position = "Labourer"):
#     print(name, "\t", position)
# # you can give them in any order if you use their names!
# employee_info(position="Supervisor", name="Kira")


# def max(*nums, positive = True):
#     if not positive:
#         return "This function only works for positive numbers!"
#     biggest_so_far = 0 # this only works for positive numbers
#     for num in nums: # nums is a collection!
#         if num > biggest_so_far:
#             biggest_so_far = num
#     return biggest_so_far
# # the collections still must come first
# print(max(1,2,3,4,positive = True))
# print(max(-2,-1,-10, positive = False))





#RESTART
# def sum(x, y):
#     ans = x + y
#     return ans

# print(sum(9, 7))

# def product(x=1, y=1):
#     ans = x * y
#     return ans

# print(product(99))

# def products(*nums):
#     ans = 1
#     for num in nums:
#         ans *= num 
#     return ans

# print(products(4,3,4,5))


#CLASSWORK:
#1
#Global variable is accessed anywhere whereas local is only accesable inside the code UNLESS you make it global

#2
#If you try to use a local variable outside it's function, it will produce a name error

#3
# def mini(*nums):
#     small = nums[0]
#     for num in nums:
#         if small > num:
#             small = num
#     return small

# print(mini(3,4,1,2,3,0,1,3,7,9,0,-2,3,4,5,6))

# def maxi(*nums):
#     big = nums[0]
#     for num in nums:
#         if big < num:
#             big = num
#     return big

# print(maxi(1,2,3,4,99,9,7,4,32))

# def avg(*nums):
#     avrge = 0
#     for num in nums:
#         avrge += num
#     total = avrge / len(nums)
#     return total


#4
def names(*nums):
    for num in nums:
        print(num,end='     ')
    return num

print(names("Jessica", "Nathan", "Immanual", "Vivan", "Shreya"))

#5
def info(name = "N/A", phone_number = "xxx-xxx-xxxx"):
    print(name, "\t", phone_number)

info()

#6
def quadr_area(length, width=0):
    if width == 0:
        return length ** 2
    elif width != 0:
        return length * width

print(quadr_area(7)) #length = 7, width = 0 -> 49

print(quadr_area(9, 3)) #length = 9, width = 3 -> 27

print(quadr_area(9)) #length = 9, width = 0 -> 81

print(quadr_area(3, 1)) #length = 3, width = 1 -> 3

#7
def sum_or_product(*nums, boolean):
    if boolean == True:
        return sum ((nums))
    elif boolean == False:
        product = 1
        for num in nums:
            product = product * num
        return product


print(sum_or_product(4, 5, 3, 2, boolean=True)) #4 + 5 + 3 + 2 = 14

#8
#optional variables are useful when you want to make things easier for yourself in repitition terms

#9
#The main benefit of using keyword-only parameters is when they are used together with positional-only parameters to remove difficulty.