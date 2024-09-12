#Homework

#PART 1
string = "22 Delview Way"
print(string[3:14])
print(string[0:2], "\n")

#PART 2
print("Eight Ways to Print out 'e' with different indices(NOT TELLING HOW):")
stu = "The Pirates of the Caribbean"
print(stu[2])
print(stu[9])
print(stu[17])
print(stu[25])
print(stu[-3])
print(stu[-11])
print(stu[-19])
print(stu[-26])
print("\n")

#PART 3
secret = "Bkskrudnadjowjdol akSjditco0a20mricos diKs01iJksn9wlg"
print(secret[0:53:4])

#Challenge:
user = (input("Do you want to make an id?(press yes)"))

string = 'ucbwcoder'
while True:
     FN = input("Write your first name")
     LN = input("Write your last name")
     Id= FN[0]+LN[0]+string
     print(Id)
     pas = string[4:]+ string[0:3]
     password = (LN[0] + FN[0] + pas)
     print(password)
     user1 = input(
