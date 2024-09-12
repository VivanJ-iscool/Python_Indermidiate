#Review
# titles = ["the littlest dinosaur", "tiny dinosaur","itsy bitsy dino", "the dinosaur that never growed"]
# print(titles)
# titles[3] = 'the dinosaur that never growed to the dinosaur that never grew'
# print(titles)

#list methods:
#APPEND will add a new element added to the end
#EXTENED will copy the base list and repeat it so it prints twice
#INSERT will add a string and the index you use will be where BEFORE the string goes. Pretty much, a string gets added before the index you put.
#REMOVE will need an element from the list to remove and it will remove it.
#POP will remove also but can come back if in a variable. keep in mind that you cannot do this with any other list method.
#SORT will sort the list's elements in alphebetical order
#REVERSE will reverse the order of the base list

# Examples:
lst = ['a', 'b', 'c', 'e', 'f', "k", "o", "v"]

# lst.append('g') # notice we DO NOT write list =list.append('g')
# print(lst)#Adds g to the end

# lst.insert(3, "d")
# print(lst)#Inserts d at index 3 to create a NEW Index 3

# lst.extend(["h", "i"])
# print(lst)

# lst.remove('b') # remove the ITEM 'b' from the list
# print(lst)

# x = lst.pop(1) # remove item at INDEX 1, and store item in x
# print("The letter that got removed is", x)
# print(lst)

# lst.sort() # now our list is sorted
# print(lst)

# lst.reverse() # now our list is reversed
# print(lst)

# a = lst.sort()
# print(a)#Not what i was expecting. it said none because u cannot short or store a list in a variable. it will pop up as none.


#CLASSWORK

#1 It prints Monday, Tuesday, Wednesday

#2 The third and fourth line are mutable

#3, 4 and 5
# fav_animals = ["Dog","Shark", "Lion", "Monkey", "Giraffe"]
# fav_animals.insert(2, "Chamelion")
# fav_animals.sort()
# fav_animals.remove("Giraffe")
# print(fav_animals)

#6 will do in class
# for ind in range(len(fav_animals)):
#     print(ind)
#     fav_animals[ind] = fav_animals[ind] + "!"
# print(fav_animals)

#7
# best_animals = ["dog", "cat", "mouse", "shark", "chicken", "chamelion"]
# a = best_animals.pop(0)
# b = best_animals.pop(1)
# c = best_animals.pop(2)
# three_animals = [a, b, c]
# print(three_animals)

#8
#Lists consist of varriables, numbers and strings while strings are just strings
#Lists are mutable while strings aren't

#9
#Mutablity is when you hae the abilit to change it with code such as methods.

#EXAMPLES
# lst = ["dog", "cat", "mouse", "shark", "chicken", "chamelion", "cat"]
# lst.remove("cat")
# #at this point lst is ['dog', 'mouse', 'shark', 'chicken', 'chamelion', 'cat']
# lst.remove("cat")
# #at this point lst is ['dog', 'mouse', 'shark', 'chicken', 'chamelion']
# var = lst.pop(2)
# print(var)
# print(lst)


# #Extend and append

# lst2 = ["hello", "world", "at", "UCBW"]
# lst2.append(["2024","hii"]) 
# print(lst2)
# lst2.extend(["2024","hii"])
# print(lst2)