#HOMEWORK:

#1
##num = float(input("Enter your price for your item:"))
##money = float(input("What amount of money are you paying with"))
##while num != "0.110" and money != "0.110":
##    change = money - num
##    print("Your change for this item is $", change, "\n")
##    num = float(input("Enter your price for your item:"))
##    money = float(input("What amount of money are you paying with"))

#2
##dec = (input("Name a decimal"))
##dot_count = dec.count(".")
##dot_index = dec.find(".")
##dot_index_check = dot_index!= 1 or dot_index != (len(dec)-1)
##while dot_count != 1 or dot_index_check == False or (dec[1:dot_index].isdigit()) == False  or (dec[dot_index+1:].isdigit()) == False:
##    print(dec, type(dec))
##    print("Try again. That isn't a decimal stupid")
##    dec = (input("Name a decimal"))
##    dot_count = dec.count(".")
##    dot_index = dec.find(".")
##    dot_index_check = dot_index!=1 and dot_index != (len(dec)-1)
##else:
##    dec=float(dec)
##    print(dec, type(dec))
##    print("Nice, it's a decimal.")


#3
##word = input("Type a string with some capitol letters")
##count = 0
##for letter in word:
##    if letter.isupper():
##        count += 1
##print(count)

#4
##while True:
##    temp=''
##    password = input("Enter a password(exit to stop)")
##    if password == "exit":
##        break
##    for letter in password:
##        if letter in "A" or letter in "a":
##            temp+="@"
##        elif letter in "S" or letter in "s":
##            temp +="$"
##        elif letter in "V" or letter in "v":
##            temp+="^"
##        elif letter in "O" or letter in "o":
##            temp +="0"
##        elif letter in "E" or letter in "e":
##            temp +="3"
##        elif letter in "L" or letter in "l":
##            temp +="|"
##        else:
##            temp += letter
##    print(temp)


#PRACTICE:
#1
##string = input("Type a string")
##for letter in string:
##    if letter.isalpha():
##        string = string.replace(letter, "*")
##print(string)

#2
##while True:
##    word= input('Enter a Word: ')
##    if word == 'Exit':
##        break
##    word=word.lower()
##    for letter in word:
##        if letter in 'aeiou':
##            print('_',end=' ')
##        else:
##            print(letter,end=' ')
##    print()
            
#3
##while True:
##    word= input('Enter a Word: ')
##    if word == 'Exit':
##        break
##    word=word.lower()
##    for letter in word:
##        if letter in 'bcdfghjklmnpqrstvwxyz':
##            print('_',end=' ')
##        else:
##            print(letter,end=' ')
##    print()
