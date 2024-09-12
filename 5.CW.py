#Review
# secret = ['O', 'l', ' ', 'e'] # we are assembling a secret
# secret.insert(1, 'n') # message!
# secret.insert(3, 'y')
# secret.insert(5, 'g') # write the list down on paper
# secret.extend(['n', 'i', 'u']) # and track the changes
# secret.append('s') # to find out what the list
# secret.append('e') # becomes
# secret.append('s')
# for letter in " can read":
#     secret.append(letter)
# print(secret)

#Modules: Math, Random, Daytime, 
#Math Functions:
# import math
# print(math.floor(2.5)) # 2.5 rounded down is 2!
# print(math.ceil(2.5)) # 2.5 rounded up is 3!
# print(math.fabs(2.5)) # gives us 2.5
# print(math.fabs(-2.5)) # ALSO gives us 2.5
# print(math.isclose(25,30,rel_tol = 10))
# #^^^^25 and 30 are less than 10 apart so this is True
# print(math.isclose(3,4,rel_tol = 0.05))
# #^^^^3 and 4 are more than 0.05 apart so this is False
# print(math.pow(2,3)) # 2 to the power of 3 is 8
# print(math.sqrt(16)) # square root of 16 is 4
# print(math.floor(math.pi)) # pi (3.14159...) rounded down is 3
# print(3 > math.inf) # False! 3 is not bigger than infinity!

# #Random Functions:
# import random as r
# col = [2,3,7,8,34,6,78,0,11,6]
# print(r.choice(col))
# print(r.randrange(1,10,2)) # some random odd number from 1-10
# print(r.randrange(10)) # some random number from 0 - 10
# print(r.sample(col, 3)) # 3 random UNIQUE items from col
# print(r.choices(col, k=9)) # 9 random items from col (may repeat)

# #Daytime Functions:
# from datetime import datetime as dt
# print(dt.now())#Shows date rn(excact time and date)
# print(dt.now().weekday())#shows date rn as a number
# print(dt.now().date())#Current date
# print(dt.now().time())#Current time

#Classwork:
#1 and 2
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
import datetime as d
today = d.datetime.now().weekday()
print("Today is", days[today])

#3
lst = []
inte = int(input("Enter a number: "))
lst.append(inte)
import math as m
print(m.pow(lst[0], 2))

#4, 5 and 6
employees = ["Jane", "Alice", "Matt", "Vivan", "Josh", "Yin", "Joseph", "Kinju", "Niomi", "Gurveer", "Jelle", "Demarcus", "Anton", "Bart", "Homer"]
group_size = int(input("How many people do you need for your 'requested' job: "))
import random as r
print(r.sample(employees,k=group_size))

#7(Will also figure out later lol)
diameter = int(input("Enter a diameter: "))
import math as m
piesss = m.pi
print(piesss * diameter)

#8 and 9
import turtle
sam = turtle.Turtle()
sam.shape("turtle")
sam.pencolor("blue")
sam.pensize(5)
sam.color("red")
sam.forward(100)
sam.left(144)
sam.forward(100)
sam.left(144)
sam.forward(100)
sam.left(144)
#It is trying to make a star but only has managed to make a four
sam.forward(100)
sam.left(144)
sam.forward(100)
