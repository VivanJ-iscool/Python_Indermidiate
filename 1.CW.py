#Index = position
#numbers reprsent characters in a string
#This implys only in the string aka ONLY IN QUOTES
#spaces also count

#Practice:
#1. Index One in "The brown dog" is n because you start at index 0
#2. The index of the "g" in "The brown dog" is index 12
#3. Index 3 in "the life of pi" is the first space

#HOW TO USE INDICES:
#one way of using indices is to print the string like so:
#                               "string"[]
#whatever index of a character is in the square brackets, that letter will print. It will appear as an error if you put in a index that does not exist in the string.

#Example of Indices:
#1
##secret_word = "snake"[0] + "sheep"[1] + "gorilla"[2] + "chamelion"[4] + "jellyfish"[4] + "cheetah"[5]
##print(secret_word, "is da best <3")

#SLICING

#slicing is like the range but with strings and instead of printing numbers,
#you print out the characters in the string (technically numbers but indices)

#Examples of slicing:
##string = "Blueberry Pancakes!"
##print(string[0:9:2])
#step is 2, meaning our slice includes index 0, 2, 4, ...
#this will print "Bubry"

##print(string[4:9:1]) # this prints 'berry'
#You do not even need 3 inputs to print this since the step is only by 1

##print(string[4:9])#this will print the same
#You do not even need a start or end in some cases!
#If you omit(ignore/leave it) the start, it starts at beggining (end only):

##print(string[:9])#this will be assumed as 0:9:1 which will print "Blueberry"

#If you omit the end, python will want you to go to the end (start only):

##print(string[10:])#this is the same as [10:19:1] which prints "Pancakes!"

#NEGAGIVE INDICES:
#JUST FROM RIGHT TO LEFT

#EXAMPLE OF NEGATIVE INDICES
##string = "Ultimate Coders"
##print(string[-1:-7:-1])
#This will print coders backwards like "sredoC"


#CLASSWORK:
#1
string1 = "Strawberry Shortcake"
print(string1[0])
print(string1[11])
print(string1[-9])
print(string1[-20])

#2
name = input("What is your name?")
print(name[0])

#3
print(name[-1:len(name) - len(name) * 2 - 1:-1])

#4
message = "ccowdcionygy nrzuclwepsq!q"
print(message[0:25:2])

#5
name = "Justin Timberlake"
var = name[7:]+name[:6]
print(var)
#6
secret = "isagbnxiwrptysu ctuueogbyal hlklrae qweoinbkp zusoyY"
print(secret[-1:-52:-2])











