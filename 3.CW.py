#Review
##password = "U1tra_Secret_P@ssw0rd"
#c = 0
#s = 0
#d = 0
#for character in password:
#    if not (character.isalnum()):
#        s += 1
#    elif not character.isalpha() and character.isalnum():
#        d += 1
#    elif character.isupper():
#        c += 1
#if c >= 2 and d >= 2 and s >= 2:
#    print("That's a strong password!")
#else:
#    print("You should try to make a stronger password!")

#Lists
#lst = ["jermey", 12, "Kang", "vj", 2.35]
#print(lst)
#CLASSWORK:
#1
class_votes = ["Jen", "Jayden", "Jared", "Jen", "Jen", "Jayden", "Jayden", "Jen"]
print(class_votes)
jen_counter= 0
for item in class_votes:
    if item == "Jen":
        jen_counter+=1
print("There are", jen_counter, "class votes for Jen.")
        
#2
Jayden_counter = class_votes.count(("Jayden"))
Jaren_counter = class_votes.count(("Jaren"))
if jen_counter > Jayden_counter and jen_counter > Jaren_counter:
    print("The winner is Jen!")
elif Jayden_counter > jen_counter and Jayden_counter > Jaren_counter:
    print("The winner is Jayden!")
elif Jaren_counter > Jayden_counter and Jaren_counter > jen_counter:
    print("The winner is Jaren!")

#3
friends_names = ["jeremy", "jason", "jaymit", "river", "lily", "jen", "ben", "harley", "frida"]
friends_names+=['prisha','lisa','nathan']
print(friends_names)
friends_names_counterj = 0

#4
for item in friends_names:
    if item[0] == "j" or item[0] == 'J':
        friends_names_counterj += 1
print("There are", friends_names_counterj, "friends whos name starts with J")

#5
for i in range(len(friends_names)):
  friends_names[i] = friends_names[i].upper()
print(friends_names)

