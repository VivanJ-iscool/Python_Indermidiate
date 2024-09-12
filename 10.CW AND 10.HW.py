# # #EXAMPLES
# # f = open('myfile.txt')
# # content = f.read()
# # f.close()

# # f = open('myfile.txt','w')
# # f.write('bye\nlittle\nboy\n*shhhhhh*\n\n')
# # f.close()

# # print(content)

# # # with open('1.CW.py') as f:
# # #     print(f.read())
# # # f.close()

# # with open("myfile.txt") as fi:
# #     print(fi.readlines())#reads first line and puts it in same line/list while readlines() reads all lines and puts it in a list
# #     for line in fi:
# #         print(line)
# # fi.close()

# # #we did not send you your_name.txt! this code will create it!
# # f = open('your_name.txt','w')#w stands for write(edits and changes, doesnt add), a stands for append(adds, cant edit) and r stands for read(can see code, cant edit or add)
# # name = input("What is your name, user?")
# # f.write("last person to run this code is: " + name + "\n")
# # f.close()
# # #run this code a few times and see what happens to the file!


# #Classwork:

#1 & 2
candy_names = []
with open("candy_text.txt", "r") as can:
    for line in can.readlines():
        candy_names.append(line.split(",")[0])
print(candy_names)

#3
with open("long_poem_copy.txt", "r") as lp_copy:
    for line in lp_copy:
        print(line)#prints line
        lp_copy.readline()#reads line but doesn't print it, suppositly skipping the line

#4
with open ("second_poem_copy.txt") as sp_copy:
    sp_copy.readline()[0]
    for linez in sp_copy:
        print(linez)
        sp_copy.readline()
        sp_copy.readline()
        sp_copy.readline()
        sp_copy.readline()
        sp_copy.readline()

#5
codersz = open("all_coders.txt", "a")
name = input("What is your name, freind: ")
codersz.write(name)
codersz.close()
#6
with open ("file_knowledge.txt",'a') as smarts:
    smarts.write("A file is sort of like a new paper!\nIt stores data which coders can put in.\nThis data includes strings, integers, floats, bolean logic, lists, dictionaries and more!\nYou can access these files or even create them using with open!\n\nHowever... write is a function where you can change/append a file.\nThis can be dangerous due to the fact that you can hack and change somebodys code easily and access important information, which may include BANK DETAILS!\nI CAN HACK AND CHANGE STUFF NOW MWAHAHAHAHAHAAAA")
print(smarts)
smarts.close()

#7
with open ("pattern.txt",'a') as patt:
    for i in range(10,0,-1):
        patt.write(i * '*')
        patt.write('\n')
patt.close()

with open ("pattern.txt",'r') as patt:
    print(patt.read())
patt.close()

#HOMEWORK:

#    A = 8
#    B = 9
#    C = 2
#    D = 4
#    E = 6
#    F = 1



#Suhani's Question(s)
with open ("countries.txt,", "a") as countr:

    countries_capitols = {}
    country = input("What country would you like to add to your dictionary(type stop to stop adding countries)")
    capitol = input("What capitol would you like to add, coresponding to your country?(if country has no capitol, write naw)")
    while country != "stop":
        if country not in countries_capitols:
            countries_capitols[country] = capitol
            countr.write(country + ":" + capitol)
        country = input("What country would you like to add to your dictionary(type stop to stop adding countries)")
        capitol = input("What capitol would you like to add, coresponding to your country?(if country has no capitol, write naw)")